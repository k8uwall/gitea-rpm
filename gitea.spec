%define debug_package %{nil}
%define __spec_install_post /usr/lib/rpm/brp-compress || :

Name:			gitea
Summary:	Git with a cup of tea, painless self-hosted git service
Version:	1.6.2
Release:	20181222git2631f7f%{?dist}
License:	MIT
URL:			https://github.com/go-gitea/gitea
Group:		System/Servers
Source0:	https://github.com/go-gitea/gitea/releases/download/v%{version}/gitea-%{version}-linux-amd64
Source1:	%{name}.service
Source2:	%{name}.sysconf

%{?systemd_requires}
Requires(pre): shadow-utils

%description

Git with a cup of tea, painless self-hosted git service

%prep
%setup -T -c
pwd
cp -a %{SOURCE0} gitea
cp -a %{SOURCE1} %{name}.service
cp -a %{SOURCE2} %{name}.sysconf

%build
/bin/true

%install
install -D -m 755 %{name}         %{buildroot}%{_bindir}/%{name}
install -D -m 644 %{name}.service %{buildroot}%{_unitdir}/%{name}.service
install -D -m 644 %{name}.sysconf %{buildroot}%{_sysconfdir}/sysconfig/%{name}

%pre
getent group git >/dev/null || groupadd -r git
getent passwd git >/dev/null || \
  useradd -r -m -g git -d /home/git -s /sbin/nologin \
          -c "git clone systemAccount" git
exit 0

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun %{name}.service

%files
%defattr(-,root,root,-)
%{_bindir}/%{name}
%{_unitdir}/%{name}.service
%config(noreplace) %attr(755, git, git) %{_sysconfdir}/sysconfig/%{name}

%changelog
* Mon Dec 24 2018 k8uwall <k8uwall@example.com>
- Version bumpto v1.6.2

