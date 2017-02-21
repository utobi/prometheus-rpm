NAME="prometheus"
VERSION?=$(shell cat VERSION)
TOKEN?="TODO: SET A TOKEN"
PWD=$(shell pwd)

all: rpm clean

rpm:
	mkdir -p "$(PWD)/rpmbuild"
	mkdir -p "$(PWD)/rpmbuild/SOURCES/"
	cd "$(PWD)/rpmbuild/SOURCES" && wget https://github.com/prometheus/prometheus/releases/download/v$(VERSION)/prometheus-$(VERSION).linux-amd64.tar.gz
	cd "$(PWD)/rpmbuild/SOURCES" && tar xzvf *tar.gz
	cp -Rv contrib "$(PWD)/rpmbuild/SOURCES/prometheus-$(VERSION).linux-amd64"
	cd "$(PWD)/rpmbuild/SOURCES" && tar cvfz prometheus-$(VERSION).linux-amd64.tar.gz prometheus-$(VERSION).linux-amd64
	rpmbuild --define "version $(VERSION)" --define '_topdir '"$(PWD)/rpmbuild" -ba --clean contrib/prometheus.spec
	rpmbuild --with sysvinit --without systemd --define "version $(VERSION)" --define '_topdir '"$(PWD)/rpmbuild" -ba --clean contrib/prometheus.spec

### deploy to nexus
deploy:
	curl -v -F r=$(REPOSITORY) -F hasPom=false -F e=rpm -F g=$(GROUPID) -F a=prometheus.systemd -F v=$(VERSION) -F p=RPM -F file=@$(WORKSPACE)/prometheus/rpmbuild/RPMS/x86_64/prometheus-systemd-$(VERSION)-1.$(OS_NAME).x86_64.rpm -u $(REPOSITORY_CREDENTIALS) $(REPOSITORY_URL)
	curl -v -F r=$(REPOSITORY) -F hasPom=false -F e=rpm -F g=$(GROUPID) -F a=prometheus.sysvinit -F v=$(VERSION) -F p=RPM -F file=@$(WORKSPACE)/prometheus/rpmbuild/RPMS/x86_64/prometheus-sysvinit-$(VERSION)-1.$(OS_NAME).x86_64.rpm -u $(REPOSITORY_CREDENTIALS) $(REPOSITORY_URL)

tag:
	git tag -a "$(NAME):$(VERSION)" -m "$(NAME) in version $(VERSION)"

publish:
	for i in "$(PWD)/rpmbuild/SOURCES/RPMS/*.rpm"; do \
		../upload-github-release-asset.sh github_api_token="$(TOKEN)" owner="utobi" repo="prometheus-rpm" tag="$(NAME):v$(VERSION)" filename="$i"; \
	done
clean:
	rm -rf "$(PWD)/rpmbuild/SOURCES/prometheus-$(VERSION).linux-amd64"
	rm -f "$(PWD)/rpmbuild/SOURCES/prometheus-$(VERSION).linux-amd64.tar.gz"
