JAVA_URL="https://oasislmf-model-library-open-models-uclfitter.s3.eu-west-1.amazonaws.com/java/footprint.bin.z"
SUMATRA_URL="https://oasislmf-model-library-open-models-uclfitter.s3.eu-west-1.amazonaws.com/sumatra/footprint.bin.z"

wget "$JAVA_URL" -O model_data/java/footprint.bin.z
wget "$SUMATRA_URL" -O model_data/sumatra/footprint.bin.z
