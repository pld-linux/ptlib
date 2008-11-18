# TODO:
#	IPv6 support disabled ('NULL' undeclared)
#
Summary:	Portable Tools Library
Name:		ptlib
Version:	2.4.2
Release:	2
URL:		http://www.opalvoip.org/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/ptlib/2.4/%{name}-%{version}.tar.bz2
# Source0-md5:	47ba7da2a339643d5f5406215d457d5a
License:	MPLv1.0
Group:		Libraries
BuildRequires:	SDL-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	bison
BuildRequires:	esound-devel
BuildRequires:	expat-devel
BuildRequires:	flex
BuildRequires:	libstdc++-devel
#BuildRequires:	libavc1394-devel
#BuildRequires:	libdc1394-devel < 2.0.0
BuildRequires:	openssl-devel
BuildRequires:	openldap-devel
BuildRequires:	pkgconfig
BuildRequires:	unixODBC-devel
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

%package devel
Summary:	PTLib (Portable Tools Library) development files
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files and libraries for developing applications that use ptlib.


%package static
Summary:	PTLib (Portable Tools Library) static libraries
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
PTLib (Portable Tools Library) static libraries.

%package sound-alsa
Summary:	Alsa audio plugin
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-sound
Obsoletes:	pwlib-sound-alsa

%description sound-alsa
Alsa audio plugin.

%package sound-esd
Summary:	Esound audio plugin
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-sound

%description sound-esd
Esound audio plugin.

%package sound-oss
Summary:	OSS audio plugin
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-sound
Obsoletes:	pwlib-sound-oss

%description sound-oss
OSS audio plugin.

%package video-v4l
Summary:	v4l video input plugin
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description video-v4l
v4l video input plugin.

%package video-v4l2
Summary:	v4l2 video input plugin
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	pwlib-video-v4l2

%description video-v4l2
v4l2 video input plugin.

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
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/make
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}/make/%{name}-config
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
