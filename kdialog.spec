%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	Utility to display KDE dialog boxes from shell scripts
Name:		kdialog
Version:	19.12.1
Release:	1
Epoch:		1
License:	LGPLv2+
Group:		Graphical desktop/KDE
Url:		http://utils.kde.org/projects/filelight/
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5KDELibs4Support)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	pkgconfig(Qt5DBus)
Conflicts:	kdialog < 1:17.04.0
Conflicts:	kde-baseapps < 1:17.04.0

%description
Utility to display KDE dialog boxes from shell scripts.
The syntax is very much inspired from the "dialog" command
(which shows text mode dialogs).

%files -f %{name}.lang
%{_bindir}/kdialog*
%{_datadir}/dbus-1/interfaces/org.kde.kdialog.ProgressDialog.xml
%{_datadir}/metainfo/org.kde.kdialog.metainfo.xml

#----------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang %{name}
