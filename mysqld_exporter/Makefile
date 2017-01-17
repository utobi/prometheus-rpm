VERSION=0.9.0
PWD=$(shell pwd)

all: rpm clean

rpm:
	mkdir -p "$(PWD)/rpmbuild"
	mkdir -p "$(PWD)/rpmbuild/SOURCES/"
	cd "$(PWD)/rpmbuild/SOURCES" && wget https://github.com/prometheus/mysqld_exporter/releases/download/v$(VERSION)/mysqld_exporter-$(VERSION).linux-amd64.tar.gz
	cd "$(PWD)/rpmbuild/SOURCES" && mkdir -p "mysqld_exporter-$(VERSION).linux-amd64" && tar xzvf *tar.gz -C "mysqld_exporter-$(VERSION).linux-amd64"
	cp -Rv contrib "$(PWD)/rpmbuild/SOURCES/mysqld_exporter-$(VERSION).linux-amd64"
	cd "$(PWD)/rpmbuild/SOURCES" && tar cvfz mysqld_exporter-$(VERSION).linux-amd64.tar.gz mysqld_exporter-$(VERSION).linux-amd64
	rpmbuild --define '_topdir '"$(PWD)/rpmbuild" -ba --clean contrib/mysqld_exporter_sysvinit.spec
	rpmbuild --define '_topdir '"$(PWD)/rpmbuild" -ba --clean contrib/mysqld_exporter_systemd.spec

deploy:
	curl -v -F r=$(REPOSITORY) -F hasPom=false -F e=rpm -F g=$(GROUPID) -F a=prometheus-mysqld-exporter.sysvinit -F v=$(VERSION) -F p=RPM -F file=@$(WORKSPACE)/mysqld_exporter/rpmbuild/RPMS/x86_64/mysqld-exporter-sysvinit-$(VERSION)-1.$(OS_NAME).x86_64.rpm -u $(REPOSITORY_CREDENTIALS) $(REPOSITORY_URL)
	curl -v -F r=$(REPOSITORY) -F hasPom=false -F e=rpm -F g=$(GROUPID) -F a=prometheus-mysqld-exporter.systemd -F v=$(VERSION) -F p=RPM -F file=@$(WORKSPACE)/mysqld_exporter/rpmbuild/RPMS/x86_64/mysqld-exporter-systemd-$(VERSION)-1.$(OS_NAME).x86_64.rpm -u $(REPOSITORY_CREDENTIALS) $(REPOSITORY_URL)

clean:
	rm -rf "$(PWD)/rpmbuild/SOURCES/prometheus-mysqld-exporter-$(VERSION)"
	rm -rf "$(PWD)/rpmbuild/SOURCES/prometheus-mysqld-exporter-$(VERSION).linux-amd64.tar.gz"
