%define origname wqy-bitmapfont
%define version 1.0.0
%define betaver RC1

Name:	x11-font-%{origname}
Version:	%{version}
Release:	%mkrel -c %betaver 5
Summary:	WenQuanYi Bitmap Song
Group:	System/Fonts/X11 bitmap
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL:	https://www.wenq.org
Source0:	http://downloads.sourceforge.net/project/wqy/wqy-bitmapfont/%version-%betaver/wqy-bitmapsong-pcf-%version-%betaver.tar.gz
License:	GPLv2+
BuildArch:	noarch
BuildRequires: fontconfig
Requires(pre):	mkfontdir, mkfontscale
Requires(postun):	mkfontdir, mkfontscale
Requires:	fontconfig >= 2.4.2-7
Conflicts:	fontconfig < 2.4.2-7

%description
WenQuanYi bitmap fonts include all 20,932 Unicode 5.2
CJK Unified Ideographs (U4E00 - U9FA5) and 6,582
CJK Extension A characters (U3400 - U4DB5) at
5 different pixel sizes (9pt-12X12, 10pt-13X13,
10.5pt-14x14, 11pt-15X15 and 12pt-16x16 pixel).
Use of this bitmap font for on-screen display of Chinese
(traditional and simplified) in web pages and elsewhere
eliminates the annoying "blurring" problems caused by
insufficient "hinting" of anti-aliased vector CJK fonts.
In addition, Latin characters, Japanese Kanas and
Korean Hangul glyphs (U+AC00~U+D7A3) are also included.

%prep
%setup -qn wqy-bitmapsong

%install
rm -fr %buildroot

install -d %{buildroot}/%_datadir/fonts/wqy
install -m 0644 *.pcf fonts.alias %{buildroot}/%_datadir/fonts/wqy

mkdir -p %{buildroot}%_sysconfdir/X11/fontpath.d/
ln -s ../../..%_datadir/fonts/wqy \
    %{buildroot}%_sysconfdir/X11/fontpath.d/wqy-bitmapfont:pri=50

%post
mkfontscale %_datadir/fonts/wqy
mkfontdir %_datadir/fonts/wqy

