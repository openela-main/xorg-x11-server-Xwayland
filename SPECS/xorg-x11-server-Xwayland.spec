%global commit 9a55c402aa803fb10e39ab4fd18a709d0cd06fd4
%global shortcommit %(c=%{commit}; echo ${c:0:7})

#global gitdate 20230426
%global pkgname %{?gitdate:xserver}%{!?gitdate:xwayland}

%global default_font_path "catalogue:/etc/X11/fontpath.d,built-ins"

Summary:   Xwayland
Name:      xorg-x11-server-Xwayland
Version:   24.1.9
Release:   4%{?gitdate:.%{gitdate}git%{shortcommit}}%{?dist}.3

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
# CVE-2026-56000: GLX contextTags Use-After-Free in CommonMakeCurrent()
Patch:     0001-glx-free-old-context-tag-before-allocating-new-one-i.patch
# CVE-2026-55999: glamor Font Atlas Heap Buffer Overflow
Patch:     0002-fb-mi-glamor-reject-glyphs-with-negative-dimensions.patch
Patch:     0003-glamor-reject-fonts-with-per-glyph-metrics-exceeding.patch

License:   MIT

Requires: xkeyboard-config
Requires: xkbcomp
Requires: libEGL
Requires: libepoxy >= 1.5.5

BuildRequires: gcc
BuildRequires: git-core
BuildRequires: meson

BuildRequires: wayland-devel
BuildRequires: desktop-file-utils

BuildRequires: pkgconfig(wayland-client) >= 1.21.0
BuildRequires: pkgconfig(wayland-protocols) >= 1.34

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
BuildRequires: pkgconfig(xrender)
BuildRequires: pkgconfig(xres)
BuildRequires: pkgconfig(xshmfence) >= 1.1
BuildRequires: pkgconfig(xtrans) >= 1.3.2
BuildRequires: pkgconfig(xtst)
BuildRequires: pkgconfig(xv)
BuildRequires: pkgconfig(libxcvt)
BuildRequires: pkgconfig(libdecor-0) >= 0.1.1
BuildRequires: pkgconfig(liboeffis-1.0) >= 1.0.0
BuildRequires: pkgconfig(libei-1.0) >= 1.0.0
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
	%{?gitdate:-Dxwayland=true -D{xorg,xnest,xvfb,udev}=false} \
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
rm -Rf $RPM_BUILD_ROOT%{_includedir}/xorg
rm -Rf $RPM_BUILD_ROOT%{_datadir}/aclocal

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
* Wed Jul 08 2026 Olivier Fourdan <ofourdan@redhat.com> - 24.1.9-4.3
- CVE fix for: CVE-2026-55999, CVE-2026-56000
  Resolves: https://redhat.atlassian.net/browse/RHEL-191518
  Resolves: https://redhat.atlassian.net/browse/RHEL-191517

* Fri Jun 12 2026  Olivier Fourdan <ofourdan@redhat.com> - 24.1.9-4.2
- Other security related fixes
  Resolves: https://redhat.atlassian.net/browse/RHEL-184290

* Wed Jun 10 2026  Olivier Fourdan <ofourdan@redhat.com> - 24.1.9-4.1
- CVE fix for: CVE-2026-50256, CVE-2026-50257, CVE-2026-50258,
               CVE-2026-50259, CVE-2026-50260, CVE-2026-50261,
               CVE-2026-50262, CVE-2026-50263
  Resolves: https://redhat.atlassian.net/browse/RHEL-182443

* Wed Apr 22 2026 Olivier Fourdan <ofourdan@redhat.com> - 24.1.9-4
- CVE fix for: CVE-2026-33999, CVE-2026-34000, CVE-2026-34001
               CVE-2026-34002, CVE-2026-34003
  Resolves: https://redhat.atlassian.net/browse/RHEL-163189
  Resolves: https://redhat.atlassian.net/browse/RHEL-163285
  Resolves: https://redhat.atlassian.net/browse/RHEL-163243

