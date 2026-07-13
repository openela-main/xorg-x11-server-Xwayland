%global commit 280aac5a0ee09c45b17ec4be0681397f7c34c12e
%global shortcommit %(c=%{commit}; echo ${c:0:7})

#global gitdate 20210201
%global pkgname %{?gitdate:xserver}%{!?gitdate:xwayland}

%global default_font_path "catalogue:/etc/X11/fontpath.d,built-ins"

Summary:   Xwayland
Name:      xorg-x11-server-Xwayland
Version:   21.1.3
Release:   20%{?gitdate:.%{gitdate}git%{shortcommit}}%{?dist}.3

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
Patch5: 0001-present-Send-a-PresentConfigureNotify-event-for-dest.patch

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
Patch10018: 0001-Xtest-disallow-GenericEvents-in-XTestSwapFakeInput.patch
# related to CVE-2022-46344
Patch10019: 0002-Xi-return-an-error-from-XI-property-changes-if-verif.patch
# CVE-2022-46344
Patch10020: 0003-Xi-avoid-integer-truncation-in-length-check-of-ProcX.patch
# CVE-2022-46341
Patch10021: 0004-Xi-disallow-passive-grabs-with-a-detail-255.patch
# CVE-2022-46343
Patch10022: 0005-Xext-free-the-screen-saver-resource-when-replacing-i.patch
# CVE-2022-46342
Patch10023: 0006-Xext-free-the-XvRTVideoNotify-when-turning-off-from-.patch
# CVE-2022-4283
Patch10024: 0007-xkb-reset-the-radio_groups-pointer-to-NULL-after-fre.patch
# Follow-up to CVE-2022-46340
Patch10025: 0008-Xext-fix-invalid-event-type-mask-in-XTestSwapFakeInp.patch
# CVE-2023-0494
Patch10026: 0001-Xi-fix-potential-use-after-free-in-DeepCopyPointerCl.patch
# CVE-2023-1393
Patch10027: 0001-composite-Fix-use-after-free-of-the-COW.patch
# CVE-2023-5367
Patch10028: 0001-Xi-randr-fix-handling-of-PropModeAppend-Prepend.patch
# CVE-2023-6478
Patch10029: 0001-randr-avoid-integer-truncation-in-length-check-of-Pr.patch
# CVE-2023-6377
Patch10030: 0001-Xi-allocate-enough-XkbActions-for-our-buttons.patch
# Fix for CVE-2023-6816, ZDI-CAN-22664, ZDI-CAN-22665
Patch10031:   0001-dix-allocate-enough-space-for-logical-button-maps.patch
# Fix for CVE-2024-0229, ZDI-CAN-22678
Patch10032:   0002-dix-Allocate-sufficient-xEvents-for-our-DeviceStateN.patch
Patch10033:   0003-dix-fix-DeviceStateNotify-event-calculation.patch
Patch10034:   0004-Xi-when-creating-a-new-ButtonClass-set-the-number-of.patch
# Fix for CVE-2024-21885, ZDI-CAN-22744
Patch10035:   0005-Xi-flush-hierarchy-events-after-adding-removing-mast.patch
# Fix for CVE-2024-21886, ZDI-CAN-22840
Patch10036:   0006-Xi-do-not-keep-linked-list-pointer-during-recursion.patch
Patch10037:   0007-dix-when-disabling-a-master-float-disabled-slaved-de.patch
# Fix for CVE-2024-0408
Patch10038:   0008-glx-Call-XACE-hooks-on-the-GLX-buffer.patch
# Fix for CVE-2024-0409
Patch10039:   0009-ephyr-xwayland-Use-the-proper-private-key-for-cursor.patch
# Fix for copy/paste error in previous CVE fix
Patch10040:  0001-dix-fix-valuator-copy-paste-error-in-the-DeviceState.patch
# Fix for CVE-2024-31080
Patch10041:  0002-Xi-ProcXIGetSelectedEvents-needs-to-use-unswapped-le.patch
# Fix for CVE-2024-31081
Patch10042:  0003-Xi-ProcXIPassiveGrabDevice-needs-to-use-unswapped-le.patch
# Fix for CVE-2024-31083, ZDI-CAN-22880
Patch10043:  0004-render-fix-refcounting-of-glyphs-during-ProcRenderAd.patch
# Fix for the fix for CVE-2024-31083
# https://gitlab.freedesktop.org/xorg/xserver/-/issues/1659
Patch10044: 0001-render-Avoid-possible-double-free-in-ProcRenderAddGl.patch
# Fix for CVE-2024-9632
Patch10045: 0001-xkb-Fix-buffer-overflow-in-_XkbSetCompatMap.patch
# CVE-2025-49175: Out-of-bounds access in X Rendering extension
Patch10046: 0001-render-Avoid-0-or-less-animated-cursors.patch
# CVE-2025-49176: Integer overflow in Big Requests Extension
Patch10047: 0002-os-Do-not-overflow-the-integer-size-with-BigRequest.patch
Patch10048: 0003-os-Check-for-integer-overflow-on-BigRequest-length.patch
# CVE-2025-49178: Unprocessed client request via bytes to ignore
Patch10049: 0004-os-Account-for-bytes-to-ignore-when-sharing-input-bu.patch
# CVE-2025-49179: Integer overflow in X Record extension
Patch10050: 0005-record-Check-for-overflow-in-RecordSanityCheckRegist.patch
# CVE-2025-49180: Integer overflow in RandR extension
Patch10051: 0006-randr-Check-for-overflow-in-RRChangeProviderProperty.patch
# CVE-2025-62229: Use-after-free in XPresentNotify structures creation
Patch10052: 0001-present-Fix-use-after-free-in-present_create_notifie.patch
# CVE-2025-62230: Use-after-free in Xkb client resource removal
Patch10053: 0002-xkb-Make-the-RT_XKBCLIENT-resource-private.patch
Patch10054: 0003-xkb-Free-the-XKB-resource-when-freeing-XkbInterest.patch
# CVE-2025-62231: Value overflow in Xkb extension XkbSetCompatMap()
Patch10055: 0004-xkb-Prevent-overflow-in-XkbSetCompatMap.patch
# CVE-2026-33999: XKB Integer Underflow in XkbSetCompatMap()
Patch10056: 0001-xkb-fix-buffer-re-use-in-_XkbSetCompatMap.patch
# CVE-2026-34000: XKB Out-of-bounds Read in CheckSetGeom()
Patch10057: 0002-xkb-Fix-bounds-check-in-_CheckSetGeom.patch
# CVE-2026-34001: XSYNC Use-after-free in miSyncTriggerFence()
Patch10058: 0003-miext-sync-Fix-use-after-free-in-miSyncTriggerFence.patch
# CVE-2026-34002: XKB Out-of-bounds read in CheckModifierMap()
Patch10059: 0004-xkb-Fix-out-of-bounds-read-in-CheckModifierMap.patch
# CVE-2026-34003: XKB Buffer overflow in CheckKeyTypes()
Patch10060: 0005-xkb-Add-additional-bound-checking-in-CheckKeyTypes.patch
Patch10061: 0006-xkb-Add-more-_XkbCheckRequestBounds.patch
# ZDI-CAN-30159 - CVE-2026-50257 - XSYNC Use-After-Free in miSyncDestroyFence()
# ZDI-CAN-30163 - CVE-2026-50260 - XSYNC Use-After-Free in FreeCounter()
Patch10062: 0001-sync-fix-deletion-of-counters-and-fences.patch
# ZDI-CAN-30164 - CVE-2026-50261 - XSYNC Use-After-Free in SyncChangeCounter()
Patch10063: 0002-sync-restart-trigger-list-iteration-in-SyncChangeCou.patch
# ZDI-CAN-30160 - CVE-2026-50258 - XKB Key Types Stack-based Buffer Overflow
Patch10064: 0003-xkb-reject-key-types-with-num_levels-exceeding-XkbMa.patch
# ZDI-CAN-30161 - CVE-2026-50259 - XKB SetMap Request Stack-based Buffer Overflow
Patch10065: 0004-xkb-clamp-nMaps-to-mapWidths-buffer-size-in-CheckKey.patch
# ZDI-CAN-30165 - CVE-2026-50262 - GLX ChangeDrawableAttributes Out-Of-Bounds Read/Write
Patch10066: 0005-glx-fix-reversed-length-check-in-ChangeDrawableAttri.patch
# ZDI-CAN-30168 - CVE-2026-50263 - CreateSaverWindow Use-After-Free Information Disclosure
Patch10067: 0006-saver-re-fetch-screen-private-after-CheckScreenPriva.patch
# ZDI-CAN-30136 - CVE-2026-50256 - Font Alias Stack-based Buffer Overflow
Patch10068: 0007-dix-increase-XLFDMAXFONTNAMELEN-to-match-libXfont2-s.patch
# Other security related fixes
Patch10069: 0001-os-avoid-potential-out-of-bounds-access-at-logVHdrMe.patch
Patch10070: 0002-dix-avoid-null-ptr-deref-at-doListFontsWithInfo.patch
Patch10071: 0003-Xext-shm-avoid-null-dereference-in-ShmInitScreenPriv.patch
Patch10072: 0004-Xext-sync-avoid-null-dereference-if-SysCounterGetPri.patch
Patch10073: 0005-Xext-sync-avoid-null-dereference-in-init_system_idle.patch
Patch10074: 0006-Xext-sync-Avoid-dereference-of-invalid-pointer-if-ma.patch
Patch10075: 0007-Xext-vidmode-avoid-null-dereference-if-VidModeCreate.patch
Patch10076: 0008-Xext-xres-avoid-null-dereference-in-ProcXResQueryCli.patch
Patch10077: 0009-Xext-xselinux-add-fast-path-to-ProcSELinuxListSelect.patch
Patch10078: 0010-Xext-xselinux-avoid-memory-leak-in-SELinuxAtomToSID.patch
Patch10079: 0011-Xext-xtest-avoid-null-dereference-in-ProcXTestFakeIn.patch
Patch10080: 0012-Xi-avoid-null-dereference-if-wOtherInputMasks-return.patch
Patch10081: 0013-Xi-set-value-for-led_values-in-CopySwapKbdFeedback.patch
Patch10082: 0014-Xi-handle-allocation-failure-in-ProcXGetDeviceDontPr.patch
Patch10083: 0015-Xi-handle-allocation-failure-in-ProcXListInputDevice.patch
Patch10084: 0016-Xi-handle-allocation-failure-in-add_master_func.patch
Patch10085: 0017-dix-handle-allocation-failure-in-DeviceFocusEvent.patch
Patch10086: 0018-dix-avoid-null-dereference-if-wOtherInputMasks-retur.patch
Patch10087: 0019-dix-assert-that-size-of-buffers-to-swap-is-a-multipl.patch
Patch10088: 0020-dix-handle-allocation-failure-in-ChangeWindowDeviceC.patch
Patch10089: 0021-os-use-close-on-exec-for-X-server-socket-to-prevent-.patch
Patch10090: 0022-xf86bigfont-fix-Wimplicit-function-declaration-error.patch
Patch10091: 0023-dix-Fix-builds-with-meson-Dxace-false-Dwerror-true.patch
Patch10092: 0024-meson-don-t-build-xselinux-if-xace-is-disabled.patch
Patch10093: 0025-panoramix-avoid-null-dereference-in-PanoramiXMaybeAd.patch
Patch10094: 0026-panoramix-avoid-null-dereference-in-PanoramiXConsoli.patch
Patch10095: 0027-glamor-handle-potential-NULL-return-from-GetPictureS.patch
Patch10096: 0028-glamor-handle-allocation-failure-in-glamor_create_pi.patch
Patch10097: 0029-glamor-silence-false-positive-in-glamor_validate_gc.patch
Patch10098: 0030-glamor-handle-allocation-failures-in-glamor_largepix.patch
Patch10099: 0031-glamor-avoid-null-dereference-in-glamor_dash_setup.patch
Patch10100: 0032-glamor-avoid-null-dereference-in-glamor_composite_cl.patch
Patch10101: 0033-glamor-avoid-double-free-in-glamor_make_pixmap_expor.patch
Patch10102: 0034-dix-set-errorValue-correctly-when-XID-lookup-fails-i.patch
Patch10103: 0035-os-avoid-closing-null-fd-at-Fopen.patch
Patch10104: 0036-os-make-FormatInt64-handle-LONG_MIN-correctly.patch
Patch10105: 0037-xwayland-wrong-expecting_event.patch
Patch10106: 0038-render-fix-multiple-mem-leaks-on-err-paths.patch
Patch10107: 0039-dix-avoid-null-ptr-deref-at-doListFontsAndAliases.patch
Patch10108: 0040-randr-clear-primary-screen-s-primaryOutput-when-the-.patch
Patch10109: 0041-os-include-assert.h-in-ospoll.c.patch
Patch10110: 0042-xkb-fix-incorrect-size-check-when-growing-doodads-in.patch
Patch10111: 0043-xkb-fix-potential-buff-overflow-in-XkbVModIndexText-.patch
# No XIGrabtypeGestureSwipeBegin in el8
# Patch10112: 0044-Xi-add-missing-gesture-grab-type-checks-in-ProcXIPas.patch
Patch10113: 0045-xkb-Fix-out-of-bounds-array-access-in-_CheckSetShape.patch
Patch10114: 0046-xkb-Fix-off-by-one-in-color-index-validation-in-_Che.patch
Patch10115: 0047-xkb-Fix-off-by-one-and-NULL-dereferences-in-_CheckSe.patch
Patch10116: 0048-xkb-Add-bounds-check-for-action-data-in-CheckKeyActi.patch
Patch10117: 0049-present-actually-return-the-created-notifies.patch
Patch10118: 0050-glx-reject-negative-size-in-FeedbackBuffer-and-Selec.patch
# https://gitlab.freedesktop.org/xorg/xserver/-/merge_requests/2237
Patch10119: 0001-dix-Silence-a-compiler-warning-in-doListFontsAndAlia.patch
# https://gitlab.freedesktop.org/xorg/xserver/-/merge_requests/1257
Patch10120: 0001-xkb-fix-int-size-mismatch.patch
# CVE-2026-56000: GLX contextTags Use-After-Free in CommonMakeCurrent()
# Not applicable to Xwayland 21.1
# CVE-2026-55999: glamor Font Atlas Heap Buffer Overflow
Patch10122: 0002-fb-mi-glamor-reject-glyphs-with-negative-dimensions.patch
Patch10123: 0003-glamor-reject-fonts-with-per-glyph-metrics-exceeding.patch

