%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	Utility to display KDE dialog boxes from shell scripts
Name:		plasma6-kdialog
Version:	24.01.90
Release:	1
License:	LGPLv2+
Group:		Graphical desktop/KDE
Url:		http://utils.kde.org/projects/filelight/
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/kdialog-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	pkgconfig(Qt6DBus)

%description
Utility to display KDE dialog boxes from shell scripts.
The syntax is very much inspired from the "dialog" command
(which shows text mode dialogs).

%files -f kdialog.lang
%{_bindir}/kdialog*
%{_datadir}/dbus-1/interfaces/org.kde.kdialog.ProgressDialog.xml
%{_datadir}/metainfo/org.kde.kdialog.metainfo.xml
%{_datadir}/applications/org.kde.kdialog.desktop

#----------------------------------------------------------------------

%prep
%autosetup -p1 -n kdialog-%{?git:master}%{!?git:%{version}}
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang kdialog
