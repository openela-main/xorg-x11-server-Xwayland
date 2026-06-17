%global commit 280aac5a0ee09c45b17ec4be0681397f7c34c12e
%global shortcommit %(c=%{commit}; echo ${c:0:7})

#global gitdate 20210201
%global pkgname %{?gitdate:xserver}%{!?gitdate:xwayland}

%global default_font_path "catalogue:/etc/X11/fontpath.d,built-ins"

Summary:   Xwayland
Name:      xorg-x11-server-Xwayland
Version:   24.1.9
Release:   4%{?gitdate:.%{gitdate}git%{shortcommit}}%{?dist}.2

URL:       http://www.x.org
%if 0%{?gitdate}
Source0:   https://gitlab.freedesktop.org/xorg/%{pkgname}/-/archive/%{commit}/%{pkgname}-%{shortcommit}.tar.gz
%else
Source0:   https://www.x.org/pub/individual/xserver/%{pkgname}-%{version}.tar.xz
%endif

# https://gitlab.freedesktop.org/xorg/xserver/-/work_items/1885
Patch:     0001-xwayland-Handle-GetCurrentClient-returning-NULL-in-x.patch
# CVE-2026-33999: XKB Integer Underflow in XkbSetCompatMap()
Patch:     0001-xkb-fix-buffer-re-use-in-_XkbSetCompatMap.patch
# CVE-2026-34000: XKB Out-of-bounds Read in CheckSetGeom()
Patch:     0002-xkb-Fix-bounds-check-in-_CheckSetGeom.patch
# CVE-2026-34001: XSYNC Use-after-free in miSyncTriggerFence()
Patch:     0003-miext-sync-Fix-use-after-free-in-miSyncTriggerFence.patch
# CVE-2026-34002: XKB Out-of-bounds read in CheckModifierMap()
Patch:     0004-xkb-Fix-out-of-bounds-read-in-CheckModifierMap.patch
# CVE-2026-34003: XKB Buffer overflow in CheckKeyTypes()
Patch:     0005-xkb-Add-additional-bound-checking-in-CheckKeyTypes.patch
Patch:     0006-xkb-Add-more-_XkbCheckRequestBounds.patch
# ZDI-CAN-30159 - CVE-2026-50257 - XSYNC Use-After-Free in miSyncDestroyFence()
# ZDI-CAN-30163 - CVE-2026-50260 - XSYNC Use-After-Free in FreeCounter()
Patch:     0001-sync-fix-deletion-of-counters-and-fences.patch
# ZDI-CAN-30164 - CVE-2026-50261 - XSYNC Use-After-Free in SyncChangeCounter()
Patch:     0002-sync-restart-trigger-list-iteration-in-SyncChangeCou.patch
# ZDI-CAN-30160 - CVE-2026-50258 - XKB Key Types Stack-based Buffer Overflow
Patch:     0003-xkb-reject-key-types-with-num_levels-exceeding-XkbMa.patch
# ZDI-CAN-30161 - CVE-2026-50259 - XKB SetMap Request Stack-based Buffer Overflow
Patch:     0004-xkb-clamp-nMaps-to-mapWidths-buffer-size-in-CheckKey.patch
# ZDI-CAN-30165 - CVE-2026-50262 - GLX ChangeDrawableAttributes Out-Of-Bounds Read/Write
Patch:     0005-glx-fix-reversed-length-check-in-ChangeDrawableAttri.patch
# ZDI-CAN-30168 - CVE-2026-50263 - CreateSaverWindow Use-After-Free Information Disclosure
Patch:     0006-saver-re-fetch-screen-private-after-CheckScreenPriva.patch
# ZDI-CAN-30136 - CVE-2026-50256 - Font Alias Stack-based Buffer Overflow
Patch:     0007-dix-increase-XLFDMAXFONTNAMELEN-to-match-libXfont2-s.patch
# Other security related fixes
Patch:     0001-os-use-close-on-exec-for-X-server-socket-to-prevent-.patch
Patch:     0002-xf86bigfont-fix-Wimplicit-function-declaration-error.patch
Patch:     0003-dix-Fix-builds-with-meson-Dxace-false-Dwerror-true.patch
Patch:     0004-meson-don-t-build-xselinux-if-xace-is-disabled.patch
Patch:     0005-xwayland-fix-builds-with-xace-disabled.patch
Patch:     0006-panoramix-avoid-null-dereference-in-PanoramiXMaybeAd.patch
Patch:     0007-panoramix-avoid-null-dereference-in-PanoramiXConsoli.patch
Patch:     0008-glamor-handle-potential-NULL-return-from-GetPictureS.patch
Patch:     0009-glamor-handle-allocation-failure-in-glamor_create_pi.patch
Patch:     0010-glamor-silence-false-positive-in-glamor_validate_gc.patch
Patch:     0011-glamor-handle-allocation-failures-in-glamor_largepix.patch
Patch:     0012-glamor-avoid-null-dereference-in-glamor_dash_setup.patch
Patch:     0013-glamor-avoid-null-dereference-in-glamor_composite_cl.patch
Patch:     0014-glamor-avoid-double-free-in-glamor_make_pixmap_expor.patch
Patch:     0015-dix-set-errorValue-correctly-when-XID-lookup-fails-i.patch
Patch:     0016-os-avoid-closing-null-fd-at-Fopen.patch
Patch:     0017-os-make-FormatInt64-handle-LONG_MIN-correctly.patch
Patch:     0018-xwayland-wrong-expecting_event.patch
Patch:     0019-render-fix-multiple-mem-leaks-on-err-paths.patch
Patch:     0020-dix-avoid-null-ptr-deref-at-doListFontsAndAliases.patch
Patch:     0021-randr-clear-primary-screen-s-primaryOutput-when-the-.patch
Patch:     0022-os-include-assert.h-in-ospoll.c.patch
Patch:     0023-xkb-fix-incorrect-size-check-when-growing-doodads-in.patch
Patch:     0024-xkb-fix-potential-buff-overflow-in-XkbVModIndexText-.patch
Patch:     0025-Xi-add-missing-gesture-grab-type-checks-in-ProcXIPas.patch
Patch:     0026-xkb-Fix-out-of-bounds-array-access-in-_CheckSetShape.patch
Patch:     0027-xkb-Fix-off-by-one-in-color-index-validation-in-_Che.patch
Patch:     0028-xkb-Fix-off-by-one-and-NULL-dereferences-in-_CheckSe.patch
Patch:     0029-xkb-Add-bounds-check-for-action-data-in-CheckKeyActi.patch
Patch:     0030-present-actually-return-the-created-notifies.patch
Patch:     0031-glx-reject-negative-size-in-FeedbackBuffer-and-Selec.patch
# https://gitlab.freedesktop.org/xorg/xserver/-/merge_requests/2237
Patch:     0001-dix-Silence-a-compiler-warning-in-doListFontsAndAlia.patch

