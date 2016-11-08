%define debug_package %{nil}

Name:		jmx_exporter_sysvinit
Version:	0.6
Release:	1%{?dist}
Summary:	Prometheus jmx_exporter
Group:		System Environment/Daemons
License:	See the LICENSE file at github.
URL:		https://github.com/prometheus/jmx_exporter
Source0:	https://github.com/prometheus/jmx_exporter/releases/download/%{version}/parent-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
Requires(pre):  /usr/sbin/useradd
Requires:       daemonize
AutoReqProv:	No

%description

Prometheus JMX Exporter

%prep
%setup -q -n jmx_exporter-%{version}

%build
echo

%install
mkdir -vp $RPM_BUILD_ROOT/var/log/prometheus/
mkdir -vp $RPM_BUILD_ROOT/var/run/prometheus
mkdir -vp $RPM_BUILD_ROOT/usr/share/prometheus/
mkdir -vp $RPM_BUILD_ROOT/usr/share/prometheus/jmx_exporter
mkdir -vp $RPM_BUILD_ROOT/var/lib/prometheus
mkdir -vp $RPM_BUILD_ROOT/usr/bin
mkdir -vp $RPM_BUILD_ROOT/etc/init.d
mkdir -vp $RPM_BUILD_ROOT/etc/prometheus/jmx_exporter
mkdir -vp $RPM_BUILD_ROOT/etc/prometheus/jmx_exporter/examples
mkdir -vp $RPM_BUILD_ROOT/etc/sysconfig

install -m 755 contrib/jmx_exporter.init $RPM_BUILD_ROOT/etc/init.d/jmx_exporter
install -m 644 contrib/jmx_exporter.sysconfig $RPM_BUILD_ROOT/etc/sysconfig/jmx_exporter
install -m 644 contrib/jmx_exporter.yaml $RPM_BUILD_ROOT/etc/prometheus/jmx_exporter/jmx_exporter.yaml
install -m 755 contrib/jmx_exporter $RPM_BUILD_ROOT/usr/bin/jmx_exporter

install -m 755 jmx_exporter.jar $RPM_BUILD_ROOT/usr/share/prometheus/jmx_exporter/jmx_exporter.jar

install -m 644 configuration/cassandra.yml $RPM_BUILD_ROOT/etc/prometheus/jmx_exporter/examples/cassandra.yml
install -m 644 configuration/kafka-pre0-8-2.yml $RPM_BUILD_ROOT/etc/prometheus/jmx_exporter/examples/kafka-pre0-8-2.yml
install -m 644 configuration/kafka-0-8-2.yml $RPM_BUILD_ROOT/etc/prometheus/jmx_exporter/examples/kafka-0-8-2.yml
install -m 644 configuration/tomcat.yml $RPM_BUILD_ROOT/etc/prometheus/jmx_exporter/examples/tomcat.yml


%clean

%pre
getent group prometheus >/dev/null || groupadd -r prometheus
getent passwd prometheus >/dev/null || \
  useradd -r -g prometheus -s /sbin/nologin \
    -d $RPM_BUILD_ROOT/var/lib/prometheus/ -c "prometheus Daemons" prometheus
exit 0

%post
chgrp prometheus /var/run/prometheus
chmod 774 /var/run/prometheus
chown prometheus:prometheus /var/log/prometheus
chmod 744 /var/log/prometheus

%files
%defattr(-,root,root,-)
/usr/bin/jmx_exporter
/usr/share/prometheus/jmx_exporter/jmx_exporter.jar
%config(noreplace) /etc/prometheus/jmx_exporter/jmx_exporter.yaml
/etc/init.d/jmx_exporter
%config(noreplace) /etc/sysconfig/jmx_exporter
/etc/prometheus/jmx_exporter/examples/cassandra.yml
/etc/prometheus/jmx_exporter/examples/kafka-pre0-8-2.yml
/etc/prometheus/jmx_exporter/examples/kafka-0-8-2.yml
/etc/prometheus/jmx_exporter/examples/tomcat.yml
