VERSION=0.4.2
PWD=$(shell pwd)

all: rpm clean

rpm:
	mkdir -p "$(PWD)/rpmbuild"
	mkdir -p "$(PWD)/rpmbuild/SOURCES/"
	cd "$(PWD)/rpmbuild/SOURCES" && wget https://github.com/prometheus/alertmanager/releases/download/v$(VERSION)/alertmanager-$(VERSION).linux-amd64.tar.gz
	cd "$(PWD)/rpmbuild/SOURCES" && tar xzvf *tar.gz
	cp -Rv contrib "$(PWD)/rpmbuild/SOURCES/alertmanager-$(VERSION).linux-amd64"
	cd "$(PWD)/rpmbuild/SOURCES" && tar cvfz alertmanager-$(VERSION).linux-amd64.tar.gz alertmanager-$(VERSION).linux-amd64
	rpmbuild --define '_topdir '"$(PWD)/rpmbuild" -ba --clean contrib/alertmanager.spec

deploy:
	curl -v -F r=$(REPOSITORY) -F hasPom=false -F e=rpm -F g=$(GROUPID) -F a=alertmanager -F v=$(VERSION) -F p=RPM -F file=@$(WORKSPACE)/alertmanager/rpmbuild/RPMS/x86_64/alertmanager-$(VERSION)-1.$(OS_NAME).x86_64.rpm -u $(REPOSITORY_CREDENTIALS) $(REPOSITORY_URL)

clean:
	rm -rf "$(PWD)/rpmbuild/SOURCES/alertmanager-$(VERSION).linux-amd64"
	rm -f "$(PWD)/rpmbuild/SOURCES/alertmanager-$(VERSION).linux-amd64.tar.gz"
