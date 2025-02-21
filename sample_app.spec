Name: sample_app
Version: %{version}
Release: 1%{?dist}
Summary: Sample application for RPM packaging
License: MIT
Source0: sample_app-%{version}.tar.gz
Requires: coreutils
BuildArch: noarch

%description
This is a simple application that uses sleep.

%prep
%setup -q

%build
echo "Building application..."

%install
mkdir -p %{buildroot}/usr/local/bin
cp sample.sh %{buildroot}/usr/local/bin/sample

%files
/usr/local/bin/myapp

%changelog
* Tue Feb 19 2025 John Doe <john@example.com> - %{version}-1
- Initial package with sleep requirement
