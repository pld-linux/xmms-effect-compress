Summary:	Volume Compression (normalizer) for XMMS
Summary(pl):	Kompresja g³o¶no¶ci (normalizacja) dla XMMS
Name:		xmms-effect-compress
Version:	1.0
Release:	0
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://trikuare.cx/~magenta/projects/xmms-compress-%{version}.tar.gz
URL:		http://trikuare.cx/~magenta/projects/xmms-compress.html
BuildRequires:	xmms-devel
Requires:	xmms
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description

%description -l pl

%prep
%setup -q -n xmms-compress-%{version}

%build
%{__make} \
	COMMON_CFLAGS="%{rpmcflags} -ffast-math `glib-config --cflags`"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/`%{_bindir}/xmms-config --effect-plugin-dir`/
install libcompress.so \
	$RPM_BUILD_ROOT/`%{_bindir}/xmms-config	--effect-plugin-dir`/libcompress.so

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc  README
%attr(755,root,root) %{_libdir}/xmms/*/*.so
