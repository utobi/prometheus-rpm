%define debug_package %{nil}

Name:		mysqld-exporter-sysvinit
Version:	0.9.0
Release:	2%{?dist}
Summary:	Prometheus exporter for machine metrics, written in Go with pluggable metric collectors.
Group:		System Environment/Daemons
License:	See the LICENSE file at github.
URL:		https://github.com/prometheus/mysqld_exporter
Source0:        https://github.com/prometheus/mysqld_exporter/releases/download/v%{version}/mysqld_exporter-%{version}.linux-amd64.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
Requires(pre):  /usr/sbin/useradd
Requires:       daemonize
AutoReqProv:	No

%description

Prometheus exporter for MySQL server metrics.

%prep
%setup -q -n mysqld_exporter-%{version}.linux-amd64

%build
echo

%install
mkdir -vp $RPM_BUILD_ROOT/var/log/prometheus/
mkdir -vp $RPM_BUILD_ROOT/var/run/prometheus
mkdir -vp $RPM_BUILD_ROOT/var/lib/prometheus
mkdir -vp $RPM_BUILD_ROOT/usr/bin
mkdir -vp $RPM_BUILD_ROOT/etc/init.d
mkdir -vp $RPM_BUILD_ROOT/etc/sysconfig
install -m 755 mysqld_exporter-%{version}.linux-amd64/mysqld_exporter $RPM_BUILD_ROOT/usr/bin/mysqld_exporter
install -m 755 contrib/mysqld_exporter.init $RPM_BUILD_ROOT/etc/init.d/mysqld_exporter
install -m 644 contrib/mysqld_exporter.sysconfig $RPM_BUILD_ROOT/etc/sysconfig/mysqld_exporter

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
/usr/bin/mysqld_exporter
/etc/init.d/mysqld_exporter
%config(noreplace) /etc/sysconfig/mysqld_exporter
/var/run/prometheus
/var/log/prometheus
/var/lib/prometheus