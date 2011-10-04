# 
# Do not Edit! Generated by:
# spectacle version 0.15
# 
# >> macros
# << macros

Name:       nano
Summary:    A small text editor
Version:    2.2.4
Release:    3
Group:      Applications/Editors
License:    GPLv2+
URL:        http://www.nano-editor.org
Source0:    http://www.nano-editor.org/dist/v2.2/%{name}-%{version}.tar.gz
Source100:  nano.yaml
Requires(post): /sbin/install-info
Requires(postun): /sbin/install-info
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  autoconf
BuildRequires:  gettext-devel
BuildRequires:  groff

%description
GNU nano is a small and friendly text editor.



%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%configure --disable-static \
    --enable-all

make %{?jobs:-j%jobs}

# >> build post
# << build post
%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%make_install

# >> install post
rm -f %{buildroot}%{_infodir}/dir
mkdir -p ${RPM_BUILD_ROOT}%{_bindir}
# << install post
%find_lang nano



%post
%install_info --info-dir=%_infodir %{_infodir}/nano.info.*

%postun
if [ $1 = 0 ] ;then
%install_info_delete --info-dir=%{_infodir} %{_infodir}/nano.info.*
fi


%files -f nano.lang
%defattr(-,root,root,-)
# >> files
%doc AUTHORS BUGS COPYING ChangeLog INSTALL NEWS README THANKS TODO
%doc doc/nanorc.sample
%doc doc/faq.html
%{_bindir}/*
%doc %{_mandir}/man*/*
%lang(fr) %{_mandir}/fr/man*/*
%{_infodir}/nano.info.*
%{_datadir}/nano
# << files

