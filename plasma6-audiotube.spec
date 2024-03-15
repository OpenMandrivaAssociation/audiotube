%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
#define git 20240218
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
#define commit cc1ac2462e41873741c8b6f3fcafa29ae3ce6a30

Name:		plasma6-audiotube
Version:	24.02.0
Release:	%{?git:0.%{git}.}2
Summary:	YouTube Music client for Plasma Mobile
%if 0%{?git}
Source0:        https://invent.kde.org/multimedia/audiotube/-/archive/%{gitbranch}/audiotube-%{gitbranchd}.tar.bz2
%else
Source0:        https://download.kde.org/%{stable}/release-service/%{version}/src/audiotube-%{version}.tar.xz
%endif
License:	GPLv3
Group:		Applications/Productivity
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Concurrent)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6QuickControls2)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6QmlCore)
BuildRequires: cmake(Qt6QmlNetwork)
BuildRequires:	cmake(Qt6Multimedia)
BuildRequires:	cmake(Qt6Sql)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(Qt6WebSockets)
BuildRequires:	cmake(KF6Kirigami2)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6Crash)
BuildRequires:	cmake(pybind11)
BuildRequires:	cmake(KF6KirigamiAddons)
BuildRequires:	cmake(KF6WindowSystem)
BuildRequires:	cmake(FutureSQL6)
BuildRequires:	cmake(QCoro6)
BuildRequires: qt6-qtbase-theme-gtk3
BuildRequires: qt6-qtmultimedia-gstreamer
BuildRequires:	qt6-qtbase-sql-postgresql
BuildRequires: qt6-qtbase-sql-odbc
BuildRequires: qt6-qtbase-sql-mariadb
BuildRequires: qt6-qtbase-sql-firebird
BuildRequires:	python-devel
BuildRequires:	python%{pyver}dist(yt-dlp)
BuildRequires:	python%{pyver}dist(ytmusicapi)
Requires:	python%{pyver}dist(yt-dlp)

%description
YouTube Music client for Plasma Mobile

%prep
%autosetup -p1 -n audiotube-%{?git:%{gitbranchd}}%{!?git:%{version}}
%cmake \
	-DQT_MAJOR_VERSION=6 \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

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
