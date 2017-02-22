%define _unpackaged_files_terminate_build 0
%define debug_package %{nil}

Name:			jmx_exporter_agent
Version:		%{version}
Release:		1%{?dist}
Summary:		Prometheus jmx_exporter java agent
Group:			System Environment/Daemons
License:		See the LICENSE file at github.
URL:			https://github.com/prometheus/jmx_exporter
Source0:		https://github.com/prometheus/jmx_exporter/releases/download/%{version}/parent-%{version}.tar.gz
BuildRoot:		%{_tmppath}/%{name}-%{version}-root
AutoReqProv:		No

%description

Prometheus JMX Exporter Java Agent

%prep
%setup -q -n jmx_exporter-%{version}

%build
echo

%install
mkdir -vp $RPM_BUILD_ROOT/usr/share/prometheus/jmx_exporter
mkdir -vp $RPM_BUILD_ROOT/usr/share/prometheus/jmx_exporter/examples

install -m 644 contrib/jmx_exporter.yaml $RPM_BUILD_ROOT/usr/share/prometheus/jmx_exporter/examples/jmx_exporter.yaml
install -m 755 jmx_javaagent_exporter.jar $RPM_BUILD_ROOT/usr/share/prometheus/jmx_exporter/jmx_javaagent_exporter.jar
install -m 644 configuration/cassandra.yml $RPM_BUILD_ROOT/usr/share/prometheus/jmx_exporter/examples/cassandra.yml
install -m 644 configuration/kafka-pre0-8-2.yml $RPM_BUILD_ROOT/usr/share/prometheus/jmx_exporter/examples/kafka-pre0-8-2.yml
install -m 644 configuration/kafka-0-8-2.yml $RPM_BUILD_ROOT/usr/share/prometheus/jmx_exporter/examples/kafka-0-8-2.yml 
install -m 644 configuration/tomcat.yml $RPM_BUILD_ROOT/usr/share/prometheus/jmx_exporter/examples/tomcat.yml

%clean

%files
%defattr(-,root,root,-)
/usr/share/prometheus/jmx_exporter/jmx_javaagent_exporter.jar
/usr/share/prometheus/jmx_exporter/examples/cassandra.yml
/usr/share/prometheus/jmx_exporter/examples/kafka-pre0-8-2.yml
/usr/share/prometheus/jmx_exporter/examples/kafka-0-8-2.yml
/usr/share/prometheus/jmx_exporter/examples/tomcat.yml