* Tue Apr 21 2026 Olivier Fourdan <ofourdan@redhat.com> - 24.1.9-3
- Fix a regression in Xwayland 24.1.9 with XTS test Xlib10
  Resolves: https://redhat.atlassian.net/browse/RHEL-169767

* Tue Jan 20 2026 Michel Dänzer  <mdaenzer@redhat.com> - 24.1.9-2
- Rebuild against xorg-x11-xtrans-devel 1.6.0-1
  Resolves: RHEL-117512

* Fri Nov  7 2025 Olivier Fourdan <ofourdan@redhat.com> - 24.1.9-1
- Rebase to Xwayland 24.1.9 (RHEL-120264)

* Thu Oct 30 2025 Olivier Fourdan <ofourdan@redhat.com> - 24.1.5-5
- CVE fix for: CVE-2025-62229 (RHEL-119966), CVE-2025-62230 (RHEL-120012),
               CVE-2025-62231 (RHEL-125005)

* Wed Jun 18 2025 Olivier Fourdan <ofourdan@redhat.com> - 24.1.5-4
- CVE fix for: CVE-2025-49175 (RHEL-97129), CVE-2025-49176 (RHEL-97135),
               CVE-2025-49177 (RHEL-97141), CVE-2025-49178 (RHEL-97147),
               CVE-2025-49179 (RHEL-97153), CVE-2025-49180 (RHEL-97159)

* Wed May 7 2025 Tomas Pelka <tpelka@redhat.com> - 24.1.5-3
Rebuild for 10.0.z required due to issue when releasing original erratum.
- CVE fix for: CVE-2025-26594 (RHEL-80504), CVE-2025-26595 (RHEL-80505),
               CVE-2025-26596 (RHEL-80510), CVE-2025-26597 (RHEL-80511),
               CVE-2025-26598 (RHEL-80513), CVE-2025-26599 (RHEL-80512),
               CVE-2025-26600 (RHEL-80517), CVE-2025-26601 (RHEL-80516)

* Wed Feb 26 2025 Olivier Fourdan <ofourdan@redhat.com> - 24.1.5-2
- CVE fix for: CVE-2025-26594 (RHEL-80504), CVE-2025-26595 (RHEL-80505),
               CVE-2025-26596 (RHEL-80510), CVE-2025-26597 (RHEL-80511),
               CVE-2025-26598 (RHEL-80513), CVE-2025-26599 (RHEL-80512),
               CVE-2025-26600 (RHEL-80517), CVE-2025-26601 (RHEL-80516)

* Tue Feb 11 2025 Olivier Fourdan <ofourdan@redhat.com> - 24.1.5-1
- xwayland 24.1.5 (RHEL-78562)
- Fix a regression with keyboard modifiers due to a bug in gamescope

* Thu Nov  7 2024  Olivier Fourdan <ofourdan@redhat.com> - 24.1.1-4
- Remove unneeded build dependencies on xorg-x11-util-macros and libXpm
- Remove unneeded build dependency on wayland-eglstream-protocols (RHEL-66317)

* Wed Oct 30 2024  Olivier Fourdan <ofourdan@redhat.com> - 24.1.1-3
- Fix for CVE-2024-9632 - (RHEL-61994)

* Tue Oct 29 2024 Troy Dawson <tdawson@redhat.com> - 24.1.1-2
- Bump release for October 2024 mass rebuild:
  Resolves: RHEL-64018

* Wed Jul 10 2024 Olivier Fourdan <ofourdan@redhat.com> - 24.1.1-1
- xwayland 24.1.1 (RHEL-45260)

* Mon Jun 24 2024 Troy Dawson <tdawson@redhat.com> - 24.1.0-2
- Bump release for June 2024 mass rebuild

