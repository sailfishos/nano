Name:       nano
Summary:    A small text editor
Version:    2.2.6
Release:    1
Group:      Applications/Editors
License:    GPLv3
URL:        http://www.nano-editor.org
Patch0:     nano-2.2.4-notimestamp.patch
Patch1:     nano-2.2.6-tinfo.patch
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

# nano-2.2.4-notimestamp.patch
%patch0 -p1
# nano-2.2.6-tinfo.patch
%patch1 -p1

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
%doc AUTHORS BUGS COPYING ChangeLog INSTALL NEWS README THANKS TODO
%doc doc/nanorc.sample
%doc doc/faq.html
%{_bindir}/*
%doc %{_mandir}/man*/*
%lang(fr) %{_mandir}/fr/man*/*
%{_infodir}/nano.info.*
%{_datadir}/nano