License:   MIT

Requires: xorg-x11-server-common
Requires: libEGL
Requires: libepoxy >= 1.5.5

BuildRequires: gcc
BuildRequires: git-core
BuildRequires: meson

BuildRequires: wayland-devel
BuildRequires: desktop-file-utils

BuildRequires: pkgconfig(wayland-client) >= 1.21.0
BuildRequires: pkgconfig(wayland-protocols) >= 1.34
BuildRequires: pkgconfig(wayland-eglstream-protocols)

BuildRequires: pkgconfig(epoxy) >= 1.5.5
BuildRequires: pkgconfig(fontenc)
BuildRequires: pkgconfig(libdrm) >= 2.4.89
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
BuildRequires: pkgconfig(libxcvt)
BuildRequires: pkgconfig(libdecor-0) >= 0.1.1
BuildRequires: xorg-x11-proto-devel >= 2024.1-1

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
Requires: %{name}%{?_isa} = %{version}-%{release}

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
        -Dserverconfigdir=%{_datadir}/xwayland \
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

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files
%dir %{_datadir}/xwayland
%{_bindir}/Xwayland
%{_mandir}/man1/Xwayland.1*
%{_datadir}/applications/org.freedesktop.Xwayland.desktop
%{_datadir}/xwayland/protocol.txt

%files devel
%{_libdir}/pkgconfig/xwayland.pc

%changelog
* Fri Jun 12 2026  Olivier Fourdan <ofourdan@redhat.com> - 24.1.9-4.2
- Other security related fixes
  Resolves: https://redhat.atlassian.net/browse/RHEL-184292

* Wed Jun 10 2026  Olivier Fourdan <ofourdan@redhat.com> - 24.1.9-4.1
- CVE fix for: CVE-2026-50256, CVE-2026-50257, CVE-2026-50258,
               CVE-2026-50259, CVE-2026-50260, CVE-2026-50261,
               CVE-2026-50262, CVE-2026-50263
  Resolves: https://redhat.atlassian.net/browse/RHEL-182426

