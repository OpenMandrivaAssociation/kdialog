#define git 20240217
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	Utility to display KDE dialog boxes from shell scripts
Name:		kdialog
Version:	25.12.1
Release:	%{?git:0.%{git}.}1
License:	LGPLv2+
Group:		Graphical desktop/KDE
Url:		https://utils.kde.org/projects/filelight/
%if 0%{?git:1}
Source0:	https://invent.kde.org/utilities/kdialog/-/archive/%{gitbranch}/kdialog-%{gitbranchd}.tar.bz2#/kdialog-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/kdialog-%{version}.tar.xz
%endif
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KF6TextWidgets)
BuildRequires:	cmake(KF6Notifications)
BuildRequires:	pkgconfig(Qt6DBus)

%rename plasma6-kdialog

BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%description
Utility to display KDE dialog boxes from shell scripts.
The syntax is very much inspired from the "dialog" command
(which shows text mode dialogs).

%files -f %{name}.lang
%{_bindir}/kdialog*
%{_datadir}/dbus-1/interfaces/org.kde.kdialog.ProgressDialog.xml
%{_datadir}/metainfo/org.kde.kdialog.metainfo.xml
%{_datadir}/applications/org.kde.kdialog.desktop
