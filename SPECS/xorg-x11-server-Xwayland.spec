%global commit 280aac5a0ee09c45b17ec4be0681397f7c34c12e
%global shortcommit %(c=%{commit}; echo ${c:0:7})

#global gitdate 20210201
%global pkgname %{?gitdate:xserver}%{!?gitdate:xwayland}

%global default_font_path "catalogue:/etc/X11/fontpath.d,built-ins"

Summary:   Xwayland
Name:      xorg-x11-server-Xwayland
Version:   21.1.3
Release:   7%{?gitdate:.%{gitdate}git%{shortcommit}}%{?dist}

URL:       http://www.x.org
%if 0%{?gitdate}
Source0:   https://gitlab.freedesktop.org/xorg/%{pkgname}/-/archive/%{commit}/%{pkgname}-%{shortcommit}.tar.gz
%else
Source0:   https://www.x.org/pub/individual/xserver/%{pkgname}-%{version}.tar.xz
%endif

Patch1: 0001-xwayland-eglstream-Demote-EGLstream-device-warning.patch
Patch2: 0002-xwayland-glamor-Change-errors-to-verbose-messages.patch
Patch3: 0003-xwayland-glamor-Log-backend-selected-for-debug.patch
Patch4: 0004-xwayland-eglstream-Prefer-EGLstream-if-available.patch

# CVE-2021-4011
Patch10001: 0001-record-Fix-out-of-bounds-access-in-SwapCreateRegiste.patch
# CVE-2021-4009
Patch10002: 0002-xfixes-Fix-out-of-bounds-access-in-ProcXFixesCreateP.patch
# CVE-2021-4010
Patch10003: 0003-Xext-Fix-out-of-bounds-access-in-SProcScreenSaverSus.patch
# CVE-2021-4008
Patch10004: 0004-render-Fix-out-of-bounds-access-in-SProcRenderCompos.patch
# CVE-2022-2319/ZDI-CAN-16062, CVE-2022-2320/ZDI-CAN-16070
Patch10005: 0001-xkb-switch-to-array-index-loops-to-moving-pointers.patch
Patch10006: 0002-xkb-swap-XkbSetDeviceInfo-and-XkbSetDeviceInfoCheck.patch
Patch10007: 0003-xkb-add-request-length-validation-for-XkbSetGeometry.patch
# CVE-2022-3550
Patch10008: 0001-xkb-proof-GetCountedString-against-request-length-at.patch
# CVE-2022-3551
Patch10009: 0001-xkb-fix-some-possible-memleaks-in-XkbGetKbdByName.patch
# CVE-2022-46340
Patch10010: 0001-Xtest-disallow-GenericEvents-in-XTestSwapFakeInput.patch
# related to CVE-2022-46344
Patch10011: 0002-Xi-return-an-error-from-XI-property-changes-if-verif.patch
# CVE-2022-46344
Patch10012: 0003-Xi-avoid-integer-truncation-in-length-check-of-ProcX.patch
# CVE-2022-46341
Patch10013: 0004-Xi-disallow-passive-grabs-with-a-detail-255.patch
# CVE-2022-46343
Patch10014: 0005-Xext-free-the-screen-saver-resource-when-replacing-i.patch
# CVE-2022-46342
Patch10015: 0006-Xext-free-the-XvRTVideoNotify-when-turning-off-from-.patch
# CVE-2022-46283
Patch10016: 0007-xkb-reset-the-radio_groups-pointer-to-NULL-after-fre.patch
# Follow-up to CVE-2022-46340
Patch10017: 0008-Xext-fix-invalid-event-type-mask-in-XTestSwapFakeInp.patch
# CVE-2023-0494
Patch10018: 0001-Xi-fix-potential-use-after-free-in-DeepCopyPointerCl.patch

License:   MIT

Requires: xorg-x11-server-common
Requires: libEGL

BuildRequires: gcc
BuildRequires: git-core
BuildRequires: meson

BuildRequires: wayland-devel
BuildRequires: pkgconfig(wayland-client) >= 1.3.0
BuildRequires: pkgconfig(wayland-protocols)
BuildRequires: pkgconfig(wayland-eglstream-protocols)

BuildRequires: pkgconfig(dmx)
BuildRequires: pkgconfig(epoxy)
BuildRequires: pkgconfig(fontenc)
BuildRequires: pkgconfig(libdrm) >= 2.4.0
BuildRequires: pkgconfig(libssl)
BuildRequires: pkgconfig(libtirpc)
BuildRequires: pkgconfig(pixman-1)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xau)
BuildRequires: pkgconfig(xdmcp)
BuildRequires: pkgconfig(xext)
BuildRequires: pkgconfig(xfixes)
BuildRequires: pkgconfig(xfont2)
BuildRequires: pkgconfig(xi)
BuildRequires: pkgconfig(xinerama)
BuildRequires: pkgconfig(xkbfile)
BuildRequires: pkgconfig(xmu)
BuildRequires: pkgconfig(xorg-macros) >= 1.17
BuildRequires: pkgconfig(xpm)
BuildRequires: pkgconfig(xrender)
BuildRequires: pkgconfig(xres)
BuildRequires: pkgconfig(xshmfence) >= 1.1
BuildRequires: pkgconfig(xtrans) >= 1.3.2
BuildRequires: pkgconfig(xtst)
BuildRequires: pkgconfig(xv)
BuildRequires: xorg-x11-proto-devel >= 7.7-10

BuildRequires: mesa-libGL-devel >= 9.2
BuildRequires: mesa-libEGL-devel
BuildRequires: mesa-libgbm-devel