* Wed May 15 2024 Olivier Fourdan <ofourdan@redhat.com> - 24.1.0-1
- xwayland 24.1.0 (RHEL-29911)

* Thu Apr  4 2024 Olivier Fourdan <ofourdan@redhat.com> - 23.2.4-4
- CVE fix for: CVE-2024-31080, CVE-2024-31081, CVE-2024-31083

* Mon Jan 29 2024 Florian Weimer <fweimer@redhat.com> - 23.2.4-3
- Fix C compatibility issue on i686

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 23.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jan 16 2024 Olivier Fourdan <ofourdan@redhat.com> - 23.2.4-1
- xwayland 23.2.4 - (#2254280)
  CVE fix for: CVE-2023-6816, CVE-2024-0229, CVE-2024-21885, CVE-2024-21886,
  CVE-2024-0408, CVE-2024-0409

* Wed Dec 13 2023 Peter Hutterer <peter.hutterer@redhat.com> - 23.2.3-1
- xwayland 23.2.3 
  CVE fix for: CVE-2023-6377, CVE-2023-6478

* Fri Nov 24 2023 Olivier Fourdan <ofourdan@redhat.com> - 23.2.2-2
- Drop dependency on xorg-x11-server-common

* Thu Oct 26 2023 Olivier Fourdan <ofourdan@redhat.com> - 23.2.2-1
- xwayland 23.2.2 - (#2246029)

* Wed Oct 25 2023 Peter Hutterer <peter.hutterer@redhat.com> - 23.2.1-2
- Fix for CVE-2023-5367

* Wed Sep 20 2023 Olivier Fourdan <ofourdan@redhat.com> - 23.2.1-1
- xwayland 23.2.1 - (#2239813)

* Mon Sep 11 2023 Olivier Fourdan <ofourdan@redhat.com> - 23.2.0-2
- migrated to SPDX license

* Wed Aug 16 2023 Olivier Fourdan <ofourdan@redhat.com> - 23.2.0-1
- xwayland 23.2.0

* Wed Aug  2 2023 Olivier Fourdan <ofourdan@redhat.com> - 23.1.99.902-1
- xwayland 23.1.99.902 (xwayland 23.2.0 rc2)

* Mon Jul 31 2023 Olivier Fourdan <ofourdan@redhat.com> - 23.1.99.901-2
- Fix devel package requires.

* Wed Jul 19 2023 Olivier Fourdan <ofourdan@redhat.com> - 23.1.99.901-1
- xwayland 23.1.99.901 (xwayland 23.2.0 rc1)

* Tue Jun  6 2023 Olivier Fourdan <ofourdan@redhat.com> - 23.1.2-1
- xwayland 23.1.2

* Thu Apr 27 2023 Olivier Fourdan <ofourdan@redhat.com> - 23.1.1-2
- Fix spec file to build from git upstream - (#2190211)

* Wed Mar 29 2023 Olivier Fourdan <ofourdan@redhat.com> - 23.1.1-1
- xwayland 23.1.1 - (#2182734)
  CVE fix for: CVE-2023-1393

* Wed Mar 22 2023 Olivier Fourdan <ofourdan@redhat.com> - 23.1.0-1
- xwayland 23.1.0 - (#2180913)

* Thu Mar  9 2023 Olivier Fourdan <ofourdan@redhat.com> - 23.0.99.902-1
- xwayland 23.0.99.902 (xwayland 23.1.0 rc2) - (#2172415, #2173201)

* Wed Feb 22 2023 Olivier Fourdan <ofourdan@redhat.com> - 23.0.99.901-1
- xwayland 23.0.99.901 (xwayland 23.1.0 rc1) - (#2172415)

* Tue Feb  7 2023 Olivier Fourdan <ofourdan@redhat.com> - 22.1.8-1
- xwayland 22.1.8
  Fixes CVE-2023-0494 (#2165995, #2167566, #2167734)

* Sun Jan 29 2023 Stefan Bluhm <stefan.bluhm@clacee.eu> - 22.1.7-4
- Updated conditional Fedora statement.

* Thu Jan 19 2023 Olivier Fourdan <ofourdan@redhat.com> - 22.1.7-3
- Use the recommended way to apply conditional patches without
  conditionalizing the sources (for byte-swapped clients).

* Tue Jan 17 2023 Olivier Fourdan <ofourdan@redhat.com> - 22.1.7-2
- Disallow byte-swapped clients on Fedora 38 and above (#2159489)

* Mon Dec 19 2022 Olivier Fourdan <ofourdan@redhat.com> - 22.1.7-1
- xwayland 22.1.7

* Wed Dec 14 2022 Peter Hutterer <peter.hutterer@redhat.com> - 22.1.6-1
- xwayland 22.1.6
  Fixes CVE-2022-46340, CVE-2022-46341, CVE-2022-46342, CVE-2022-46343,
  CVE-2022-46344, CVE-2022-4283

* Wed Nov  2 2022 Olivier Fourdan <ofourdan@redhat.com> - 22.1.5-1
- xwayland 22.1.5 (#2139387)

* Thu Oct 20 2022 Olivier Fourdan <ofourdan@redhat.com> - 22.1.4-1
- xwayland 22.1.4 (#2136518)

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 22.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 12 2022 Olivier Fourdan <ofourdan@redhat.com> - 22.1.3-1
- xwayland 22.1.3 - (#2106387)
  Fix CVE-2022-2319/ZDI-CAN-16062, CVE-2022-2320/ZDI-CAN-16070

* Wed May 25 2022 Olivier Fourdan <ofourdan@redhat.com> - 22.1.2-1
- xwayland 22.1.2 - (#2090172)

* Thu Mar 31 2022 Olivier Fourdan <ofourdan@redhat.com> - 22.1.1-1
- xwayland 22.1.1 - (#2070435)

* Wed Feb 16 2022 Olivier Fourdan <ofourdan@redhat.com> - 22.1.0
- xwayland 22.1.0 - (#2055270)

* Wed Feb  2 2022 Olivier Fourdan <ofourdan@redhat.com> - 22.0.99.902
- xwayland 22.0.99.902 (xwayland 22.1.0 rc2) - (#2042521)

* Tue Jan 25 2022 Olivier Fourdan <ofourdan@redhat.com> - 22.0.99.901
- xwayland 22.0.99.901 (xwayland 22.1.0 rc1) - (#2042521)

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 21.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Dec 14 2021 Olivier Fourdan <ofourdan@redhat.com> - 21.1.4
- xwayland 21.1.4

* Mon Nov  8 2021 Olivier Fourdan <ofourdan@redhat.com> - 21.1.3
- xwayland 21.1.3 - (#2016468)

* Thu Oct 21 2021 Olivier Fourdan <ofourdan@redhat.com> - 21.1.2.901-1
- xwayland 21.1.2.901 (aka 21.1.3 RC1) - (#2015413)

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 21.1.2-3
- Rebuilt with OpenSSL 3.0.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 21.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jul 9 2021 Olivier Fourdan <ofourdan@redhat.com> - 21.1.2-1
- xwayland 21.1.2

* Thu Jul 1 2021 Olivier Fourdan <ofourdan@redhat.com> - 21.1.1.901-1
- xwayland 21.1.1.901

* Mon Jun 21 2021 Olivier Fourdan <ofourdan@redhat.com> - 21.1.1-3
- Fix a use-after-free in the previous changes for GLX

* Thu Jun 10 2021 Olivier Fourdan <ofourdan@redhat.com> - 21.1.1-2
- Backport fixes for GLX and EGLstream (#1948003)

* Wed Apr  14 2021 Olivier Fourdan <ofourdan@redhat.com> - 21.1.1-1
- xwayland 21.1.1 (CVE-2021-3472 / ZDI-CAN-1259)

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
