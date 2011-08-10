Summary:	Desktop notification and configuration for dhcpcd
Name:		dhcpcd-ui
Version:	0.5.2
Release:	1
License:	BSD
Group:		Libraries
Source0:	http://roy.marples.name/downloads/dhcpcd/%{name}-%{version}.tar.bz2
# Source0-md5:	bb9996c139524510f77f96d029ae5cfc
URL:		http://roy.marples.name/projects/dhcpcd-ui/wiki
BuildRequires:	dbus-devel
BuildRequires:	gtk+2-devel
BuildRequires:	libnotify-devel
BuildRequires:	pkgconfig
Requires:	dhcpcd-dbus
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
dhcpcd-ui is a GTK+ monitor and configuration GUI for dhcpcd. It uses
dhcpcd-dbus to actually talk to dhcpcd and wpa_supplicant.

dhcpcd-ui sits in the notification area, it's icon representing the
overall network state. When attempting to negotiate an address you get
a nice animation. A notification bubble is also shown per interface
state change.

A drop down menu shows available Access Points, which one your
connected to, if they're encrypted or not and their overall quality.
You can click on one to configure the PSK or WEP key 0 for it.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/dhcpcd-gtk
%{_datadir}/gnome/autostart/dhcpcd-gtk.desktop
%{_datadir}/dhcpcd
%{_mandir}/man8/dhcpcd-gtk.8*
