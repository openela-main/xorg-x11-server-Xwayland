%global commit 9a55c402aa803fb10e39ab4fd18a709d0cd06fd4
%global shortcommit %(c=%{commit}; echo ${c:0:7})

#global gitdate 20230426
%global pkgname %{?gitdate:xserver}%{!?gitdate:xwayland}

%global default_font_path "catalogue:/etc/X11/fontpath.d,built-ins"

Summary:   Xwayland
Name:      xorg-x11-server-Xwayland
Version:   24.1.5
Release:   5%{?gitdate:.%{gitdate}git%{shortcommit}}%{?dist}

URL:       http://www.x.org
%if 0%{?gitdate}
Source0:   https://gitlab.freedesktop.org/xorg/%{pkgname}/-/archive/%{commit}/%{pkgname}-%{shortcommit}.tar.gz
%else
Source0:   https://www.x.org/pub/individual/xserver/%{pkgname}-%{version}.tar.xz
%endif

# Fix a regression with gamescope
# https://gitlab.freedesktop.org/xorg/xserver/-/issues/1790
Patch:     0001-Revert-xwayland-Don-t-run-key-behaviors-and-actions.patch
# CVE-2025-26594: Use-after-free of the root cursor
Patch: 0001-Cursor-Refuse-to-free-the-root-cursor.patch
Patch: 0002-dix-keep-a-ref-to-the-rootCursor.patch
# CVE-2025-26595: Buffer overflow in XkbVModMaskText()
Patch: 0003-xkb-Fix-buffer-overflow-in-XkbVModMaskText.patch
# CVE-2025-26596: Heap overflow in XkbWriteKeySyms()
Patch: 0004-xkb-Fix-computation-of-XkbSizeKeySyms.patch
# CVE-2025-26597: Buffer overflow in XkbChangeTypesOfKey()
Patch: 0005-xkb-Fix-buffer-overflow-in-XkbChangeTypesOfKey.patch
# CVE-2025-26598: Out-of-bounds write in CreatePointerBarrierClient()
Patch: 0006-Xi-Fix-barrier-device-search.patch
# CVE-2025-26599: Use of uninitialized pointer in compRedirectWindow()
Patch: 0007-composite-Handle-failure-to-redirect-in-compRedirect.patch
Patch: 0008-composite-initialize-border-clip-even-when-pixmap-al.patch
# CVE-2025-26600: Use-after-free in PlayReleasedEvents()
Patch: 0009-dix-Dequeue-pending-events-on-frozen-device-on-remov.patch
# CVE-2025-26601: Use-after-free in SyncInitTrigger()
Patch: 0010-sync-Do-not-let-sync-objects-uninitialized.patch
Patch: 0011-sync-Check-values-before-applying-changes.patch
Patch: 0012-sync-Do-not-fail-SyncAddTriggerToSyncObject.patch
Patch: 0013-sync-Apply-changes-last-in-SyncChangeAlarmAttributes.patch
# CVE-2025-49175: Out-of-bounds access in X Rendering extension
Patch: 0001-render-Avoid-0-or-less-animated-cursors.patch
# CVE-2025-49176: Integer overflow in Big Requests Extension
Patch: 0002-os-Do-not-overflow-the-integer-size-with-BigRequest.patch
Patch: 0003-os-Check-for-integer-overflow-on-BigRequest-length.patch
# CVE-2025-49177: Data leak in XFIXES Extension 6
Patch: 0004-xfixes-Check-request-length-for-SetClientDisconnectM.patch
# CVE-2025-49178: Unprocessed client request via bytes to ignore
Patch: 0005-os-Account-for-bytes-to-ignore-when-sharing-input-bu.patch
# CVE-2025-49179: Integer overflow in X Record extension
Patch: 0006-record-Check-for-overflow-in-RecordSanityCheckRegist.patch
# CVE-2025-49180: Integer overflow in RandR extension
Patch: 0007-randr-Check-for-overflow-in-RRChangeProviderProperty.patch
# CVE-2025-62229: Use-after-free in XPresentNotify structures creation
Patch: 0001-present-Fix-use-after-free-in-present_create_notifie.patch
# CVE-2025-62230: Use-after-free in Xkb client resource removal
Patch: 0002-xkb-Make-the-RT_XKBCLIENT-resource-private.patch
Patch: 0003-xkb-Free-the-XKB-resource-when-freeing-XkbInterest.patch
# CVE-2025-62231: Value overflow in Xkb extension XkbSetCompatMap()
Patch: 0004-xkb-Prevent-overflow-in-XkbSetCompatMap.patch

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
* Thu Oct 30 2025 Olivier Fourdan <ofourdan@redhat.com> - 24.1.5-5
- CVE fix for: CVE-2025-62229 (RHEL-119964), CVE-2025-62230 (RHEL-120013),
               CVE-2025-62231 (RHEL-125006)

* Wed Jun 18 2025 Olivier Fourdan <ofourdan@redhat.com> - 24.1.5-4
- CVE fix for: CVE-2025-49175 (RHEL-97130), CVE-2025-49176 (RHEL-97136),
               CVE-2025-49177 (RHEL-97142), CVE-2025-49178 (RHEL-97148),
               CVE-2025-49179 (RHEL-97154), CVE-2025-49180 (RHEL-97160)

* Wed May 7 2025 Tomas Pelka <tpelka@redhat.com> - 24.1.5-3
Rebuild for 10.0.z required due to issue when releasing original erratum.
- CVE fix for: CVE-2025-26594 (RHEL-80504), CVE-2025-26595 (RHEL-80505),
               CVE-2025-26596 (RHEL-80510), CVE-2025-26597 (RHEL-80511),
               CVE-2025-26598 (RHEL-80513), CVE-2025-26599 (RHEL-80512),
               CVE-2025-26600 (RHEL-80517), CVE-2025-26601 (RHEL-80516)

* Wed Feb 26 2025 Olivier Fourdan <ofourdan@redhat.com> - 24.1.5-2
- CVE fix for: CVE-2025-26594 (RHEL-79127), CVE-2025-26595 (RHEL-79131),
               CVE-2025-26596 (RHEL-79142), CVE-2025-26597 (RHEL-79144),
               CVE-2025-26598 (RHEL-79145), CVE-2025-26599 (RHEL-79147),
               CVE-2025-26600 (RHEL-79155), CVE-2025-26601 (RHEL-79151)

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
