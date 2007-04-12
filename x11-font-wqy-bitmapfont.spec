%define origname wqy-bitmapfont
%define version 1.0
%define snapshotdate 20070406

Name:	x11-font-%{origname}
Version:	%{version}
Release:	%mkrel -c %snapshotdate 1
Summary:	WenQuanYi Bitmap Song
Group:	System/Fonts/X11 bitmap
URL:	http://www.wenq.org
Source0:	http://heanet.dl.sourceforge.net/sourceforge/wqy/%{origname}-bdf-all-nightly_build.tar.gz
License:	GPL
BuildRoot:	%{_tmppath}/%{name}-root
BuildArch:	noarch
BuildRequires:	bdftopcf

Requires(pre):	mkfontdir, mkfontscale, chkfontpath
Requires(postun):	mkfontdir, mkfontscale, chkfontpath
Requires:	fontconfig

%description
The Wen Quan Yi bitmap font includes complete CJK Unified 
Ideograph (U4E00 - U9FA5) glyphs at four different sizes 
(9pt-12X12 pixel, 10pt-13X13 pixel, 11pt-15X15 pixel, 
12pt-16x16 pixel) and two weights (medium and bold). 
Use of this bitmap font for on-screen display of Chinese 
(traditional and simplified) in web pages and elsewhere 
eliminates the annoying "blurring" problems caused by 
the high stroke density of many Chinese characters and 
insufficient "hinting" of anti-aliased Chinese fonts. 
This font also provides bitmap glyphs for Japanese 
Hiragana (U3040 - U309F), Katakana (U30A0 - U30FF) 
and for Korean Hangul (UAC00 - UD7A3).

%prep
%setup -q -n %{origname}-all -a 0

%build
%make wqyv1

%install
rm -fr %buildroot

install -d %{buildroot}/%_datadir/fonts/wqy
install -m 0755 *.pcf %{buildroot}/%_datadir/fonts/wqy

%post
mkfontscale %_datadir/fonts/wqy
mkfontdir %_datadir/fonts/wqy
[ -x %{_bindir}/fc-cache ] && %{_bindir}/fc-cache
if [ "$1" = "1" ]; then
	chkfontpath -a %_datadir/fonts/wqy
fi

%preun
if [ "$1" = "0" ]; then
	chkfontpath -r %_datadir/fonts/wqy
fi

%postun
mkfontscale %_datadir/fonts/wqy
mkfontdir %_datadir/fonts/wqy
[ -x %{_bindir}/fc-cache ] && %{_bindir}/fc-cache 

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README ChangeLog AUTHORS COPYING
%_datadir/fonts/wqy/*.pcf


