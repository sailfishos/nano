Name:       nano
Summary:    A small text editor
Version:    6.4
Release:    1
License:    GPLv3
URL:        http://www.nano-editor.org
Source0:    %{name}-%{version}.tar.bz2
Patch0:     0001-autogen-Do-not-fetch-sources-at-the-build-time.patch
Patch1:     0002-Build-with-older-makeinfo-that-doesn-t-support-c.patch
BuildRequires:  pkgconfig(ncursesw)
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gettext-devel
BuildRequires:  sed
BuildRequires:  texinfo

%description
GNU nano is a small and friendly text editor.

%package doc
Summary:   Documentation for %{name}
Requires:  %{name} = %{version}-%{release}
Requires(post): /sbin/install-info
Requires(postun): /sbin/install-info

%description doc
Man and info pages for %{name}.

%prep
%autosetup -p1 -n %{name}-%{version}/upstream

%build
./autogen.sh
%configure

%make_build

%install
%make_install

rm -f %{buildroot}%{_infodir}/dir
mkdir -p ${RPM_BUILD_ROOT}%{_bindir}
%find_lang nano

mkdir -p %{buildroot}%{_docdir}/%{name}-%{version}
	install -m0644 -t %{buildroot}%{_docdir}/%{name}-%{version} \
	        AUTHORS ChangeLog INSTALL NEWS README THANKS TODO

# Remove html doc files 
rm -rf %{buildroot}%{_docdir}/%{name}

%post doc
%install_info --info-dir=%_infodir %{_infodir}/nano.info.*

%postun doc
if [ $1 = 0 ] ;then
%install_info_delete --info-dir=%{_infodir} %{_infodir}/nano.info.*
fi

%files -f nano.lang
%defattr(-,root,root,-)
%license COPYING
%{_bindir}/*
%{_datadir}/%{name}

%files doc
%defattr(-,root,root,-)
%{_infodir}/%{name}.info.*
%{_mandir}/man*/*
%{_docdir}/%{name}-%{version}
