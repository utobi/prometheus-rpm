VERSION=0.7
PWD=$(shell pwd)

all: rpm clean

rpm:
	mkdir -p "$(PWD)/rpmbuild"
	mkdir -p "$(PWD)/rpmbuild/SOURCES/"
	mkdir -p "$(PWD)/rpmbuild/SOURCES/jmx_javaagent_exporter-$(VERSION)"
	mkdir -p "$(PWD)/rpmbuild/SOURCES/jmx_javaagent_exporter-$(VERSION)/configuration"
	cd "$(PWD)/rpmbuild/SOURCES/" && wget https://github.com/prometheus/jmx_exporter/archive/parent-$(VERSION).zip
	cd "$(PWD)/rpmbuild/SOURCES/" && unzip parent-$(VERSION).zip
	cd "$(PWD)/rpmbuild/SOURCES/jmx_exporter-parent-$(VERSION)/" && mvn clean package
	cd "$(PWD)/rpmbuild/SOURCES/jmx_exporter-parent-$(VERSION)/" && cp jmx_prometheus_javaagent/target/jmx_prometheus_javaagent-$(VERSION).jar ../jmx_javaagent_exporter-$(VERSION)/jmx_javaagent_exporter.jar
	cd "$(PWD)/rpmbuild/SOURCES/jmx_exporter-parent-$(VERSION)/" && cp example_configs/* ../jmx_javaagent_exporter-$(VERSION)/configuration
	cp -Rv contrib "$(PWD)/rpmbuild/SOURCES/jmx_javaagent_exporter-$(VERSION)"
	cd "$(PWD)/rpmbuild/SOURCES" && tar cvfz parent-$(VERSION).tar.gz jmx_javaagent_exporter-$(VERSION)
	rpmbuild --define '_topdir '"$(PWD)/rpmbuild" -ba --clean contrib/jmx_javaagent_exporter.spec

deploy:
	curl -v -F r=$(REPOSITORY) -F hasPom=false -F e=rpm -F g=$(GROUPID) -F a=jmx_javaagent_exporter -F v=$(VERSION) -F p=RPM -F file=@$(WORKSPACE)/prometheus-rpm/jmx_javaagent_exporter/rpmbuild/RPMS/x86_64/jmx_javaagent_exporter-$(VERSION)-1.el6.x86_64.rpm -u $(REPOSITORY_CREDENTIALS) $(REPOSITORY_URL)

clean:
	rm -rf "$(PWD)/rpmbuild/SOURCES/jmx_exporter-parent-$(VERSION)"
	rm "$(PWD)/rpmbuild/SOURCES/parent-$(VERSION).zip"
