#!bin/bash

# To use this script, first run ./verify.sh
# Then with the results:
# 1. Go to sourcify.dev
# 2. Add metadata.json from build/metadata/<ContractName>/metadata.json to the upload dialog
# 3. Add all files in sources-flattened-dir to the dialog
# 4. Set the contract address and upload

ROOTDIR="$(pwd)/$(dirname $0)"
SOURCES_DIR=$ROOTDIR/sources-flattened-dir

mkdir -p "$SOURCES_DIR"
cp -R contracts/ $SOURCES_DIR/contracts/

CONTRACTS=(
    "contracts/Swap.sol"
    "contracts/SwapUtils.sol"
    "contracts/MathUtils.sol"
)

for CONTRACT in ${CONTRACTS[@]}; do
    echo "$CONTRACT"
    CBASENAME=$(basename $CONTRACT)
    CBASE=${CBASENAME%.sol}
    CONTRACT_DIR=$ROOTDIR/build/metadata/$CBASE/
    mkdir -p "$CONTRACT_DIR"
    docker run -v "$SOURCES_DIR/:/sources" -w /sources ethereum/solc:0.6.12 \
        --optimize --optimize-runs 5000 \
        --combined-json abi,bin,bin-runtime,compact-format,devdoc,hashes,interface,metadata "$CONTRACT" \
        | jq ".contracts | to_entries | map(select(.key | contains(\":$CBASE\"))) | first | .value " \
        > $CONTRACT_DIR/artifact.json
    cat $CONTRACT_DIR/artifact.json | jq -r ".metadata" > $CONTRACT_DIR/metadata.json
done

cp -R $SOURCES_DIR/contracts/**/*.sol "$SOURCES_DIR"
rm -fr $SOURCES_DIR/contracts/