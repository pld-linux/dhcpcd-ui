Summary:	Graphical interface to dhcpcd
Summary(pl.UTF-8):	Graficzny interfejs do dhcpcd
Name:		dhcpcd-ui
Version:	0.7.9
Release:	1
License:	BSD
Group:		Applications/Networking
#Source0Download: https://github.com/NetworkConfiguration/dhcpcd-ui/releases
Source0:	https://github.com/NetworkConfiguration/dhcpcd-ui/releases/download/v%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	e3b0b1506688c71742a65a76c740a0e0
URL:		https://roy.marples.name/projects/dhcpcd-ui
BuildRequires:	Qt5Core-devel >= 5
BuildRequires:	Qt5Gui-devel >= 5
BuildRequires:	Qt5Widgets-devel >= 5
BuildRequires:	dbus-devel
# gtk+3 also supported, but gtk+2 preferred
BuildRequires:	gtk+2-devel >= 2.0
BuildRequires:	libnotify-devel
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	ncurses-devel
BuildRequires:	pkgconfig
# for icons conversion
BuildRequires:	python3-cairosvg
BuildRequires:	qt5-build
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	dhcpcd >= 6.4.4
Suggests:	%{name}-desktop = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
dhcpcd-ui is the graphical interface to dhcpcd
(<http://roy.marples.name/projects/dhcpcd>). It has a helper library
in C to try and minimize any toolkit specific parts. There are GTK+
and Qt front ends (in separate packages).

dhcpcd-curses is very much a work in progress and is only informative
at this stage.

dhcpcd-online can report on network availability from dhcpcd.

%description -l pl.UTF-8
dhcpcd-ui to graficzny interfejs do dhcpcd
(<http://roy.marples.name/projects/dhcpcd>). Ma pomocniczą bibliotekę
w C, aby zminimalizować części specyficzne dla toolkitu. Są dostępne
frontendy GTK+ i Qt (w osobnych pakietach).

dhcpcd-curses jest w początkowej fazie rozwoju i obecnie jest tylko
informacyjny.

dhcpcd-inline potrafi informować o dostępności sieci z dhcpcd.

%package -n dhcpcd-gtk
Summary:	GTK+ frontend for network configuration
Summary(pl.UTF-8):	Frontend GTK+ do konfiguracji sieci
Group:		X11/Applications/Networking
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-desktop = %{version}-%{release}

%description -n dhcpcd-gtk
dhcpcd-gtk is a GTK+ frontend for network configuration. It uses
dhcpcd and wpa_supplicant as backends.

%description -n dhcpcd-gtk -l pl.UTF-8
dhcpcd-gtk to frontend GTK+ do konfiguracji sieci. Jako backendy
wykorzystuje dhcpcd i wpa_supplicant.

%package -n dhcpcd-qt
Summary:	Qt frontend for network configuration
Summary(pl.UTF-8):	Frontend Qt do konfiguracji sieci
Group:		X11/Applications/Networking
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-desktop = %{version}-%{release}

%description -n dhcpcd-qt
dhcpcd-qt is a Qt frontend for network configuration. It uses dhcpcd
and wpa_supplicant as backends.

%description -n dhcpcd-qt -l pl.UTF-8
dhcpcd-gtk to frontend Qt do konfiguracji sieci. Jako backendy
wykorzystuje dhcpcd i wpa_supplicant.

%prep
%setup -q

%build
# not autoconf configure, but mimits its behaviour, ignores unknown options
%configure \
	QTDIR=%{_libdir}/qt5 \
	--with-curses \
	--with-gtk \
	--with-icons \
	--with-qt \

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	INSTALL_ROOT=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md TODO
%attr(755,root,root) %{_bindir}/dhcpcd-curses
%attr(755,root,root) %{_bindir}/dhcpcd-online
%{_datadir}/dhcpcd
%{_iconsdir}/hicolor/*x*/apps/dhcpcd.png
%{_iconsdir}/hicolor/scalable/apps/dhcpcd.svg
%{_mandir}/man8/dhcpcd-curses.8*
%{_mandir}/man8/dhcpcd-online.8*

%files -n dhcpcd-gtk
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/dhcpcd-gtk
/etc/xdg/autostart/dhcpcd-gtk.desktop
%{_mandir}/man8/dhcpcd-gtk.8*

%files -n dhcpcd-qt
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/dhcpcd-qt
/etc/xdg/autostart/dhcpcd-qt.desktop
%{_mandir}/man8/dhcpcd-qt.8*
