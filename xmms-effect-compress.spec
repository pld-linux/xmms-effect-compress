Summary:	Volume Compression (normalizer) for XMMS
Summary(pl):	Kompresja g³o¶no¶ci (normalizacja) dla XMMS
Name:		xmms-effect-compress
Version:	1.1
Release:	2
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://trikuare.cx/~magenta/projects/xmms-compress-%{version}.tar.gz
URL:		http://trikuare.cx/~magenta/projects/xmms-compress.html
BuildRequires:	xmms-devel
Requires:	xmms
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_xmms_plugin_dir	%(xmms-config --effect-plugin-dir)

%description
xmms-compress is a simple dynamic range compressor for XMMS.
Technically it's not really a compressor, but a volume normalizer, but
the end result is the same as having a compressor with a very long
attack and decay.

%description -l pl
xmms-compress jest prostym, dynamicznym kompresorem g³o¶no¶ci dla XMMS.
Formalnie nie jest prawdziwym kompresorem g³o¶no¶ci, a raczej
normalizatorem g³o¶no¶ci, ale efekt koñcowy jest taki sam, jak dla
kompresora z bardzo d³ugim narastaniem i opadaniem.

%prep
%setup -q -n xmms-compress-%{version}

%build
%{__make} \
	CC=%{__cc} \
	CFLAGS="%{rpmcflags} -Wall `xmms-config --cflags`"

%install
rm -rf $RPM_BUILD_ROOT

install -D libcompress.so \
	$RPM_BUILD_ROOT%{_xmms_plugin_dir}/libcompress.so

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO ChangeLog
%attr(755,root,root) %{_xmms_plugin_dir}/*.so