%postun
mkfontscale %_datadir/fonts/wqy
mkfontdir %_datadir/fonts/wqy

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README ChangeLog AUTHORS COPYING
%_sysconfdir/X11/fontpath.d/wqy-bitmapfont:pri=50
%_datadir/fonts/wqy/*.pcf
%_datadir/fonts/wqy/fonts.alias


%changelog
* Tue May 17 2011 Funda Wang <fwang@mandriva.org> 1.0.0-0.RC1.3mdv2011.0
+ Revision: 675497
- br fontconfig for fc-query used in new rpm-setup-build

* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-0.RC1.2
+ Revision: 671224
- mass rebuild

* Mon Apr 05 2010 Funda Wang <fwang@mandriva.org> 1.0.0-0.RC1.1mdv2011.0
+ Revision: 531676
- 1.0.0 RC 1

* Wed Jan 20 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.0-0.20090411.2mdv2010.1
+ Revision: 494171
- fc-cache is now called by an rpm filetrigger

* Sat Apr 11 2009 Funda Wang <fwang@mandriva.org> 1.0-0.20090411.1mdv2009.1
+ Revision: 366074
- new snapshot

* Sat Feb 07 2009 Funda Wang <fwang@mandriva.org> 1.0-0.20090207.1mdv2009.1
+ Revision: 338347
- new snapshot

* Thu Sep 11 2008 Funda Wang <fwang@mandriva.org> 1.0-0.20080910.1mdv2009.0
+ Revision: 283666
- New snapshot

* Thu Aug 14 2008 Funda Wang <fwang@mandriva.org> 1.0-0.20080814.1mdv2009.0
+ Revision: 272171
- New snapshot

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 1.0-0.20080526.2mdv2009.0
+ Revision: 266033
- rebuild early 2009.0 package (before pixel changes)

* Tue May 27 2008 Funda Wang <fwang@mandriva.org> 1.0-0.20080526.1mdv2009.0
+ Revision: 211486
- New snapshot

* Fri May 02 2008 Funda Wang <fwang@mandriva.org> 1.0-0.20080502.1mdv2009.0
+ Revision: 200465
- New snapshot of fonts

* Sat Apr 19 2008 Funda Wang <fwang@mandriva.org> 1.0-0.20080419.1mdv2009.0
+ Revision: 195818
- New snapshot of font

* Sun Mar 16 2008 Funda Wang <fwang@mandriva.org> 1.0-0.20080316.1mdv2008.1
+ Revision: 188158
- New snapshot of fonts

  + Thierry Vignaud <tv@mandriva.org>
    - fix no-buildroot-tag

* Sat Feb 09 2008 Funda Wang <fwang@mandriva.org> 1.0-0.20080209.1mdv2008.1
+ Revision: 164469
- New snapshot of font

* Fri Jan 25 2008 Funda Wang <fwang@mandriva.org> 1.0-0.20080124.1mdv2008.1
+ Revision: 157808
- New snapshot

* Sat Dec 29 2007 Funda Wang <fwang@mandriva.org> 1.0-0.20071229.1mdv2008.1
+ Revision: 139168
- New snapshot at 20071229

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Dec 16 2007 Funda Wang <fwang@mandriva.org> 1.0-0.20071215.1mdv2008.1
+ Revision: 120494
- New snapshot at 20071215

* Sun Dec 02 2007 Funda Wang <fwang@mandriva.org> 1.0-0.20071202.1mdv2008.1
+ Revision: 114418
- New snapshot

* Fri Nov 23 2007 Funda Wang <fwang@mandriva.org> 1.0-0.20071123.1mdv2008.1
+ Revision: 111600
- New snapshot
- fix description

* Wed Nov 14 2007 Funda Wang <fwang@mandriva.org> 1.0-0.20071114.1mdv2008.1
+ Revision: 108776
- New snapshot at 20071114

* Sun Nov 04 2007 Funda Wang <fwang@mandriva.org> 1.0-0.20071103.1mdv2008.1
+ Revision: 105573
- New snapshot of fonts

* Sun Oct 28 2007 Funda Wang <fwang@mandriva.org> 1.0-0.20071028.1mdv2008.1
+ Revision: 102824
- New snapshot of fonts
- install fonts.alias

* Mon Oct 22 2007 Funda Wang <fwang@mandriva.org> 1.0-0.20071022.1mdv2008.1
+ Revision: 101125
- New snapshot at 20071022
- New snapshot of fonts

* Fri Oct 12 2007 Funda Wang <fwang@mandriva.org> 1.0-0.20071013.1mdv2008.1
+ Revision: 97777
- New snapshot at 20071013

* Tue Sep 11 2007 Funda Wang <fwang@mandriva.org> 1.0-0.20070911.1mdv2008.0
+ Revision: 84362
- New snapshot of x11-font-wqy-bitmapfont

* Sat Sep 01 2007 Funda Wang <fwang@mandriva.org> 1.0-0.20070901.1mdv2008.0
+ Revision: 77328
- New snapshot at 20070901

* Sat Aug 04 2007 Funda Wang <fwang@mandriva.org> 1.0-0.20070804.1mdv2008.0
+ Revision: 58898
- New snapshot at 070804

* Fri Jul 06 2007 Funda Wang <fwang@mandriva.org> 1.0-0.20070706.1mdv2008.0
+ Revision: 49023
- New snapshot

* Thu Jul 05 2007 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 1.0-0.20070617.3mdv2008.0
+ Revision: 48757
- normalize fontpath.d symlink name (based on pkg name)

* Thu Jul 05 2007 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 1.0-0.20070617.2mdv2008.0
+ Revision: 48700
- fontpath.d conversion (#31756)

* Sun Jun 17 2007 Funda Wang <fwang@mandriva.org> 1.0-0.20070617.1mdv2008.0
+ Revision: 40507
- New snapshot

* Sun May 20 2007 Funda Wang <fwang@mandriva.org> 1.0-0.20070520.1mdv2008.0
+ Revision: 28840
- Rediff patch1
- New upstream snapshot

* Tue May 01 2007 Funda Wang <fwang@mandriva.org> 1.0-0.20070501.1mdv2008.0
+ Revision: 19896
- new snapshot.
- new snapshot at 20070424

* Wed Apr 18 2007 Funda Wang <fwang@mandriva.org> 1.0-0.20070417.1mdv2008.0
+ Revision: 14316
- New snapshot at 20070417.


* Sat Apr 07 2007 Funda Wang <fundawang@mandriva.org> 1.0-0.20070406.1mdv2007.1
+ Revision: 151202
- new snapshot.
- Active CJK ExtA characters.
- new snapshot at 20070403.

* Fri Mar 09 2007 Funda Wang <fundawang@mandriva.org> 1.0-0.20070308.1mdv2007.1
+ Revision: 138650
- corrected tarball name.
- new snapshot at 20070308 equal 0.8.

* Tue Feb 27 2007 Thierry Vignaud <tvignaud@mandriva.com> 1.0-0.20070222.1mdv2007.1
+ Revision: 126253
- Import x11-font-wqy-bitmapfont

* Fri Feb 23 2007 Funda Wang <fundawang@gmail.com> 1.0-0.20070222.1mdv2007.1
- New snapshot on 20070222

* Thu Feb 08 2007 Funda Wang <fundawang@gmail.com> 1.0-0.20070208.1mdv2007.1
- New snapshot on 20070208
- gunzip the fonts to improve the speed
- Adopt to the new build script of upstream package

* Mon Sep 18 2006 Funda Wang <fundawang@gmail.com> 1.0-0.20060916.2mdv2007.0
- Fix post and preun scripts

* Mon Sep 18 2006 Funda Wang <fundawang@gmail.com> 1.0-0.20060916.1mdv2007.0
- New snapshot on 20060916
- No more additional fontconfig needed.

* Thu Jul 20 2006 Funda Wang <fundawang@gmail.com> 1.0-0.20060819.1mdv2007.0
- New snapshot on 20060819
- adopt to the dir change of x11-fonts (/usr/share)

* Mon Jun 05 2006 Funda Wang <fundawang@gmail.com> 0.7.0-1mdv2007.0
- First Mandriva package

