%define debug_package %{nil}

Name:		jmx_javaagent_exporter
Version:	0.7
Release:	1%{?dist}
Summary:	Prometheus jmx_exporter
Group:		System Environment/Daemons
License:	See the LICENSE file at github.
URL:		https://github.com/prometheus/jmx_exporter
Source0:	https://github.com/prometheus/jmx_exporter/releases/download/%{version}/parent-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
Requires(pre):  /usr/sbin/useradd
AutoReqProv:	No

%description

Prometheus JMX Exporter

%prep
%setup -q -n %{name}-%{version}

%build
echo

%install
mkdir -vp $RPM_BUILD_ROOT/usr/share/prometheus/
mkdir -vp $RPM_BUILD_ROOT/usr/share/prometheus/jmx_javaagent_exporter
mkdir -vp $RPM_BUILD_ROOT/etc/prometheus/jmx_javaagent_exporter
mkdir -vp $RPM_BUILD_ROOT/etc/prometheus/jmx_javaagent_exporter/examples

install -m 755 jmx_javaagent_exporter.jar $RPM_BUILD_ROOT/usr/share/prometheus/jmx_javaagent_exporter/jmx_javaagent_exporter.jar

install -m 644 configuration/cassandra.yml $RPM_BUILD_ROOT/etc/prometheus/jmx_javaagent_exporter/examples/cassandra.yml
install -m 644 configuration/kafka-pre0-8-2.yml $RPM_BUILD_ROOT/etc/prometheus/jmx_javaagent_exporter/examples/kafka-pre0-8-2.yml
install -m 644 configuration/kafka-0-8-2.yml $RPM_BUILD_ROOT/etc/prometheus/jmx_javaagent_exporter/examples/kafka-0-8-2.yml
install -m 644 configuration/tomcat.yml $RPM_BUILD_ROOT/etc/prometheus/jmx_javaagent_exporter/examples/tomcat.yml
install -m 644 configuration/zookeeper.yaml $RPM_BUILD_ROOT/etc/prometheus/jmx_javaagent_exporter/examples/zookeeper.yaml

%files
%defattr(-,root,root,-)
/usr/share/prometheus/jmx_javaagent_exporter/jmx_javaagent_exporter.jar
/etc/prometheus/jmx_javaagent_exporter/examples/cassandra.yml
/etc/prometheus/jmx_javaagent_exporter/examples/kafka-pre0-8-2.yml
/etc/prometheus/jmx_javaagent_exporter/examples/kafka-0-8-2.yml
/etc/prometheus/jmx_javaagent_exporter/examples/tomcat.yml
/etc/prometheus/jmx_javaagent_exporter/examples/zookeeper.yaml
