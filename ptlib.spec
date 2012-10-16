#
# WARNING:
#	stable Ekiga version (3.2.x) crashes with ptlib-2.10.0
#	(it works with ptlib from PTLIB_2_8 branch)
#	Recommended versions of ptlib and opal can be found at:
#		http://wiki.ekiga.org/index.php/Download_Ekiga_sources
#
# Conditional build:
%bcond_without	http		# Disable http support
%bcond_without	ipv6		# Disable ipv6 support
%bcond_without	odbc		# Disable ODBC support
%bcond_without	plugins		# Disable plugins support
%bcond_without	resolver	# Disable resolver support
%bcond_without	openssl		# Disable openssl support
%bcond_without	video		# Disable video support
#
Summary:	Portable Tools Library
Summary(pl.UTF-8):	Przenośna biblioteka narzędziowa
Name:		ptlib
Version:	2.10.8
Release:	2
Epoch:		1
URL:		http://www.opalvoip.org/
Source0:	http://downloads.sourceforge.net/opalvoip/%{name}-%{version}.tar.bz2
# Source0-md5:	ab753e3e0125415caa1861c6ae22623f
Patch0:		ptlib-2.10.8-svn-revision.patch
License:	MPLv1.0
Group:		Libraries
%{?with_video:BuildRequires:	SDL-devel}
%if %{with plugins}
BuildRequires:	alsa-lib-devel
BuildRequires:	libv4l-devel
BuildRequires:	pulseaudio-devel
%endif
BuildRequires:	bison
BuildRequires:	expat-devel
BuildRequires:	flex
#BuildRequires:	libavc1394-devel
#BuildRequires:	libdc1394-devel < 2.0.0
BuildRequires:	libstdc++-devel
%{?with_openssl:BuildRequires:	openssl-devel}
BuildRequires:	pkgconfig
%{?with_odbc:BuildRequires:	unixODBC-devel}
Obsoletes:	ptlib-sound-esd
Obsoletes:	ptlib-video-v4l
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
Requires:	%{name} = %{epoch}:%{version}-%{release}


%description devel
Header files and libraries for developing applications that use ptlib.

%description devel -l pl.UTF-8
Pliki nagłówkowe i biblioteki dla aplikacji korzystających z ptlib.

%package static
Summary:	PTLib (Portable Tools Library) static libraries
Summary(pl.UTF-8):	Biblioteki statyczne PTLib
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}


%description static
PTLib (Portable Tools Library) static libraries.

%description static -l pl.UTF-8
Biblioteki statyczne PTLib.

%package sound-alsa
Summary:	Alsa audio plugin
Summary(pl.UTF-8):	Alsa wtyczka audio
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	%{name}-sound

%description sound-alsa
Alsa audio plugin.

%description sound-alsa -l pl.UTF-8
Alsa wtyczka audio.

%package sound-pulse
Summary:	Pulse audio plugin
Summary(pl.UTF-8):	Pulse wtyczka audio
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	%{name}-sound

%description sound-pulse
Alsa audio plugin.

%description sound-pulse -l pl.UTF-8
Alsa wtyczka audio.

%package sound-oss
Summary:	OSS audio plugin
Summary(pl.UTF-8):	OSS wtyczka audio
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	%{name}-sound

%description sound-oss
OSS audio plugin.

%description sound-oss -l pl.UTF-8
OSS wtyczka audio.

%package video-v4l2
Summary:	v4l2 video input plugin
Summary(pl.UTF-8):	v4l2 wejściowa wtyczka wideo
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description video-v4l2
v4l2 video input plugin.

%description video-v4l2 -l pl.UTF-8
v4l2 wejściowa wtyczka wideo.

%package video-avc
Summary: AVC 1394 video input plugin
Group: Libraries
Requires: %{name} = %{epoch}:%{version}-%{release}

%description video-avc
AVC 1394 video input plugin.

%prep
%setup -q
%patch0 -p1

%build
# note: --enable-opal influences most of the remaining enable/disable defaults
%configure \
		--prefix=%{_prefix} \
		--enable-opal \
%if %{with plugins}
		--enable-plugins \
		--enable-alsa \
		--enable-oss \
		--enable-v4l2 \
%else
		--disable-plugins \
		--disable-alsa \
		--disable-oss \
		--disable-v4l2 \
%endif
		--disable-v4l \
		--disable-esd \
%if %{with http}
		--enable-http \
		--enable-httpforms \
		--enable-httpsvc \
%else
		--disable-http \
		--disable-httpforms \
		--disable-httpsvc \
%endif
		--%{?with_ipv6:en}%{!?with_ipv6:dis}able-ipv6 \
		--%{?with_odbc:en}%{!?with_odbc:dis}able-odbc \
		--%{?with_resolver:en}%{!?with_resolver:dis}able-resolver \
		--%{?with_openssl:en}%{!?with_openssl:dis}able-openssl \
		--%{?with_video:en}%{!?with_video:dis}able-video \
		--disable-avc \
		--disable-dc \
		--enable-debug


dir=$(pwd)
%{__make} %{?debug:debugshared}%{!?debug:optshared} \
	V=1 \
	PTLIBMAKEDIR="$dir/make" \
	PTLIBDIR="$dir" \
	CFLAGS="%{rpmcflags} %{!?debug:-DNDEBUG} -DUSE_GCC" \
	LDFLAGS="%{rpmcflags} %{rpmldflags} %{!?debug:-DNDEBUG}" \
	CXX="%{__cxx}"


%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_includedir}/%{name}}

dir=$(pwd)
%{__make} install \
	V=1 \
	DESTDIR=$RPM_BUILD_ROOT

cp version.h $RPM_BUILD_ROOT%{_includedir}/%{name}

sed -i -e 's#PTLIBDIR=.*#PTLIBDIR=%{_datadir}/ptlib#g' $RPM_BUILD_ROOT%{_datadir}/ptlib/make/plugins.mak

chmod a+x $RPM_BUILD_ROOT%{_libdir}/lib*.so.*
find $RPM_BUILD_ROOT%{_libdir}/ptlib-* -name '*.so' | xargs chmod a+x

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpt.so.*.*.*
%if %{with plugins}
%dir %{_libdir}/%{name}-%{version}
%dir %{_libdir}/%{name}-%{version}/devices
%dir %{_libdir}/%{name}-%{version}/devices/sound
%dir %{_libdir}/%{name}-%{version}/devices/videoinput
%endif

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpt*.so
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

%if %{with plugins}
%files sound-alsa
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}-%{version}/devices/sound/alsa_pwplugin.so

%files sound-pulse
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}-%{version}/devices/sound/pulse_pwplugin.so

%files sound-oss
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}-%{version}/devices/sound/oss_pwplugin.so

%files video-v4l2
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}-%{version}/devices/videoinput/v4l2_pwplugin.so

%if 0
%files video-avc
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}-%{version}/devices/videoinput/avc_pwplugin.so
%endif
%endif