* Wed Apr 22 2026 Olivier Fourdan <ofourdan@redhat.com> - 24.1.9-4
- CVE fix for: CVE-2026-33999, CVE-2026-34000, CVE-2026-34001
               CVE-2026-34002, CVE-2026-34003
  Resolves: https://redhat.atlassian.net/browse/RHEL-163199
  Resolves: https://redhat.atlassian.net/browse/RHEL-163295
  Resolves: https://redhat.atlassian.net/browse/RHEL-163253

* Tue Apr 21 2026 Olivier Fourdan <ofourdan@redhat.com> - 24.1.9-3
- Fix a regression in Xwayland 24.1.9 with XTS test Xlib10
  Resolves: https://redhat.atlassian.net/browse/RHEL-170368

* Tue Jan 13 2026 Michel Dänzer  <mdaenzer@redhat.com> - 24.1.9-2
- Rebuild against xorg-x11-xtrans-devel 1.4.0-9
  Resolves: RHEL-117510

* Thu Nov 20 2025 Olivier Fourdan <ofourdan@redhat.com> - 24.1.9-1
- Rebase to Xwayland 24.1.9 (RHEL-129828)

* Thu Oct 30 2025 Olivier Fourdan <ofourdan@redhat.com> - 23.2.7-5
- CVE fix for: CVE-2025-62229 (RHEL-119977), CVE-2025-62230 (RHEL-120023),
               CVE-2025-62231 (RHEL-125018)

* Wed Jun 18 2025 Olivier Fourdan <ofourdan@redhat.com> - 23.2.7-4
- CVE fix for: CVE-2025-49175 (RHEL-97288), CVE-2025-49176 (RHEL-97334),
               CVE-2025-49177 (RHEL-97357), CVE-2025-49178 (RHEL-97393),
               CVE-2025-49179 (RHEL-97404), CVE-2025-49180 (RHEL-97244)

* Wed Feb 26 2025 Olivier Fourdan <ofourdan@redhat.com> - 23.2.7-3
- CVE fix for: CVE-2025-26594 (RHEL-80204), CVE-2025-26595 (RHEL-80187),
               CVE-2025-26596 (RHEL-80190), CVE-2025-26597 (RHEL-80193),
               CVE-2025-26598 (RHEL-80195), CVE-2025-26599 (RHEL-80202),
               CVE-2025-26600 (RHEL-80203), CVE-2025-26601 (RHEL-80207)

* Wed Oct 30 2024 Olivier Fourdan <ofourdan@redhat.com> - 23.2.7-2
- Fix for CVE-2024-9632 - (RHEL-61997)

* Thu May 16 2024 Olivier Fourdan <ofourdan@redhat.com> - 23.2.7-1
- xwayland 23.2.7 - (RHEL-29912)

* Thu Apr  4 2024 Olivier Fourdan <ofourdan@redhat.com> - 21.1.9-7
- CVE fix for: CVE-2024-31080, CVE-2024-31081, CVE-2024-31083

* Wed Mar 13 2024 Olivier Fourdan <ofourdan@redhat.com> - 21.1.9-6
  New build to add xorg-x11-server-Xwayland-devel (RHEL-25083)

* Tue Jan 16 2024 Olivier Fourdan <ofourdan@redhat.com> - 21.1.9-5
  Fix for CVE-2023-6816, CVE-2024-0229, CVE-2024-21885, CVE-2024-21886,
  CVE-2024-0408, CVE-2024-0409

* Wed Dec 13 2023 Olivier Fourdan <ofourdan@redhat.com> - 21.1.9-4
- Fix for CVE-2023-6377, CVE-2023-6478

* Wed Oct 25 2023 Olivier Fourdan <ofourdan@redhat.com> - 22.1.9-3
- Fix for CVE-2023-5367

* Tue Apr 25 2023 Olivier Fourdan <ofourdan@redhat.com> - 22.1.9-2
- Rebuild (#2158761)

* Mon Apr  3 2023 Olivier Fourdan <ofourdan@redhat.com> - 22.1.9-1
- xwayland 22.1.9 (#2158761)

* Fri Mar 31 2023 Olivier Fourdan <ofourdan@redhat.com> - 21.1.3-8
- Fix CVE-2023-1393 (#2180299)

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
