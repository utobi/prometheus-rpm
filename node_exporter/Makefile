VERSION=0.12.0
PWD=$(shell pwd)

all: rpm clean

rpm:
	mkdir -p "$(PWD)/rpmbuild"
	mkdir -p "$(PWD)/rpmbuild/SOURCES/"
	cd "$(PWD)/rpmbuild/SOURCES" && wget https://github.com/prometheus/node_exporter/releases/download/$(VERSION)/node_exporter-$(VERSION).linux-amd64.tar.gz
	cd "$(PWD)/rpmbuild/SOURCES" && mkdir "node_exporter-$(VERSION).linux-amd64" && tar xzvf *tar.gz -C "node_exporter-$(VERSION).linux-amd64"
	cp -Rv contrib "$(PWD)/rpmbuild/SOURCES/node_exporter-$(VERSION).linux-amd64"
	cd "$(PWD)/rpmbuild/SOURCES" && tar cvfz node_exporter-$(VERSION).linux-amd64.tar.gz node_exporter-$(VERSION).linux-amd64
	rpmbuild --define '_topdir '"$(PWD)/rpmbuild" -ba --clean contrib/node_exporter.spec

deploy:
	curl -v -F r=$(REPOSITORY) -F hasPom=false -F e=rpm -F g=$(GROUPID) -F a=prometheus-node-exporter -F v=$(VERSION) -F p=RPM -F file=@$(WORKSPACE)/prometheus-rpm/node_exporter/rpmbuild/RPMS/x86_64/node-exporter-$(VERSION)-1.el6.x86_64.rpm -u $(REPOSITORY_CREDENTIALS) $(REPOSITORY_URL)
clean:
	rm -rf "$(PWD)/rpmbuild/SOURCES/prometheus-node-exporter-$(VERSION)"
	rm -rf "$(PWD)/rpmbuild/SOURCES/prometheus-node-exporter-$(VERSION).linux-amd64.tar.gz"
