%bcond clang 1
%bcond wifi 0

# TDE variables
%define tde_epoch 2
%if "%{?tde_version}" == ""
%define tde_version 14.1.5
%endif
%define pkg_rel 2

%define tde_pkg knemo
%define tde_prefix /opt/trinity


%undefine __brp_remove_la_files
%define dont_remove_libtool_files 1
%define _disable_rebuild_configure 1

# fixes error: Empty %files file …/debugsourcefiles.list
%define _debugsource_template %{nil}

%define tarball_name %{tde_pkg}-trinity


Name:		trinity-%{tde_pkg}
Epoch:		%{tde_epoch}
Version:	0.4.8
Release:	%{?tde_version}_%{?!preversion:%{pkg_rel}}%{?preversion:0_%{preversion}}%{?dist}
Summary:	Network interfaces monitor for the Trinity systray
Group:		Applications/Utilities
URL:		http://www.trinitydesktop.org/
#URL:		http://beta.smileaf.org/projects

License:	GPLv2+


Source0:		https://mirror.ppa.trinitydesktop.org/trinity/releases/R%{tde_version}/main/applications/system/%{tarball_name}-%{tde_version}%{?preversion:~%{preversion}}.tar.xz

BuildSystem:    cmake

BuildOption:    -DCMAKE_BUILD_TYPE="RelWithDebInfo"
BuildOption:    -DCMAKE_INSTALL_PREFIX=%{tde_prefix}
BuildOption:    -DSHARE_INSTALL_PREFIX="%{tde_prefix}/share"
BuildOption:    -DWITH_ALL_OPTIONS=ON
BuildOption:    -DWITH_LIBIW=%{!?with_wifi:OFF}%{?with_wifi:ON}
BuildOption:    -DBUILD_ALL=ON
BuildOption:    -DBUILD_DOC=ON
BuildOption:    -DBUILD_TRANSLATIONS=ON
BuildOption:    -DWITH_GCC_VISIBILITY=%{!?with_clang:ON}%{?with_clang:OFF}

BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	desktop-file-utils

BuildRequires:	trinity-tde-cmake >= %{tde_version}

%{!?with_clang:BuildRequires:	gcc-c++}

BuildRequires:	pkgconfig
BuildRequires:	libtool

BuildRequires:	gettext

# ACL support
BuildRequires:  pkgconfig(libacl)

# IDN support
BuildRequires:	pkgconfig(libidn)

# OPENSSL support
BuildRequires:  pkgconfig(openssl)

# Wireless support
# Wifi support
# upstream uses libiw, which is deprecated

BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(sm)



%description
KNemo displays an icon in the systray for every network interface.
Tooltips and an info dialog provide further information about the
interface.  Passive popups inform about interface changes.
A traffic plotter is also integrated.

knemo polls the network interface status every second using the
ifconfig, route and iwconfig tools. 

Homepage: http://extragear.kde.org/apps/knemo/


%conf -p
unset QTDIR QTINC QTLIB
export PATH="%{tde_prefix}/bin:${PATH}"
export PKG_CONFIG_PATH="%{tde_prefix}/%{_lib}/pkgconfig"


%files
%defattr(-,root,root,-)
%{tde_prefix}/%{_lib}/trinity/kcm_knemo.la
%{tde_prefix}/%{_lib}/trinity/kcm_knemo.so
%{tde_prefix}/%{_lib}/trinity/kded_knemod.la
%{tde_prefix}/%{_lib}/trinity/kded_knemod.so
%{tde_prefix}/share/applications/tde/kcm_knemo.desktop
%{tde_prefix}/share/apps/knemo/
%{tde_prefix}/share/icons/crystalsvg/*/*/*.png
%{tde_prefix}/share/locale/*/LC_MESSAGES/knemod.mo
%{tde_prefix}/share/locale/*/LC_MESSAGES/kcm_knemo.mo
%{tde_prefix}/share/services/kded/knemod.desktop
%{tde_prefix}/share/doc/tde/HTML/en/kcontrol/knemo/

