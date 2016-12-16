%define debug_package %{nil}

Name:		node_exporter
Version:	0.12.0
Release:	1%{?dist}
Summary:	Prometheus exporter for machine metrics, written in Go with pluggable metric collectors.
Group:		System Environment/Daemons
License:	See the LICENSE file at github.
URL:		https://github.com/prometheus/node_exporter
Source0:        https://github.com/prometheus/node_exporter/releases/download/%{version}/node_exporter-%{version}.linux-amd64.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
Requires(pre):  /usr/sbin/useradd
%if (0%{?fedora} > 0 && 0%{?fedora} < 18) || (0%{?rhel} > 0 && 0%{?rhel} < 7)
Requires:       daemonize
%endif

AutoReqProv:	No

%description

Prometheus exporter for machine metrics, written in Go with pluggable metric collectors.

%prep
%setup -q -n node_exporter-%{version}.linux-amd64

%build
echo

%install
%if (0%{?fedora} > 0 && 0%{?fedora} < 18) || (0%{?rhel} > 0 && 0%{?rhel} < 7)
mkdir -vp $RPM_BUILD_ROOT/etc/init.d
install -m 755 contrib/node_exporter.init $RPM_BUILD_ROOT/etc/init.d/node_exporter
mkdir -vp $RPM_BUILD_ROOT/var/log/prometheus/
%else
mkdir -vp $RPM_BUILD_ROOT/usr/lib/systemd/system
install -m 755 contrib/node_exporter.service $RPM_BUILD_ROOT/usr/lib/systemd/system/node_exporter.service
mkdir -vp $RPM_BUILD_ROOT/opt/prometheus
%endif
mkdir -vp $RPM_BUILD_ROOT/etc/sysconfig
mkdir -vp $RPM_BUILD_ROOT/usr/bin
mkdir -vp $RPM_BUILD_ROOT/var/lib/prometheus
mkdir -vp $RPM_BUILD_ROOT/var/run/prometheus
install -m 755 node_exporter-%{version}.linux-amd64/node_exporter $RPM_BUILD_ROOT/usr/bin/node_exporter
install -m 644 contrib/node_exporter.sysconfig $RPM_BUILD_ROOT/etc/sysconfig/node_exporter

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
%if (0%{?fedora} > 0 && 0%{?fedora} < 18) || (0%{?rhel} > 0 && 0%{?rhel} < 7)
chown prometheus:prometheus /var/log/prometheus
chmod 744 /var/log/prometheus
%else
chown prometheus:prometheus /opt/prometheus
chmod 744 /opt/prometheus
%endif

%files
%defattr(-,root,root,-)
/usr/bin/node_exporter
%config(noreplace) /etc/sysconfig/node_exporter
/var/run/prometheus
%if (0%{?fedora} > 0 && 0%{?fedora} < 18) || (0%{?rhel} > 0 && 0%{?rhel} < 7)
/etc/init.d/node_exporter
/var/log/prometheus
%else
/usr/lib/systemd/system/node_exporter.service
/opt/prometheus
%endif