License:   MIT

Requires: xorg-x11-server-common
Requires: libEGL
Requires: libepoxy >= 1.5.5

BuildRequires: gcc
BuildRequires: git-core
BuildRequires: meson

BuildRequires: wayland-devel
BuildRequires: pkgconfig(wayland-client) >= 1.3.0
BuildRequires: pkgconfig(wayland-protocols)
BuildRequires: pkgconfig(wayland-eglstream-protocols)

BuildRequires: pkgconfig(dmx)
BuildRequires: pkgconfig(epoxy) >= 1.5.5
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
* Wed Jul 08 2026 Olivier Fourdan <ofourdan@redhat.com> - 21.1.3-20.3
- CVE fix for: CVE-2026-55999
  Resolves: https://redhat.atlassian.net/browse/RHEL-191516

* Fri Jun 12 2026  Olivier Fourdan <ofourdan@redhat.com> - 21.1.3-20.2
- Other security related fixes
  Resolves: https://redhat.atlassian.net/browse/RHEL-184293

* Wed Jun 10 2026  Olivier Fourdan <ofourdan@redhat.com> - 21.1.3-20.1
- CVE fix for: CVE-2026-50256, CVE-2026-50257, CVE-2026-50258,
               CVE-2026-50259, CVE-2026-50260, CVE-2026-50261,
               CVE-2026-50262, CVE-2026-50263
  Resolves: https://redhat.atlassian.net/browse/RHEL-182445

