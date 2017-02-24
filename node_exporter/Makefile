NAME="node_exporter"
VERSION?=$(shell cat VERSION)
TOKEN?="TODO: SET A TOKEN"
PWD=$(shell pwd)

all: rpm clean

rpm:
	mkdir -p "$(PWD)/rpmbuild"
	mkdir -p "$(PWD)/rpmbuild/SOURCES/"
	cd "$(PWD)/rpmbuild/SOURCES" && wget https://github.com/prometheus/$(NAME)/releases/download/v$(VERSION)/$(NAME)-$(VERSION).linux-amd64.tar.gz
	cd "$(PWD)/rpmbuild/SOURCES" && tar xzvf *tar.gz
	cp -Rv contrib "$(PWD)/rpmbuild/SOURCES/$(NAME)-$(VERSION).linux-amd64"
	cd "$(PWD)/rpmbuild/SOURCES" && tar cvfz $(NAME)-$(VERSION).linux-amd64.tar.gz $(NAME)-$(VERSION).linux-amd64
	rpmbuild --define "version $(VERSION)" --define '_topdir '"$(PWD)/rpmbuild" -ba --clean contrib/$(NAME).spec
	rpmbuild --with sysvinit --without systemd --define "version $(VERSION)" --define '_topdir '"$(PWD)/rpmbuild" -ba --clean contrib/$(NAME).spec

clean:
	rm -rf "$(PWD)/rpmbuild/SOURCES/$(NAME)-$(VERSION).linux-amd64"
	rm -f "$(PWD)/rpmbuild/SOURCES/$(NAME)-$(VERSION).linux-amd64.tar.gz"

### deploy to nexus
deploy:
	curl -v -F r=$(REPOSITORY) -F hasPom=false -F e=rpm -F g=$(GROUPID) -F a=$(NAME) -F v=$(VERSION) -F p=RPM -F file=@$(WORKSPACE)/$(NAME)/rpmbuild/RPMS/x86_64/$(NAME)-$(VERSION)-1.$(OS_NAME).x86_64.rpm -u $(REPOSITORY_CREDENTIALS) $(REPOSITORY_URL)
	curl -v -F r=$(REPOSITORY) -F hasPom=false -F e=rpm -F g=$(GROUPID) -F a=$(NAME).sysvinit -F v=$(VERSION) -F p=RPM -F file=@$(WORKSPACE)/$(NAME)/rpmbuild/RPMS/x86_64/$(NAME)-$(VERSION)-1.sysvinit.$(OS_NAME).x86_64.rpm -u $(REPOSITORY_CREDENTIALS) $(REPOSITORY_URL)

tag:
	git tag -a "$(NAME)_$(VERSION)" -m "$(NAME) in version $(VERSION)"

