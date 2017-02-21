%define _unpackaged_files_terminate_build 0
%define debug_package %{nil}
%bcond_with sysvinit
%bcond_without systemd

Name:		prometheus
Version:	%{version}
%if %{with sysvinit}
Release:	1.sysvinit%{?dist}
%endif
%if %{with systemd}
Release:	1%{?dist}
%endif
Summary:	Prometheus is a systems and service monitoring system. It collects metrics from configured targets at given intervals, evaluates rule expressions, displays the results, and can trigger alerts if some condition is observed to be true.
Group:		System Environment/Daemons
License:	See the LICENSE file at github.
URL:		https://github.com/prometheus/prometheus
Source0:	https://github.com/prometheus/prometheus/releases/download/%{version}/prometheus-%{version}.linux-amd64.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
Requires(pre):  /usr/sbin/useradd
%if %{with sysvinit}
Requires:       daemonize
%endif
%if %{with systemd}
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
%endif
AutoReqProv:	No

%description

Prometheus is a systems and service monitoring system.
It collects metrics from configured targets at given intervals, evaluates
rule expressions, displays the results, and can trigger alerts if
some condition is observed to be true.

%prep
%setup -q -n prometheus-%{version}.linux-amd64

%build
echo

%install
mkdir -vp $RPM_BUILD_ROOT/var/log/prometheus/
mkdir -vp $RPM_BUILD_ROOT/var/run/prometheus
mkdir -vp $RPM_BUILD_ROOT/var/lib/prometheus
mkdir -vp $RPM_BUILD_ROOT/usr/bin
mkdir -vp $RPM_BUILD_ROOT/etc/prometheus
mkdir -vp $RPM_BUILD_ROOT/etc/sysconfig
mkdir -vp $RPM_BUILD_ROOT/usr/share/prometheus
mkdir -vp $RPM_BUILD_ROOT/usr/share/prometheus/consoles
mkdir -vp $RPM_BUILD_ROOT/usr/share/prometheus/console_libraries
%if %{with sysvinit}
mkdir -vp $RPM_BUILD_ROOT/etc/init.d
%endif
%if %{with systemd}
mkdir -vp $RPM_BUILD_ROOT/usr/lib/systemd/system
%endif


install -m 644 contrib/prometheus.rules $RPM_BUILD_ROOT/etc/prometheus/prometheus.rules
install -m 644 contrib/prometheus.sysconfig $RPM_BUILD_ROOT/etc/sysconfig/prometheus
install -m 644 contrib/prometheus.yaml $RPM_BUILD_ROOT/etc/prometheus/prometheus.yaml
install -m 755 prometheus $RPM_BUILD_ROOT/usr/bin/prometheus
install -m 755 promtool $RPM_BUILD_ROOT/usr/bin/promtool
%if %{with sysvinit}
install -m 755 contrib/prometheus.init $RPM_BUILD_ROOT/etc/init.d/prometheus
%endif
%if %{with systemd}
install -m 755 contrib/prometheus.service $RPM_BUILD_ROOT/usr/lib/systemd/system/prometheus.service
%endif

