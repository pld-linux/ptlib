#
# WARNING: keep compatible with Ekiga releases.
#	Recommended versions of ptlib and opal can be found at:
#	http://wiki.ekiga.org/index.php/Download_Ekiga_sources
#	(for Ekiga 4.0.x it's ptlib 3.10.x + opal 3.10.x)
# TODO: lua support (needs patching or some lua version packaged as default)
#
# Conditional build:
%bcond_without	http		# HTTP support
%bcond_without	ipv6		# IPv6 support
%bcond_without	ldap		# LDAP support
%bcond_without	lua		# Lua support
%bcond_without	odbc		# ODBC support
%bcond_without	openssl		# openssl support
%bcond_without	plugins		# plugins support
%bcond_without	resolver	# resolver support
%bcond_without	video		# video support
%bcond_with	esd		# EsounD audio support (obsolete)
%bcond_with	avc1394		# AVC1394 video input plugin [requires old libraw1394]
%bcond_with	dc1394		# DC1394 video input plugin [requires old libdc1394]
#
Summary:	Portable Tools Library
Summary(pl.UTF-8):	Przenośna biblioteka narzędziowa
Name:		ptlib
Version:	2.10.11
Release:	1
Epoch:		1
License:	MPL v1.0
Group:		Libraries
Source0:	http://downloads.sourceforge.net/opalvoip/%{name}-%{version}.tar.bz2
# Source0-md5:	eb2fb52c91224483c17dcea6df9c23a3
Patch0:		bison3.patch
Patch1:		%{name}-lua.patch
URL:		http://www.opalvoip.org/
%{?with_video:BuildRequires:	SDL-devel}
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	cyrus-sasl-devel
%{?with_esd:BuildRequires:	esound-devel}
BuildRequires:	expat-devel
BuildRequires:	flex
%{?with_avc1394:BuildRequires:	libavc1394-devel}
%{?with_dc1394:BuildRequires:	libdc1394-devel < 2.0.0}
BuildRequires:	libstdc++-devel
%{?with_lua:BuildRequires:	lua52-devel >= 5.2}
%{?with_ldap:BuildRequires:	openldap-devel}
%{?with_openssl:BuildRequires:	openssl-devel}
BuildRequires:	pkgconfig
%{?with_odbc:BuildRequires:	unixODBC-devel}
%if %{with plugins}
BuildRequires:	alsa-lib-devel
BuildRequires:	libv4l-devel
BuildRequires:	pulseaudio-devel
%endif
%{!?with_esd:Obsoletes:	ptlib-sound-esd}
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
Summary:	ALSA audio plugin for PTLib
Summary(pl.UTF-8):	Wtyczka dźwięku ALSA dla biblioteki PTLib
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	%{name}-sound

%description sound-alsa
ALSA audio plugin for PTLib.

%description sound-alsa -l pl.UTF-8
Wtyczka dźwięku ALSA dla biblioteki PTLib.

%package sound-esd
Summary:	EsounD audio plugin for PTLib
Summary(pl.UTF-8):	Wtyczka dźwięku EsounD dla biblioteki PTLib
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	%{name}-sound

%description sound-esd
EsounD audio plugin for PTLib.

%description sound-esd -l pl.UTF-8
Wtyczka dźwięku EsounD dla biblioteki PTLib.

%package sound-oss
Summary:	OSS audio plugin for PTLib
Summary(pl.UTF-8):	Wtyczka dźwięku OSS dla biblioteki PTLib
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	%{name}-sound

%description sound-oss
OSS audio plugin for PTLib.

%description sound-oss -l pl.UTF-8
Wtyczka dźwięku OSS dla biblioteki PTLib.

%package sound-pulse
Summary:	Pulse audio plugin for PTLib
Summary(pl.UTF-8):	Wtyczka dźwięku Pulse dla biblioteki PTLib
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	%{name}-sound

%description sound-pulse
Pulse audio plugin for PTLib.

