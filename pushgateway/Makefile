VERSION=0.3.0
PWD=$(shell pwd)

all: rpm clean

rpm:
	mkdir -p "$(PWD)/rpmbuild"
	mkdir -p "$(PWD)/rpmbuild/SOURCES/"
	mkdir -p "$(PWD)/rpmbuild/SOURCES/pushgateway-$(VERSION).linux-amd64"
	cd "$(PWD)/rpmbuild/SOURCES/pushgateway-$(VERSION).linux-amd64" && wget https://github.com/prometheus/pushgateway/releases/download/$(VERSION)/pushgateway-$(VERSION).linux-amd64.tar.gz
	cd "$(PWD)/rpmbuild/SOURCES/pushgateway-$(VERSION).linux-amd64" && tar xzvf *tar.gz
	cp -Rv contrib "$(PWD)/rpmbuild/SOURCES/pushgateway-$(VERSION).linux-amd64"
	cd "$(PWD)/rpmbuild/SOURCES" && tar cvfz pushgateway-$(VERSION).linux-amd64.tar.gz pushgateway-$(VERSION).linux-amd64
	rpmbuild --define '_topdir '"$(PWD)/rpmbuild" -ba --clean contrib/pushgateway.spec

deploy:
	curl -v -F r=$(REPOSITORY) -F hasPom=false -F e=rpm -F g=$(GROUPID) -F a=pushgateway -F v=$(VERSION) -F p=RPM -F file=@$(WORKSPACE)/pushgateway/rpmbuild/RPMS/x86_64/pushgateway-$(VERSION)-1.el6.x86_64.rpm -u $(REPOSITORY_CREDENTIALS) $(REPOSITORY_URL)

clean:
	rm -rf "$(PWD)/rpmbuild/SOURCES/pushgateway-$(VERSION).linux-amd64"
	rm -f "$(PWD)/rpmbuild/SOURCES/pushgateway-$(VERSION).linux-amd64.tar.gz"