install -m 755 console_libraries/menu.lib $RPM_BUILD_ROOT/usr/share/prometheus/console_libraries
install -m 755 console_libraries/prom.lib $RPM_BUILD_ROOT/usr/share/prometheus/console_libraries
install -m 755 consoles/aws_elasticache.html $RPM_BUILD_ROOT/usr/share/prometheus/consoles
install -m 755 consoles/aws_elb.html $RPM_BUILD_ROOT/usr/share/prometheus/consoles
install -m 755 consoles/aws_redshift-cluster.html $RPM_BUILD_ROOT/usr/share/prometheus/consoles
install -m 755 consoles/aws_redshift.html $RPM_BUILD_ROOT/usr/share/prometheus/consoles
install -m 755 consoles/blackbox.html $RPM_BUILD_ROOT/usr/share/prometheus/consoles
install -m 755 consoles/cassandra.html $RPM_BUILD_ROOT/usr/share/prometheus/consoles
install -m 755 consoles/cloudwatch.html $RPM_BUILD_ROOT/usr/share/prometheus/consoles
install -m 755 consoles/haproxy-backend.html $RPM_BUILD_ROOT/usr/share/prometheus/consoles
install -m 755 consoles/haproxy-backends.html $RPM_BUILD_ROOT/usr/share/prometheus/consoles
install -m 755 consoles/haproxy-frontend.html $RPM_BUILD_ROOT/usr/share/prometheus/consoles
install -m 755 consoles/haproxy-frontends.html $RPM_BUILD_ROOT/usr/share/prometheus/consoles
install -m 755 consoles/haproxy.html $RPM_BUILD_ROOT/usr/share/prometheus/consoles
install -m 755 consoles/index.html.example $RPM_BUILD_ROOT/usr/share/prometheus/consoles
install -m 755 consoles/node-cpu.html $RPM_BUILD_ROOT/usr/share/prometheus/consoles
install -m 755 consoles/node-disk.html $RPM_BUILD_ROOT/usr/share/prometheus/consoles
install -m 755 consoles/node-overview.html $RPM_BUILD_ROOT/usr/share/prometheus/consoles
install -m 755 consoles/node.html $RPM_BUILD_ROOT/usr/share/prometheus/consoles
install -m 755 consoles/prometheus-overview.html $RPM_BUILD_ROOT/usr/share/prometheus/consoles
install -m 755 consoles/prometheus.html $RPM_BUILD_ROOT/usr/share/prometheus/consoles
install -m 755 consoles/snmp-overview.html $RPM_BUILD_ROOT/usr/share/prometheus/consoles
install -m 755 consoles/snmp.html $RPM_BUILD_ROOT/usr/share/prometheus/consoles

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
%if %{with systemd}
/usr/lib/systemd/system/prometheus.service
%endif

%files
%defattr(-,root,root,-)
%if %{with sysvinit}
/etc/init.d/prometheus
%endif
%if %{with systemd}
/usr/lib/systemd/system/prometheus.service
%endif
/usr/bin/prometheus
/usr/bin/promtool
%config(noreplace) /etc/prometheus/prometheus.yaml
%config(noreplace) /etc/prometheus/prometheus.rules
%config(noreplace) /etc/sysconfig/prometheus
/usr/share/prometheus/consoles/aws_elasticache.html
/usr/share/prometheus/consoles/aws_elb.html
/usr/share/prometheus/consoles/aws_redshift-cluster.html
/usr/share/prometheus/consoles/aws_redshift.html
/usr/share/prometheus/consoles/blackbox.html
/usr/share/prometheus/consoles/cassandra.html
/usr/share/prometheus/consoles/cloudwatch.html
/usr/share/prometheus/consoles/haproxy-backend.html
/usr/share/prometheus/consoles/haproxy-backends.html
/usr/share/prometheus/consoles/haproxy-frontend.html
/usr/share/prometheus/consoles/haproxy-frontends.html
/usr/share/prometheus/consoles/haproxy.html
/usr/share/prometheus/consoles/index.html.example
/usr/share/prometheus/consoles/node-cpu.html
/usr/share/prometheus/consoles/node-disk.html
/usr/share/prometheus/consoles/node-overview.html
/usr/share/prometheus/consoles/node.html
/usr/share/prometheus/consoles/prometheus-overview.html
/usr/share/prometheus/consoles/prometheus.html
/usr/share/prometheus/consoles/snmp-overview.html
/usr/share/prometheus/consoles/snmp.html
/usr/share/prometheus/console_libraries/prom.lib
/usr/share/prometheus/console_libraries/menu.lib
%attr(755, prometheus, prometheus)/var/lib/prometheus
/var/run/prometheus
/var/log/prometheus
