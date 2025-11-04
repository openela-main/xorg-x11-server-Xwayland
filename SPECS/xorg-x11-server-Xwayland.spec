%global commit 280aac5a0ee09c45b17ec4be0681397f7c34c12e
%global shortcommit %(c=%{commit}; echo ${c:0:7})

#global gitdate 20210201
%global pkgname %{?gitdate:xserver}%{!?gitdate:xwayland}

%global default_font_path "catalogue:/etc/X11/fontpath.d,built-ins"

Summary:   Xwayland
Name:      xorg-x11-server-Xwayland
Version:   23.2.7
Release:   5%{?gitdate:.%{gitdate}git%{shortcommit}}%{?dist}

URL:       http://www.x.org
%if 0%{?gitdate}
Source0:   https://gitlab.freedesktop.org/xorg/%{pkgname}/-/archive/%{commit}/%{pkgname}-%{shortcommit}.tar.gz
%else
Source0:   https://www.x.org/pub/individual/xserver/%{pkgname}-%{version}.tar.xz
%endif

# Fix for CVE-2024-9632
Patch1:    0001-xkb-Fix-buffer-overflow-in-_XkbSetCompatMap.patch
# CVE-2025-26594: Use-after-free of the root cursor
Patch2: 0001-Cursor-Refuse-to-free-the-root-cursor.patch
Patch3: 0002-dix-keep-a-ref-to-the-rootCursor.patch
# CVE-2025-26595: Buffer overflow in XkbVModMaskText()
Patch4: 0003-xkb-Fix-buffer-overflow-in-XkbVModMaskText.patch
# CVE-2025-26596: Heap overflow in XkbWriteKeySyms()
Patch5: 0004-xkb-Fix-computation-of-XkbSizeKeySyms.patch
# CVE-2025-26597: Buffer overflow in XkbChangeTypesOfKey()
Patch6: 0005-xkb-Fix-buffer-overflow-in-XkbChangeTypesOfKey.patch
# CVE-2025-26598: Out-of-bounds write in CreatePointerBarrierClient()
Patch7: 0006-Xi-Fix-barrier-device-search.patch
# CVE-2025-26599: Use of uninitialized pointer in compRedirectWindow()
Patch8: 0007-composite-Handle-failure-to-redirect-in-compRedirect.patch
Patch9: 0008-composite-initialize-border-clip-even-when-pixmap-al.patch
# CVE-2025-26600: Use-after-free in PlayReleasedEvents()
Patch10: 0009-dix-Dequeue-pending-events-on-frozen-device-on-remov.patch
# CVE-2025-26601: Use-after-free in SyncInitTrigger()
Patch11: 0010-sync-Do-not-let-sync-objects-uninitialized.patch
Patch12: 0011-sync-Check-values-before-applying-changes.patch
Patch13: 0012-sync-Do-not-fail-SyncAddTriggerToSyncObject.patch
Patch14: 0013-sync-Apply-changes-last-in-SyncChangeAlarmAttributes.patch
# CVE-2025-49175: Out-of-bounds access in X Rendering extension
Patch15: 0001-render-Avoid-0-or-less-animated-cursors.patch
# CVE-2025-49176: Integer overflow in Big Requests Extension
Patch16: 0002-os-Do-not-overflow-the-integer-size-with-BigRequest.patch
Patch17: 0003-os-Check-for-integer-overflow-on-BigRequest-length.patch
# CVE-2025-49177: Data leak in XFIXES Extension 6
Patch18: 0004-xfixes-Check-request-length-for-SetClientDisconnectM.patch
# CVE-2025-49178: Unprocessed client request via bytes to ignore
Patch19: 0005-os-Account-for-bytes-to-ignore-when-sharing-input-bu.patch
# CVE-2025-49179: Integer overflow in X Record extension
Patch20: 0006-record-Check-for-overflow-in-RecordSanityCheckRegist.patch
# CVE-2025-49180: Integer overflow in RandR extension
Patch21: 0007-randr-Check-for-overflow-in-RRChangeProviderProperty.patch
# CVE-2025-62229: Use-after-free in XPresentNotify structures creation
Patch22: 0001-present-Fix-use-after-free-in-present_create_notifie.patch
# CVE-2025-62230: Use-after-free in Xkb client resource removal
Patch23: 0002-xkb-Make-the-RT_XKBCLIENT-resource-private.patch
Patch24: 0003-xkb-Free-the-XKB-resource-when-freeing-XkbInterest.patch
# CVE-2025-62231: Value overflow in Xkb extension XkbSetCompatMap()
Patch25: 0004-xkb-Prevent-overflow-in-XkbSetCompatMap.patch

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
BuildRequires: pkgconfig(wayland-protocols) >= 1.30
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
BuildRequires: xorg-x11-proto-devel >= 2023.2-1

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
* Thu Oct 30 2025 Olivier Fourdan <ofourdan@redhat.com> - 23.2.7-5
- CVE fix for: CVE-2025-62229 (RHEL-119975), CVE-2025-62230 (RHEL-120020),
               CVE-2025-62231 (RHEL-125016)

* Wed Jun 18 2025 Olivier Fourdan <ofourdan@redhat.com> - 23.2.7-4
- CVE fix for: CVE-2025-49175 (RHEL-97341), CVE-2025-49176 (RHEL-97335),
               CVE-2025-49177 (RHEL-97358), CVE-2025-49178 (RHEL-97395),
               CVE-2025-49179 (RHEL-97405), CVE-2025-49180 (RHEL-97245)

* Wed Feb 26 2025 Olivier Fourdan <ofourdan@redhat.com> - 23.2.7-3
- CVE fix for: CVE-2025-26594 (RHEL-79126), CVE-2025-26595 (RHEL-79130),
               CVE-2025-26596 (RHEL-79134), CVE-2025-26597 (RHEL-79140),
               CVE-2025-26598 (RHEL-79141), CVE-2025-26599 (RHEL-79146),
               CVE-2025-26600 (RHEL-79154), CVE-2025-26601 (RHEL-79150)

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
