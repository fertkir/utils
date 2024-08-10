%global commit 8d1ca28b6f62c5858a65cd525c0997b1ebe2b1b8

Name:           keepassxc-unlocker
Version:        0.1.0
Release:        1%{?dist}
Summary:        Auto-unlocker for KeePassXC

License:        GPLv3+
URL:            https://github.com/fertkir/utils/tree/main/keepassxc-unlocker
Source0:        https://github.com/fertkir/utils/archive/%{commit}/util.tar.gz

Requires:       libsecret
Requires:       procps-ng
Requires:       dbus-tools

%description
Takes passwords from system keyring using libsecret and unlocks kdbx databases by listening and sending D-Bus messages.

%prep
%setup -q

%build


%install
install -Dm755 ./keepassxc-unlocker/keepassxc-unlocker %{_bindir}/keepassxc-unlocker


%files
%license ./LICENSE
%doc ./keepassxc-unlocker/README.md



%changelog
* Sat Aug 10 2024 Kirill Fertikov <kirill.fertikov@gmail.com>
- 