* Tue Apr 14 2026 Olivier Fourdan <ofourdan@redhat.com> - 21.1.3-20
- CVE fix for: CVE-2026-33999, CVE-2026-34000, CVE-2026-34001
               CVE-2026-34002, CVE-2026-34003
  Resolves: https://redhat.atlassian.net/browse/RHEL-163191
  Resolves: https://redhat.atlassian.net/browse/RHEL-163287
  Resolves: https://redhat.atlassian.net/browse/RHEL-163245

* Thu Oct 30 2025 Olivier Fourdan <ofourdan@redhat.com> - 21.1.3-19
- CVE fix for: CVE-2025-62229 (RHEL-119967), CVE-2025-62230 (RHEL-120015),
               CVE-2025-62231 (RHEL-125007)

* Wed Jun 18 2025 Olivier Fourdan <ofourdan@redhat.com> - 21.1.3-18
- CVE fix for: CVE-2025-49175 (RHEL-97278), CVE-2025-49176 (RHEL-97299,
               CVE-2025-49178 (RHEL-97374), CVE-2025-49179 (RHEL-97417),
               CVE-2025-49180 (RHEL-97249)

* Wed Oct 30 2024 Olivier Fourdan <ofourdan@redhat.com> - 21.1.3-17
- Fix for CVE-2024-9632 - (RHEL-61995)

* Thu Apr  4 2024 Olivier Fourdan <ofourdan@redhat.com> - 21.1.3-16
- CVE fix for: CVE-2024-31080, CVE-2024-31081, CVE-2024-31083

* Tue Jan 16 2024 Olivier Fourdan <ofourdan@redhat.com> - 21.1.3-15
  Fix for CVE-2023-6816, CVE-2024-0229, CVE-2024-21885, CVE-2024-21886,
  CVE-2024-0408, CVE-2024-0409

* Wed Dec 13 2023 Olivier Fourdan <ofourdan@redhat.com> - 21.1.3-14
- Fix for CVE-2023-6377, CVE-2023-6478

* Wed Oct 25 2023 Olivier Fourdan <ofourdan@redhat.com> - 21.1.3-13
- Fix for CVE-2023-5367

* Tue Jun 13 2023 Olivier Fourdan <ofourdan@redhat.com> - 21.1.3-12
- Backport fix for a deadlock with DRI3
  Resolves: rhbz#2212831

* Fri Mar 31 2023 Olivier Fourdan <ofourdan@redhat.com> - 21.1.3-11
- Fix CVE-2023-1393 (#2180298)

* Tue Feb  7 2023 Olivier Fourdan <ofourdan@redhat.com> - 21.1.3-10
- Fix CVE-2023-0494 (#2166972)

* Mon Dec 19 2022 Peter Hutterer <peter.hutterer@redhat.com> - 21.1.3-9
- Follow-up fix for CVE-2022-46340 (#2151777)

* Tue Dec 13 2022 Peter Hutterer <peter.hutterer@redhat.com> - 21.1.3-8
- CVE fix for: CVE-2022-4283 (#2151802), CVE-2022-46340 (#2151777),
  CVE-2022-46341 (#2151782), CVE-2022-46342 (#2151785),
  CVE-2022-46343 (#2151792), CVE-2022-46344 (#2151795)

* Mon Nov 14 2022 Olivier Fourdan <ofourdan@redhat.com> -  21.1.3-7
- Fix CVE-2022-3550, CVE-2022-3551
  Resolves: rhbz#2140767, rhbz#2140774

* Fri Jul 29 2022 Olivier Fourdan <ofourdan@redhat.com> - 21.1.3-6
- CVE fix for: CVE-2022-2319/ZDI-CAN-16062, CVE-2022-2320/ZDI-CAN-16070
  Resolves: rhbz#2110442, rhbz#2110437

* Thu Jun 09 2022 Ray Strode <rstrode@redhat.com> - 21.1.3-5
- Rebuild again for ipv6 xtrans fix
  Related: #2075132

* Tue May 24 2022 Ray Strode <rstrode@redhat.com> - 21.1.3-3
- Rebuild for ipv6 xtrans fix
  Related: #2075132

* Fri Jan  7 2022 Olivier Fourdan <ofourdan@redhat.com> - 21.1.3-2
- CVE fix for: CVE-2021-4008 (#2038066), CVE-2021-4009 (#2038068),
  CVE-2021-4010 (#2038071), CVE-2021-4011 (#2038073)

* Thu Dec  2 2021 Olivier Fourdan <ofourdan@redhat.com> - 21.1.3-1
- Rebase to 21.1.3 (rhbz#2015842)
- Prefer EGLstream if both EGLstream and GBM are usable

* Mon Aug  9 2021 Olivier Fourdan <ofourdan@redhat.com> - 21.1.1-6
- Backport the latest fixes from Xwayland for EGLstream (rhbz#1977741)

* Tue Jun 29 2021 Olivier Fourdan <ofourdan@redhat.com> - 21.1.1-5
- Require libepoxy >= 1.5.5 (rhbz#1976132)

* Mon Jun 21 2021 Olivier Fourdan <ofourdan@redhat.com> - 21.1.1-4
- Fix a use-after-free in the previous changes for GLX

* Mon Jun 14 2021 Olivier Fourdan <ofourdan@redhat.com> - 21.1.1-3
- Backport fixes for GLX and EGLstream (#1961981)

* Thu Jun  03 2021 Tomas Pelka <tpelka@redhat.com> - 21.1.1-2
- bump release and rebuild to correctly trigger gating

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
