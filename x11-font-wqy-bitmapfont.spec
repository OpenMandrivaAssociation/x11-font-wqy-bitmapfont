%define origname wqy-bitmapfont
%define version 1.0
%define snapshotdate 20070520

# fwang: whether we are using west part or east part of the source.
# check here: http://wenq.org/index.cgi?BitmapSong#nightly_build_NB
%define use_west_part 0

# fwang: whether we should use cjk parts only
# if yes, wqy bitmapsong could be treated as monospace font
%define cjk_part_only 1

Name:	x11-font-%{origname}
Version:	%{version}
Release:	%mkrel -c %snapshotdate 1
Summary:	WenQuanYi Bitmap Song
Group:	System/Fonts/X11 bitmap
URL:	http://www.wenq.org
Source0:	http://heanet.dl.sourceforge.net/sourceforge/wqy/%{origname}-bdf-gb18030-nightly_build.tar.gz
Source1:	http://heanet.dl.sourceforge.net/sourceforge/wqy/%{origname}-bdf-all-nightly_build.tar.gz
# fwang: The original Makefile doesn't fit fontconfig and qt3
#Patch0:	%{origname}-Makefile-cjk-range.patch
Patch1:	%{origname}-fontconfig-rule-kill-minimal-fontsize.patch
Patch2:	%{origname}-fontconfig-rule-fit-monospace.patch
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
%if %use_west_part
%setup -q -T -n %{origname}-all -b 1
%else
%setup -q -T -n %{origname}-gb18030 -b 0
%endif
#%patch0 -p0
%patch1 -p0
%if %cjk_part_only
%patch2 -p0
%endif

%build
%if %cjk_part_only
%make cjk
%else
%make wqyv1
%endif

%install
rm -fr %buildroot

install -d %{buildroot}/%_datadir/fonts/wqy
install -m 0644 *.pcf %{buildroot}/%_datadir/fonts/wqy

install -d %{buildroot}/%_sysconfdir/fonts/conf.d/
install -m 0644 *.conf %{buildroot}/%_sysconfdir/fonts/conf.d

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
%_sysconfdir/fonts/conf.d/*.conf
