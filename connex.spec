Name:           connex
Version:        1.3.0
Release:        1
Summary:        Modern Wi-Fi Manager for Hyprland with GTK3 interface
License:        MIT
URL:            https://github.com/Lluciocc/connex

Source0:        https://github.com/Lluciocc/connex/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  python
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  python-gobject3
BuildRequires:  networkmanager

Requires:       python
Requires:       python-gobject3
Requires:       gtk+3
Requires:       networkmanager
Requires:       lib64appindicator
Requires:       libnotify

# lets not pull it. It should be supplements
#Recommends:     papirus-icon-theme
#Recommends:     hyprland

BuildArch:      noarch

%description
Connex is a modern Wi-Fi manager for Hyprland and GTK-based desktops.
Provides tray icon, UI dialogs and utilities for managing Wi-Fi
connections using NetworkManager.

%prep
%autosetup -n %{name}-%{version}

%build
# No build step required (Python application)

%install
install -Dm755 connex.py %{buildroot}/usr/bin/connex

# Assets
install -Dm644 assets/core/speedtest.py %{buildroot}/%{_libdir}/%{name}/assets/core/speedtest.py
install -Dm644 assets/tray/system_tray.py %{buildroot}/%{_libdir}/%{name}/assets/tray/system_tray.py
install -Dm644 assets/utils/debug.py %{buildroot}/%{_libdir}/%{name}/assets/utils/debug.py
install -Dm644 assets/ui/dialogs.py %{buildroot}/%{_libdir}/%{name}/assets/ui/dialogs.py
install -Dm644 assets/ui/main_window.py %{buildroot}/%{_libdir}/%{name}/assets/ui/main_window.py
install -Dm644 assets/core/proxies.py %{buildroot}/%{_libdir}/%{name}/assets/core/proxies.py

# Desktop entry
install -Dm644 connex.desktop %{buildroot}/usr/share/applications/connex.desktop

# Icon
install -Dm644 connex.svg %{buildroot}/usr/share/icons/hicolor/scalable/apps/connex.svg

# Autostart
install -Dm644 connex-tray.desktop %{buildroot}/etc/xdg/autostart/connex-tray.desktop

# License & docs
install -Dm644 LICENSE %{buildroot}/usr/share/licenses/%{name}/LICENSE
install -Dm644 README.md %{buildroot}/usr/share/doc/%{name}/README.md

%files
%license usr/share/licenses/%{name}/LICENSE
%doc usr/share/doc/%{name}/README.md
%{_bindir}/connex
%{_libdir}/connex/assets/
%{_datadir}/applications/connex.desktop
%{_datadir}/icons/hicolor/scalable/apps/connex.svg
%{_sysconfdir}/xdg/autostart/connex-tray.desktop
