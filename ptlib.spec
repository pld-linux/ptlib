# TODO:
#	IPv6 support disabled ('NULL' undeclared)
#
Summary:	Portable Tools Library
Summary(pl.UTF-8):	Przenośna biblioteka narzędziowa
Name:		ptlib
Version:	2.6.5
Release:	6
URL:		http://www.opalvoip.org/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/ptlib/2.6/%{name}-%{version}.tar.bz2
# Source0-md5:	db7fd581b66998cd76d96f8b7c3f22a1
License:	MPLv1.0
Group:		Libraries
BuildRequires:	SDL-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	bison
BuildRequires:	esound-devel
BuildRequires:	expat-devel
BuildRequires:	flex
#BuildRequires:	libavc1394-devel
#BuildRequires:	libdc1394-devel < 2.0.0
BuildRequires:	libstdc++-devel
BuildRequires:	openldap-devel
BuildRequires:	openssl-devel
BuildRequires:	pkgconfig
BuildRequires:	unixODBC-devel
Provides:	pwlib = %{version}-%{release}
Obsoletes:	pwlib
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PTLib (Portable Tools Library) is a moderately large class library
that has it's genesis many years ago as PWLib (portable Windows
Library), a method to product applications to run on both Microsoft
Windows and Unix systems. It has also been ported to other systems
such as Mac OSX, VxWorks and other embedded systems.

It is supplied mainly to support the OPAL project, but that shouldn't
stop you from using it in whatever project you have in mind if you so
desire.

%description -l pl.UTF-8
PTLib (przenośna biblioteka narzędziowa) jest względnie dużą
biblioteką, która wywodzi się z PWLib (przenośna biblioteka Windows)
służącej do tworzenia aplikacji działających zarówno w systemach
Microsoft Windows jak i Unix. Została także przeniesiona na inne
systemy takie jak Mac OSX, VxWorks i inne wbudowane.

Zestaw ten powstał by wspierać projekt OPAL, to nie powinno jednak być
przeszkodą by móc go wykorzystać do innych celów jeśli tylko ktoś ma
na to ochotę.

%package devel
Summary:	PTLib (Portable Tools Library) development files
Summary(pl.UTF-8):	PTLib pliki deweloperskie
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Provides:	pwlib-devel = %{version}-%{release}
Obsoletes:	pwlib-devel


%description devel
Header files and libraries for developing applications that use ptlib.

%description devel -l pl.UTF-8
Pliki nagłówkowe i biblioteki dla aplikacji korzystających z ptlib.

%package static
Summary:	PTLib (Portable Tools Library) static libraries
Summary(pl.UTF-8):	Biblioteki statyczne PTLib
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Provides:	pwlib-static = %{version}-%{release}
Obsoletes:	pwlib-static


%description static
PTLib (Portable Tools Library) static libraries.

%description static -l pl.UTF-8
Biblioteki statyczne PTLib.

%package sound-alsa
Summary:	Alsa audio plugin
Summary(pl.UTF-8):	Alsa wtyczka audio
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-sound
Obsoletes:	pwlib-sound-alsa

%description sound-alsa
Alsa audio plugin.

%description sound-alsa -l pl.UTF-8
Alsa wtyczka audio.

%package sound-esd
Summary:	Esound audio plugin
Summary(pl.UTF-8):	Esound wtyczka audio
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-sound

%description sound-esd
Esound audio plugin.

%description sound-esd -l pl.UTF-8
Esound wtyczka audio.

%package sound-oss
Summary:	OSS audio plugin
Summary(pl.UTF-8): OSS wtyczka audio
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-sound
Obsoletes:	pwlib-sound-oss

%description sound-oss
OSS audio plugin.

%description sound-oss -l pl.UTF-8
OSS wtyczka audio.

%package video-v4l
Summary:	v4l video input plugin
Summary(pl.UTF-8):	v4l wejściowa wtyczka wideo
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description video-v4l
v4l video input plugin.

%description video-v4l -l pl.UTF-8
v4l wejściowa wtyczka wideo.

%package video-v4l2
Summary:	v4l2 video input plugin
Summary(pl.UTF-8): v4l2 wejściowa wtyczka wideo
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	pwlib-video-v4l2

%description video-v4l2
v4l2 video input plugin.

%description video-v4l2 -l pl.UTF-8
v4l2 wejściowa wtyczka wideo.

#%package video-avc
#Summary:	AVC 1394 video input plugin
#Group:		Libraries
#Requires:	%{name} = %{version}-%{release}
#
#%description video-avc
#AVC 1394 video input plugin.

%prep
%setup -q

%build
%configure \
		--prefix=%{_prefix} \
		--enable-alsa \
		--enable-static \
		--enable-opal \
		--enable-plugins \
		--enable-esd \
		--enable-oss \
		--enable-v4l2 \
		--enable-v4l \
		--enable-http \
		--enable-httpforms \
		--enable-httpsvc \
		--disable-avc \
		--disable-dc \
		--enable-debug
dir=$(pwd)
%{__make} %{?debug:debugshared}%{!?debug:optshared} \
	PTLIBMAKEDIR="$dir/make" \
	PTLIBDIR="$dir" \
	OPTCCFLAGS="%{rpmcflags} %{!?debug:-DNDEBUG}"\
	CXX="%{__cxx}"


%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_includedir}/%{name}}

dir=$(pwd)
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -d %{_libdir}/lib*.a $RPM_BUILD_ROOT%{_libdir}
cp version.h $RPM_BUILD_ROOT%{_includedir}/%{name}

ln -s ptlib $RPM_BUILD_ROOT%{_datadir}/pwlib

sed -i -e 's#PTLIBDIR=.*#PTLIBDIR=%{_datadir}/ptlib#g' $RPM_BUILD_ROOT%{_datadir}/ptlib/make/plugins.mak

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpt.so.*.*.*
%dir %{_libdir}/%{name}-%{version}
%dir %{_libdir}/%{name}-%{version}/devices
%dir %{_libdir}/%{name}-%{version}/devices/sound
%dir %{_libdir}/%{name}-%{version}/devices/videoinput


%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpt*.so
%{_datadir}/pwlib
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/make
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_datadir}/%{name}/make/%{name}-config
%{_includedir}/ptclib
%{_includedir}/ptlib
%{_includedir}/*.h
%{_datadir}/%{name}/make/*.mak
%{_pkgconfigdir}/%{name}.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files sound-alsa
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}-%{version}/devices/sound/alsa_pwplugin.so

%files sound-esd
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}-%{version}/devices/sound/esd_pwplugin.so

%files sound-oss
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}-%{version}/devices/sound/oss_pwplugin.so

%files video-v4l
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}-%{version}/devices/videoinput/v4l_pwplugin.so

%files video-v4l2
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}-%{version}/devices/videoinput/v4l2_pwplugin.so

#%files video-avc
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_libdir}/%{name}-%{version}/devices/videoinput/avc_pwplugin.so
