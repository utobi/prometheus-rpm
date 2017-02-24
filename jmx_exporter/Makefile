NAME="jmx_exporter"
VERSION?=$(shell cat VERSION)
TOKEN?="TODO: SET A TOKEN"
PWD=$(shell pwd)

all: rpm clean

rpm:
	mkdir -p "$(PWD)/rpmbuild"
	mkdir -p "$(PWD)/rpmbuild/SOURCES/"
	mkdir -p "$(PWD)/rpmbuild/SOURCES/jmx_exporter-$(VERSION)"
	mkdir -p "$(PWD)/rpmbuild/SOURCES/jmx_exporter-$(VERSION)/configuration"
	cd "$(PWD)/rpmbuild/SOURCES/" && wget https://github.com/prometheus/jmx_exporter/archive/parent-$(VERSION).zip
	cd "$(PWD)/rpmbuild/SOURCES/" && unzip -o parent-$(VERSION).zip
	cd "$(PWD)/rpmbuild/SOURCES/jmx_exporter-parent-$(VERSION)/" && mvn clean package
	cd "$(PWD)/rpmbuild/SOURCES/jmx_exporter-parent-$(VERSION)/" && cp jmx_prometheus_httpserver/target/jmx_prometheus_httpserver-$(VERSION)-jar-with-dependencies.jar ../jmx_exporter-$(VERSION)/jmx_exporter.jar
	cd "$(PWD)/rpmbuild/SOURCES/jmx_exporter-parent-$(VERSION)/" && cp jmx_prometheus_javaagent/target/jmx_prometheus_javaagent-$(VERSION).jar ../jmx_exporter-$(VERSION)/jmx_javaagent_exporter.jar
	cd "$(PWD)/rpmbuild/SOURCES/jmx_exporter-parent-$(VERSION)/" && cp example_configs/* ../jmx_exporter-$(VERSION)/configuration
	cp -Rv contrib "$(PWD)/rpmbuild/SOURCES/jmx_exporter-$(VERSION)"
	cd "$(PWD)/rpmbuild/SOURCES" && tar cvfz parent-$(VERSION).tar.gz jmx_exporter-$(VERSION)
	rpmbuild  --define "version $(VERSION)" --define '_topdir '"$(PWD)/rpmbuild" -ba --clean contrib/jmx_exporter.spec
	rpmbuild  --define "version $(VERSION)" --define '_topdir '"$(PWD)/rpmbuild" -ba --clean contrib/jmx_exporter_agent.spec

clean:
	rm -rf "$(PWD)/rpmbuild/SOURCES/jmx_exporter-$(VERSION)"
	rm "$(PWD)/rpmbuild/SOURCES/parent-$(VERSION).zip"

### deploy to nexus
deploy:
	curl -v -F r=$(REPOSITORY) -F hasPom=false -F e=rpm -F g=$(GROUPID) -F a=$(NAME) -F v=$(VERSION) -F p=RPM -F file=@$(WORKSPACE)/$(NAME)/rpmbuild/RPMS/x86_64/$(NAME)-$(VERSION)-1.$(OS_NAME).x86_64.rpm -u $(REPOSITORY_CREDENTIALS) $(REPOSITORY_URL)
	curl -v -F r=$(REPOSITORY) -F hasPom=false -F e=rpm -F g=$(GROUPID) -F a=$(NAME).sysvinit -F v=$(VERSION) -F p=RPM -F file=@$(WORKSPACE)/$(NAME)/rpmbuild/RPMS/x86_64/$(NAME)-$(VERSION)-1.sysvinit.$(OS_NAME).x86_64.rpm -u $(REPOSITORY_CREDENTIALS) $(REPOSITORY_URL)

tag:
	git tag -a "v$(VERSION)__$(NAME)" -m "$(NAME) in version $(VERSION)"

