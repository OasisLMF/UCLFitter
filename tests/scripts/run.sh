#!/bin/bash

# Enhanced run.sh script that accepts arguments for flexible test execution
# Usage: ./run.sh [TEST_DIRECTORY] [CONFIG_FILE] [OPTIONS]

set -e  # Exit on any error

# Default values
DEFAULT_TEST_DIR="../test_java"
DEFAULT_CONFIG="oasislmf.json"
VERBOSE=false
DRY_RUN=false
OUTPUT_DIR=""

# Color codes for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_info() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Function to display help
show_help() {
    cat << EOF
Usage: $0 [OPTIONS] [TEST_DIRECTORY] [CONFIG_FILE]

Run OasisLMF model tests with flexible configuration.

ARGUMENTS:
    TEST_DIRECTORY    Directory containing test files (default: $DEFAULT_TEST_DIR)
    CONFIG_FILE       Configuration file to use (default: $DEFAULT_CONFIG)

OPTIONS:
    -h, --help        Show this help message
    -v, --verbose     Enable verbose output
    -d, --dry-run     Show what would be executed without running
    -o, --output DIR  Specify custom output directory
    --no-venv         Skip virtual environment activation

EXAMPLES:
    $0                                    # Run with defaults
    $0 ../test_policy_test_2              # Run specific test directory
    $0 ../test_java custom_config.json    # Run with custom config
    $0 -v -o /tmp/output ../test_java     # Verbose mode with custom output

EOF
}

# Parse command line arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        -h|--help)
            show_help
            exit 0
            ;;
        -v|--verbose)
            VERBOSE=true
            shift
            ;;
        -d|--dry-run)
            DRY_RUN=true
            shift
            ;;
        -o|--output)
            OUTPUT_DIR="$2"
            shift 2
            ;;
        --no-venv)
            NO_VENV=true
            shift
            ;;
        -*)
            print_error "Unknown option: $1"
            show_help
            exit 1
            ;;
        *)
            if [[ -z "$TEST_DIR" ]]; then
                TEST_DIR="$1"
            elif [[ -z "$CONFIG_FILE" ]]; then
                CONFIG_FILE="$1"
            else
                print_error "Too many arguments"
                show_help
                exit 1
            fi
            shift
            ;;
    esac
done

# Set defaults if not provided
TEST_DIR="${TEST_DIR:-$DEFAULT_TEST_DIR}"
CONFIG_FILE="${CONFIG_FILE:-$DEFAULT_CONFIG}"

# Verbose output function
verbose_print() {
    if [[ "$VERBOSE" == "true" ]]; then
        print_info "$1"
    fi
}

# Dry run execution function
execute_command() {
    local cmd="$1"
    local description="$2"
    
    if [[ "$DRY_RUN" == "true" ]]; then
        print_warning "[DRY RUN] Would execute: $cmd"
        return 0
    fi
    
    verbose_print "$description"
    verbose_print "Executing: $cmd"
    
    if eval "$cmd"; then
        verbose_print "Command succeeded"
        return 0
    else
        print_error "Command failed: $cmd"
        return 1
    fi
}

# Main execution starts here
print_info "Starting OasisLMF test execution"
print_info "Test Directory: $TEST_DIR"
print_info "Config File: $CONFIG_FILE"

# Navigate to project root
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"

verbose_print "Script directory: $SCRIPT_DIR"
verbose_print "Project root: $PROJECT_ROOT"

execute_command "cd '$PROJECT_ROOT'" "Changing to project root directory"

# Activate virtual environment (unless --no-venv is specified)
if [[ "$NO_VENV" != "true" ]]; then
    if [[ -f ".venv/bin/activate" ]]; then
        execute_command "source .venv/bin/activate" "Activating virtual environment"
        print_success "Virtual environment activated"
    else
        print_warning "Virtual environment not found at .venv/bin/activate"
        print_warning "Continuing without virtual environment activation"
    fi
fi

# Navigate to test directory
TEST_FULL_PATH="$PROJECT_ROOT/tests/$TEST_DIR"
if [[ "$TEST_DIR" == /* ]]; then
    # Absolute path provided
    TEST_FULL_PATH="$TEST_DIR"
elif [[ "$TEST_DIR" == ../* ]]; then
    # Relative path from project root/tests
    TEST_FULL_PATH="$PROJECT_ROOT/tests/$TEST_DIR"
fi

verbose_print "Full test path: $TEST_FULL_PATH"

if [[ ! -d "$TEST_FULL_PATH" ]]; then
    print_error "Test directory does not exist: $TEST_FULL_PATH"
    exit 1
fi

execute_command "cd '$TEST_FULL_PATH'" "Changing to test directory"

# Check if config file exists
if [[ ! -f "$CONFIG_FILE" ]]; then
    print_error "Configuration file not found: $CONFIG_FILE"
    print_info "Available files in directory:"
    ls -la
    exit 1
fi

print_success "Configuration file found: $CONFIG_FILE"

# Prepare oasislmf command
OASIS_CMD="oasislmf model run -C '$CONFIG_FILE'"

# Add output directory if specified
if [[ -n "$OUTPUT_DIR" ]]; then
    # Create output directory if it doesn't exist
    execute_command "mkdir -p '$OUTPUT_DIR'" "Creating output directory"
    OASIS_CMD="$OASIS_CMD --output-dir '$OUTPUT_DIR'"
fi

# Add verbose flag if requested
if [[ "$VERBOSE" == "true" ]]; then
    OASIS_CMD="$OASIS_CMD --verbose"
fi

# Execute the main command
print_info "Running OasisLMF model..."
if execute_command "$OASIS_CMD" "Running OasisLMF model with configuration $CONFIG_FILE"; then
    print_success "OasisLMF model execution completed successfully!"
    
    # List output files if verbose
    if [[ "$VERBOSE" == "true" ]]; then
        print_info "Generated output files:"
        if [[ -d "output" ]]; then
            ls -la output/
        elif [[ -n "$OUTPUT_DIR" && -d "$OUTPUT_DIR" ]]; then
            ls -la "$OUTPUT_DIR"/
        fi
    fi
else
    print_error "OasisLMF model execution failed!"
    exit 1
fi

print_success "Test execution completed!"
