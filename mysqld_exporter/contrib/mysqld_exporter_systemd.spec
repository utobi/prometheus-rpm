%define debug_package %{nil}

Name:    mysqld-exporter-systemd
Version: 0.9.0
Release: 2%{?dist}
Summary: Prometheus exporter for MySQL server metrics.
License: ASL 2.0
URL:     https://github.com/prometheus/mysqld_exporter

Source0: https://github.com/prometheus/mysqld_exporter/releases/download/v%{version}/mysqld_exporter-%{version}.linux-amd64.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description

Prometheus exporter for MySQL server metrics.

%prep
%setup -q -n mysqld_exporter-%{version}.linux-amd64

%build
echo

%install
mkdir -vp $RPM_BUILD_ROOT/var/lib/prometheus
mkdir -vp $RPM_BUILD_ROOT/usr/bin
mkdir -vp $RPM_BUILD_ROOT/usr/lib/systemd/system
mkdir -vp $RPM_BUILD_ROOT/etc/sysconfig
install -m 755 mysqld_exporter-%{version}.linux-amd64/mysqld_exporter $RPM_BUILD_ROOT/usr/bin/mysqld_exporter
install -m 644 contrib/mysqld_exporter.service $RPM_BUILD_ROOT/usr/lib/systemd/system/mysqld_exporter.service
install -m 644 contrib/mysqld_exporter.sysconfig $RPM_BUILD_ROOT/etc/sysconfig/mysqld_exporter

%clean

%pre
getent group prometheus >/dev/null || groupadd -r prometheus
getent passwd prometheus >/dev/null || \
  useradd -r -g prometheus -d /var/lib/prometheus -s /sbin/nologin \
          -c "Prometheus services" prometheus
exit 0

%post
%systemd_post mysqld_exporter.service

%preun
%systemd_preun mysqld_exporter.service

%postun
%systemd_postun mysqld_exporter.service

%files
%defattr(-,root,root,-)
/usr/bin/mysqld_exporter
/usr/lib/systemd/system/mysqld_exporter.service
%config(noreplace) /etc/sysconfig/mysqld_exporter
%attr(755, prometheus, prometheus)/var/lib/prometheus