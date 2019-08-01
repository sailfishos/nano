Name:       nano
Summary:    A small text editor
Version:    2.8.5
Release:    1
Group:      Applications/Editors
License:    GPLv3
URL:        http://www.nano-editor.org
Source0:    %{name}-%{version}.tar.bz2
Patch0:     0001-autogen-Do-not-fetch-sources-at-the-build-time.patch
Requires(post): /sbin/install-info
Requires(postun): /sbin/install-info
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  autoconf
BuildRequires:  gettext-devel
BuildRequires:  groff
BuildRequires:  sed
BuildRequires:  texinfo

%description
GNU nano is a small and friendly text editor.

%prep
%setup -q -n %{name}-%{version}/upstream
%patch0 -p1

%build
./autogen.sh
%configure

make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install

rm -f %{buildroot}%{_infodir}/dir
mkdir -p ${RPM_BUILD_ROOT}%{_bindir}
%find_lang nano

%post
%install_info --info-dir=%_infodir %{_infodir}/nano.info.*

%postun
if [ $1 = 0 ] ;then
%install_info_delete --info-dir=%{_infodir} %{_infodir}/nano.info.*
fi

%files -f nano.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README THANKS TODO
%doc doc/faq.html
%{_bindir}/*
%doc %{_mandir}/man*/*
%{_infodir}/nano.info.*
%{_datadir}/nano