%description sound-pulse -l pl.UTF-8
Wtyczka dźwięku Pulse dla biblioteki PTLib.

%package video-v4l2
Summary:	v4l2 video input plugin for PTLib
Summary(pl.UTF-8):	Wtyczka wejścia obrazu v4l2 dla biblioteki PTLib
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description video-v4l2
v4l2 video input plugin for PTLib.

%description video-v4l2 -l pl.UTF-8
Wtyczka wejścia obrazu v4l2 dla biblioteki PTLib.

%package video-avc
Summary:	AVC 1394 video input plugin for PTLib
Summary(pl.UTF-8):	Wtyczka wejścia obrazu AVC 1394 dla biblioteki PTLib
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description video-avc
AVC 1394 video input plugin for PTLib.

%description video-avc -l pl.UTF-8
Wtyczka wejścia obrazu AVC 1394 dla biblioteki PTLib

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__aclocal}
%{__autoconf}
# note: --enable-opal influences most of the remaining enable/disable defaults
%{?with_lua:CPPFLAGS="%{rpmcppflags} -I/usr/include/lua5.2"}
%configure \
	--disable-v4l \
%if %{with plugins}
	--enable-plugins \
	--enable-alsa \
	--enable-avc%{!?with_avc1394:=no} \
	--enable-dc%{!?with_dc1394:=no} \
	--enable-esd%{!?with_esd:=no} \
	--enable-lua%{!?with_lua:=no} \
	--enable-oss \
	--enable-v4l2 \
%else
	--disable-plugins \
	--disable-alsa \
	--disable-avc \
	--disable-dc \
	--disable-esd \
	--disable-oss \
	--disable-v4l2 \
%endif
%if %{with http}
	--enable-http \
	--enable-httpforms \
	--enable-httpsvc \
%else
	--disable-http \
	--disable-httpforms \
	--disable-httpsvc \
%endif
	--enable-ipv6%{!?with_ipv6:=no} \
	--enable-odbc%{!?with_odbc:=no} \
	--enable-openldap%{!?with_ldap:=no} \
	--enable-openssl%{!?with_openssl:=no} \
	--enable-resolver%{!?with_resolver:=no} \
	--enable-sasl%{!?with_sasl:=no} \
	--enable-video%{!?with_video:=no}

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

%{__make} install \
	V=1 \
	DESTDIR=$RPM_BUILD_ROOT

cp version.h $RPM_BUILD_ROOT%{_includedir}/%{name}

sed -i -e 's#PTLIBDIR=.*#PTLIBDIR=%{_datadir}/ptlib#g' $RPM_BUILD_ROOT%{_datadir}/ptlib/make/plugins.mak

chmod a+x $RPM_BUILD_ROOT%{_libdir}/lib*.so.*
find $RPM_BUILD_ROOT%{_libdir}/ptlib-* -name '*.so' | xargs chmod a+x

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

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
%attr(755,root,root) %{_bindir}/ptlib-config
%attr(755,root,root) %{_libdir}/libpt.so
%{_includedir}/ptclib
%{_includedir}/ptlib
%{_includedir}/ptbuildopts.h
%{_includedir}/ptlib.h
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/make
%attr(755,root,root) %{_datadir}/%{name}/make/%{name}-config
%{_datadir}/%{name}/make/*.mak
%{_pkgconfigdir}/ptlib.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libpt_s.a

%if %{with plugins}
%files sound-alsa
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}-%{version}/devices/sound/alsa_pwplugin.so

%if %{with esd}
%files sound-esd
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}-%{version}/devices/sound/esd_pwplugin.so
%endif

%files sound-oss
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}-%{version}/devices/sound/oss_pwplugin.so

%files sound-pulse
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}-%{version}/devices/sound/pulse_pwplugin.so

%files video-v4l2
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}-%{version}/devices/videoinput/v4l2_pwplugin.so

%if %{with avc1394}
%files video-avc
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}-%{version}/devices/videoinput/avc_pwplugin.so
%endif
%endif
