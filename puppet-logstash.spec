%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:                   puppet-logstash
Version:                0.6.4
Release:                1%{?dist}
Summary:                Module for managing and configuring Logstash
License:                Apache-2.0

URL:                    https://github.com/elastic/puppet-logstash

Source0:                https://github.com/elastic/puppet-logstash/archive/%{version}.tar.gz

BuildArch:              noarch

Requires:               puppet-stdlib
Requires:               puppet-lib-file_concat

Requires:               puppet >= 2.7.0

%description
Module for managing and configuring Logstash

%prep
%setup -q -n %{name}-%{upstream_version}

find . -type f -name ".*" -exec rm {} +
find . -size 0 -exec rm {} +
find . \( -name "*.pl" -o -name "*.sh"  \) -exec chmod +x {} +
find . \( -name "*.pp" -o -name "*.py"  \) -exec chmod -x {} +
find . \( -name "*.rb" -o -name "*.erb" \) -exec chmod -x {} +
find . \( -name spec -o -name ext \) | xargs rm -rf

%build


%install
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/logstash/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/logstash/



%files
%{_datadir}/openstack-puppet/modules/logstash/


%changelog
