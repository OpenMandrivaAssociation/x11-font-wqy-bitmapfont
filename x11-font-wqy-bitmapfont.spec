%define origname wqy-bitmapfont
%define version 1.0.0
%define betaver RC1

Name:	x11-font-%{origname}
Version:	%{version}
Release:	%mkrel -c %betaver 2
Summary:	WenQuanYi Bitmap Song
Group:	System/Fonts/X11 bitmap
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL:	http://www.wenq.org
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
