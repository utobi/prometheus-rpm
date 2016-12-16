VERSION=0.12.0
PWD=$(shell pwd)
DIST=$(shell rpm --eval %dist)
OUTPUT_DIR=$(PWD)/output
MOCK=/usr/bin/mock

all: el6 el7

prepare: clean
	mkdir -p '$(OUTPUT_DIR)'
	mkdir -p '$(PWD)/rpmbuild/SOURCES/'
	cd '$(PWD)/rpmbuild/SOURCES' && curl --location --remote-name --silent --show-error  https://github.com/prometheus/node_exporter/releases/download/$(VERSION)/node_exporter-$(VERSION).linux-amd64.tar.gz
	cd '$(PWD)/rpmbuild/SOURCES' && mkdir node_exporter-$(VERSION).linux-amd64 && tar xzvf *tar.gz -C node_exporter-$(VERSION).linux-amd64
	cp -Rv contrib '$(PWD)/rpmbuild/SOURCES/node_exporter-$(VERSION).linux-amd64'
	cd '$(PWD)/rpmbuild/SOURCES' && tar cvfz node_exporter-$(VERSION).linux-amd64.tar.gz node_exporter-$(VERSION).linux-amd64

el6: prepare
	$(MOCK) --root epel-6-x86_64 --define '%dist .el6' --buildsrpm --spec contrib/node_exporter.spec --sources '$(PWD)/rpmbuild/SOURCES' --resultdir '$(OUTPUT_DIR)'
	$(MOCK) --root epel-6-x86_64 --define '%dist .el6' '$(OUTPUT_DIR)/node_exporter-$(VERSION)-1.el6.src.rpm' --resultdir '$(OUTPUT_DIR)'

el7: prepare
	$(MOCK) --root epel-7-x86_64 --define '%dist .el7' --buildsrpm --spec contrib/node_exporter.spec --sources '$(PWD)/rpmbuild/SOURCES' --resultdir '$(OUTPUT_DIR)'
	$(MOCK) --root epel-7-x86_64 --define '%dist .el7' '$(OUTPUT_DIR)/node_exporter-$(VERSION)-1.el7.src.rpm' --resultdir '$(OUTPUT_DIR)'

deploy:
	curl -v -F r=$(REPOSITORY) -F hasPom=false -F e=rpm -F g=$(GROUPID) -F a=prometheus-node-exporter.sysvinit -F v=$(VERSION) -F p=RPM -F file=@$(WORKSPACE)/prometheus-rpm/node_exporter/rpmbuild/RPMS/x86_64/node-exporter-sysvinit-$(VERSION)-1.el6.x86_64.rpm -u $(REPOSITORY_CREDENTIALS) $(REPOSITORY_URL)
	curl -v -F r=$(REPOSITORY) -F hasPom=false -F e=rpm -F g=$(GROUPID) -F a=prometheus-node-exporter.systemd -F v=$(VERSION) -F p=RPM -F file=@$(WORKSPACE)/prometheus-rpm/node_exporter/rpmbuild/RPMS/x86_64/node-exporter-systemd-$(VERSION)-1.el6.x86_64.rpm -u $(REPOSITORY_CREDENTIALS) $(REPOSITORY_URL)

clean:
	rm -rf '$(PWD)/rpmbuild/SOURCES'

