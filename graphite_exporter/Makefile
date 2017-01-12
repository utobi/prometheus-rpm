VERSION=0.1.0
PWD=$(shell pwd)

all: rpm clean

rpm:
	mkdir -p "$(PWD)/rpmbuild"
	mkdir -p "$(PWD)/rpmbuild/SOURCES/"
	cd "$(PWD)/rpmbuild/SOURCES" && wget https://github.com/prometheus/graphite_exporter/releases/download/$(VERSION)/graphite_exporter-$(VERSION).linux-amd64.tar.gz
	cd "$(PWD)/rpmbuild/SOURCES" && mkdir -p "graphite_exporter-$(VERSION).linux-amd64" && tar xzvf *tar.gz -C "graphite_exporter-$(VERSION).linux-amd64"
	cp -Rv contrib "$(PWD)/rpmbuild/SOURCES/graphite_exporter-$(VERSION).linux-amd64"
	cd "$(PWD)/rpmbuild/SOURCES" && tar cvfz graphite_exporter-$(VERSION).linux-amd64.tar.gz graphite_exporter-$(VERSION).linux-amd64
	rpmbuild --define '_topdir '"$(PWD)/rpmbuild" -ba --clean contrib/graphite_exporter.spec

deploy:
	curl -v -F r=$(REPOSITORY) -F hasPom=false -F e=rpm -F g=$(GROUPID) -F a=prometheus-graphite-exporter -F v=$(VERSION) -F p=RPM -F file=@$(WORKSPACE)/graphite_exporter/rpmbuild/RPMS/x86_64/graphite-exporter-$(VERSION)-1.$(OS_NAME).x86_64.rpm -u $(REPOSITORY_CREDENTIALS) $(REPOSITORY_URL)

clean:
	rm -rf "$(PWD)/rpmbuild/SOURCES/graphite_exporter-$(VERSION)"
	rm -rf "$(PWD)/rpmbuild/SOURCES/graphite_exporter-$(VERSION).linux-amd64"
	rm -rf "$(PWD)/rpmbuild/SOURCES/graphite_exporter-$(VERSION).linux-amd64.tar.gz"
