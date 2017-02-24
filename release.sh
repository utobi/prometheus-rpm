#!/bin/bash
###
# Requires https://github.com/aktau/github-release to be correctly installed and in $PATH
#
shopt -s globstar

NAMES=( alertmanager graphite_exporter jmx_exporter node_exporter prometheus pushgateway )
USER="utobi"
REPO="prometheus-rpm"

for NAME in "${NAMES[@]}"; do
    VERSION=$(cat "$NAME/VERSION")
    TAG=v"$VERSION"__"$NAME"
    echo "Releasing $NAME in version $VERSION"
    export GITHUB_TOKEN=$TOKEN
    github-release release \
        --user $USER \
        --repo $REPO \
        --tag $TAG \
        --name "$TAG" \

    for i in $NAME/rpmbuild/**/*.rpm; do
        github-release upload \
            --user $USER \
            --repo $REPO \
            --tag $TAG \
            --name "$(basename $i)" \
            --file "$i"
    done
done


