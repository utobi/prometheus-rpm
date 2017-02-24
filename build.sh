#!/bin/bash
NAMES=( alertmanager graphite_exporter jmx_exporter node_exporter prometheus pushgateway )

for NAME in "${NAMES[@]}"; do
    VERSION=$(cat "$NAME/VERSION")
    echo "Building $NAME in version $VERSION"
    cd $NAME && rm -rf rpmbuild && make && cd ..
done

