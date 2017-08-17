# spec file for package nodejs-nodejs-through
%{?scl:%scl_package nodejs-nodejs-through}
%{!?scl:%global pkg_name %{name}}

%global npm_name through
%{?nodejs_find_provides_and_requires}

%global enable_tests 0

Name:		%{?scl_prefix}nodejs-through
Version:	2.3.8
Release:	4%{?dist}
Summary:	simplified stream construction
Url:		https://github.com/dominictarr/through
Source0:	https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
License:	MIT and ASL 2.0

BuildArch:	noarch
ExclusiveArch:	%{nodejs_arches} noarch

BuildRequires:	%{?scl_prefix}nodejs-devel
#BuildRequires:	nodejs-packaging

%if 0%{?enable_tests}
BuildRequires:	npm(from)
BuildRequires:	npm(stream-spec)
BuildRequires:	npm(tape)
%endif

%description
simplified stream construction

%prep
%setup -q -n package

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}

cp -pr package.json index.js \
	%{buildroot}%{nodejs_sitelib}/%{npm_name}

%{nodejs_symlink_deps}

%if 0%{?enable_tests}
%check
%{nodejs_symlink_deps} --check
set -e; for t in test/*.js; do node $t; done
%endif

%files
%{nodejs_sitelib}/through

%doc readme.markdown
%license LICENSE.APACHE2 LICENSE.MIT

%changelog
* Mon Jul 03 2017 Zuzana Svetlikova <zsvetlik@redhat.com> - 2.3.8-4
- rh-nodejs8 rebuild

* Tue Jun 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 2.3.8-3
- Resolves: #1334856, add ASL 2.0

* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 2.3.8-2
- rebuilt

* Wed Jul 29 2015 Zuzana Svetlikova <zsvetlik@redhat.com> - 2.3.8-1
- Initial build
