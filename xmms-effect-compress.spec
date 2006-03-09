Summary:	Volume Compression (normalizer) for XMMS
Summary(pl):	Kompresja g³o¶no¶ci (normalizacja) dla XMMS
Name:		xmms-effect-compress
Version:	1.1
Release:	3
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://trikuare.cx/~magenta/projects/xmms-compress-%{version}.tar.gz
# Source0-md5:	4c2fb5fbad5207c48b948a0eb769e44b
URL:		http://trikuare.cx/~magenta/projects/xmms-compress.html
BuildRequires:	rpmbuild(macros) >= 1.125
BuildRequires:	xmms-devel
Requires:	xmms
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -Wall `xmms-config --cflags`"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{xmms_effect_plugindir}

install libcompress.so $RPM_BUILD_ROOT%{xmms_effect_plugindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO ChangeLog
%attr(755,root,root) %{xmms_effect_plugindir}/*.so
