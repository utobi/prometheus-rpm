#!/bin/bash -x
shopt -s globstar

NAMES=( alertmanager graphite_exporter jmx_exporter node_exporter prometheus pushgateway )

for NAME in "${NAMES[@]}"; do
    VERSION=$(cat "$NAME/VERSION")
    echo "Releasing $NAME in version $VERSION"
    for i in **/RPMS/*.rpm; do 
        ../upload-github-release-asset.sh github_api_token="$(TOKEN)" owner="utobi" repo="prometheus-rpm" tag="$(NAME):v$(VERSION)" filename="$i"
    done
done


