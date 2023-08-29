%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
#define git 20200916
#define commit cc1ac2452e41873741c8b5f3fcafa29ae3ce5a30

Name:		audiotube
Version:	23.08.0
Release:	%{?git:0.%{git}.}1
Summary:	YouTube Music client for Plasma Mobile
%if 0%{?git}
Source0:        https://invent.kde.org/plasma-mobile/%{name}/-/archive/master/%{name}-master.tar.bz2
%else
Source0:        http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
%endif
License:	GPLv3
Group:		Applications/Productivity
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5Concurrent)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Quick)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5QuickControls2)
BuildRequires:	cmake(Qt5Multimedia)
BuildRequires:	cmake(Qt5Sql)
BuildRequires:	cmake(Qt5Svg)
BuildRequires:	cmake(Qt5WebSockets)
BuildRequires:	cmake(KF5Kirigami2)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5Crash)
BuildRequires:	cmake(pybind11)
BuildRequires:	cmake(KF5KirigamiAddons)
BuildRequires:	cmake(FutureSQL5)
BuildRequires:	cmake(QCoro5)
BuildRequires:	python-devel
BuildRequires:	python%{pyver}dist(yt-dlp)
BuildRequires:	python%{pyver}dist(ytmusicapi)
Requires:	python%{pyver}dist(yt-dlp)

%description
YouTube Music client for Plasma Mobile

%prep
%autosetup -p1
%cmake_kde5 -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build
%find_lang audiotube

%files -f audiotube.lang
%{_bindir}/audiotube
%{_datadir}/applications/org.kde.audiotube.desktop
%{_datadir}/icons/hicolor/scalable/apps/org.kde.audiotube.svg
%{_datadir}/metainfo/org.kde.audiotube.appdata.xml
