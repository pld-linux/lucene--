Summary:	A high-performance, full-featured text search engine written in C++
Name:		lucene++
Version:	3.0.8
Release:	2
License:	Apache v2.0 or LGPLv3+
Group:		Libraries
Source0:	https://github.com/luceneplusplus/LucenePlusPlus/archive/rel_%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	cb9b2e7cb37b7dd68c1e24a65c6eda9d
Patch0:		stdc++.patch
Patch1:		contrib-soversion.patch
Patch2:		config-install.patch
Patch3:		pkgconfig.patch
URL:		https://github.com/luceneplusplus/LucenePlusPlus
BuildRequires:	boost-devel
BuildRequires:	cmake >= 2.8.6
BuildRequires:	pkgconfig
BuildRequires:	subversion
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An up to date C++ port of the popular Java Lucene library, a
high-performance, full-featured text search engine.

%package devel
Summary:	Development files for lucene++
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Development files for lucene++, a high-performance, full-featured text
search engine written in C++

%prep
%setup -q -n LucenePlusPlus-rel_%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
mkdir -p build
cd build
%cmake .. \
	-DENABLE_TEST:BOOL=OFF
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING README* REQUESTS
%{_libdir}/liblucene++.so.0
%{_libdir}/liblucene++.so.*.*.*
%{_libdir}/liblucene++-contrib.so.0
%{_libdir}/liblucene++-contrib.so.*.*.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/lucene++/
%{_libdir}/liblucene++.so
%{_libdir}/liblucene++-contrib.so
%{_pkgconfigdir}/liblucene++.pc
%{_pkgconfigdir}/liblucene++-contrib.pc
%{_libdir}/cmake/liblucene++*.cmake
