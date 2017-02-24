#!/bin/bash 
#-x
shopt -s globstar
shopt -s extglob

[[ -z "$REPOSITORY" ]] && { echo "\$REPOSITORY is empty" ; exit 1; }
[[ -z "$REPOSITORY_CREDENTIALS" ]] && { echo "\$REPOSITORY_CREDENTIALS is empty" ; exit 1; }
[[ -z "$GROUPID" ]] && { echo "\$GROUPID is empty" ; exit 1; }


NAMES=( alertmanager graphite_exporter jmx_exporter node_exporter prometheus pushgateway )

for NAME in "${NAMES[@]}"; do
    VERSION=$(cat "$NAME/VERSION")
    echo "Deploying $NAME in version $VERSION to Nexus"
    for i in $NAME/**/RPMS/**/!(*sysvinit*).rpm; do
        echo "   Deploying $i" 
        curl -v -F r="$REPOSITORY" -F hasPom=false -F e=rpm -F g="$GROUPID" -F a="$NAME" -F v="$VERSION" -F p=RPM -F file=@"$i" -u "$REPOSITORY_CREDENTIALS" "$REPOSITORY_URL"
    done
    for i in $NAME/**/RPMS/**/*sysvinit*.rpm; do 
        echo "   Deploying $i"
        curl -v -F r="$REPOSITORY" -F hasPom=false -F e=rpm -F g="$GROUPID" -F a="$NAME".sysvinit -F v="$VERSION" -F p=RPM -F file=@"$i" -u "$REPOSITORY_CREDENTIALS" "$REPOSITORY_URL"
    done
done