BuildRequires: audit-libs-devel
BuildRequires: libselinux-devel >= 2.0.86-1

# libunwind is Exclusive for the following arches
%ifarch aarch64 %{arm} hppa ia64 mips ppc ppc64 %{ix86} x86_64
%if !0%{?rhel}
BuildRequires: libunwind-devel
%endif
%endif

BuildRequires: pkgconfig(xcb-aux)
BuildRequires: pkgconfig(xcb-image)
BuildRequires: pkgconfig(xcb-icccm)
BuildRequires: pkgconfig(xcb-keysyms)
BuildRequires: pkgconfig(xcb-renderutil)

%description
Xwayland is an X server for running X clients under Wayland.

%package devel
Summary: Development package
Requires: pkgconfig

%description devel
The development package provides the developmental files which are
necessary for developing Wayland compositors using Xwayland.

%prep
%autosetup -S git_am -n %{pkgname}-%{?gitdate:%{commit}}%{!?gitdate:%{version}}

%build
%meson \
        -Dxwayland_eglstream=true \
        -Ddefault_font_path=%{default_font_path} \
        -Dbuilder_string="Build ID: %{name} %{version}-%{release}" \
        -Dxkb_output_dir=%{_localstatedir}/lib/xkb \
        -Dxcsecurity=true \
        -Dglamor=true \
        -Ddri3=true

%meson_build

%install
%meson_install

# Remove unwanted files/dirs
rm $RPM_BUILD_ROOT%{_mandir}/man1/Xserver.1*
rm -Rf $RPM_BUILD_ROOT%{_libdir}/xorg
rm -Rf $RPM_BUILD_ROOT%{_includedir}/xorg
rm -Rf $RPM_BUILD_ROOT%{_datadir}/aclocal
rm -Rf $RPM_BUILD_ROOT%{_localstatedir}/lib/xkb

%files
%{_bindir}/Xwayland
%{_mandir}/man1/Xwayland.1*

%files devel
%{_libdir}/pkgconfig/xwayland.pc

%changelog
* Tue Feb  7 2023 Olivier Fourdan <ofourdan@redhat.com> - 21.1.3-7
- Fix CVE-2023-0494 (#2166974)

* Mon Dec 19 2022 Peter Hutterer <peter.hutterer@redhat.com> - 21.1.3-6
- Follow-up fix for CVE-2022-46340 (#2151778)

* Wed Dec 14 2022 Peter Hutterer <peter.hutterer@redhat.com> - 21.1.3-5
- CVE fix for: CVE-2022-4283 (#2151803), CVE-2022-46340 (#2151778),
  CVE-2022-46341 (#2151783), CVE-2022-46342 (#2151786),
  CVE-2022-46343 (#2151793), CVE-2022-46344 (#2151796)

* Mon Nov 14 2022 Olivier Fourdan <ofourdan@redhat.com> -  21.1.3-4
- Fix CVE-2022-3550, CVE-2022-3551
  Resolves: rhbz#2140769, rhbz#2140771

* Fri Jul 29 2022 Olivier Fourdan <ofourdan@redhat.com> - 21.1.3-3
- CVE fix for: CVE-2022-2319/ZDI-CAN-16062, CVE-2022-2320/ZDI-CAN-16070
  Resolves: rhbz#2110440, rhbz#2110433

* Fri Jan  7 2022 Olivier Fourdan <ofourdan@redhat.com> - 21.1.3-2
- CVE fix for: CVE-2021-4008 (#2038067), CVE-2021-4009 (#2038070),
  CVE-2021-4010 (#2038072), CVE-2021-4011 (#2038074)

* Thu Dec  2 2021 Olivier Fourdan <ofourdan@redhat.com> - 21.1.3-1
- Rebase to 21.1.3 (rhbz#2015839)
- Prefer EGLstream if both EGLstream and GBM are usable

* Tue Aug 10 2021 Mohan Boddu <mboddu@redhat.com> - 21.1.1-6
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Mon Aug  9 2021 Olivier Fourdan <ofourdan@redhat.com> - 21.1.1-5
- Backport the latest fixes from Xwayland for EGLstream (rhbz#1977742)

* Tue Jun 22 2021 Mohan Boddu <mboddu@redhat.com> - 21.1.1-4
- Rebuilt for RHEL 9 BETA for openssl 3.0
  Related: rhbz#1971065

* Mon Jun 21 2021 Olivier Fourdan <ofourdan@redhat.com> - 21.1.1-3
- Fix a use-after-free in the previous changes for GLX

* Thu Jun 17 2021 Olivier Fourdan <ofourdan@redhat.com> - 21.1.1-2
- Backport fixes for GLX and EGLstream (#1969486)

* Thu Jun 17 2021 Olivier Fourdan <ofourdan@redhat.com> - 21.1.1-1
- xwayland 21.1.1 (#1952897)

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 21.1.0-2
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Thu Mar  18 2021 Olivier Fourdan <ofourdan@redhat.com> - 21.1.0-1
- xwayland 21.1.0

* Thu Mar  4 2021 Olivier Fourdan <ofourdan@redhat.com> - 21.0.99.902-1
- xwayland 21.0.99.902
- Remove xdmcp, udev, udev_kms build options
- Stop overriding the vendor name, same as xorg-x11-server

* Thu Feb 18 2021 Olivier Fourdan <ofourdan@redhat.com> - 21.0.99.901-1
- xwayland 21.0.99.901

* Mon Feb  1 2021 Olivier Fourdan <ofourdan@redhat.com> - 1.20.99.1-0.1.20210201git5429791
- Initial import (#1912335).
