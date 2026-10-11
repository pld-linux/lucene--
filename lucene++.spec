Summary:	A high-performance, full-featured text search engine written in C++
Summary(pl.UTF-8):	Bardzo wydajny, w pełni funkcjonalny silnik wyszukiwania pełnotekstowego w C++
Name:		lucene++
Version:	3.0.9
Release:	2
License:	Apache v2.0 or LGPLv3+
Group:		Libraries
#Source0Download: https://github.com/luceneplusplus/LucenePlusPlus/tags
Source0:	https://github.com/luceneplusplus/LucenePlusPlus/archive/rel_%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	33da6751de47523e22e7a1beebd78c29
Patch0:		boost-1.85.patch
Patch1:		%{name}-boost-asio-update.patch
Patch2:		%{name}-swap-typos.patch
Patch3:		%{name}-c++17.patch
URL:		https://github.com/luceneplusplus/LucenePlusPlus
BuildRequires:	boost-devel
BuildRequires:	cmake >= 3.5
BuildRequires:	libstdc++-devel >= 6:7
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRequires:	subversion
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An up to date C++ port of the popular Java Lucene library, a
high-performance, full-featured text search engine.

%description -l pl.UTF-8
Port do aktualnego C++ popularnej biblioteki Javy Lucene - bardzo
wydajnego, w pełni funkcjonalnego silnika wyszukiwania
pełnotekstowego.

%package devel
Summary:	Development files for lucene++
Summary(pl.UTF-8):	Pliki programistyczne lucene++
Group:		Development/Libraries
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	libstdc++-devel >= 6:7

%description devel
Development files for lucene++, a high-performance, full-featured text
search engine written in C++

%description devel -l pl.UTF-8
Pliki programistyczne lucene++ - bardzo wydajnego, w pełni
funkcjonalnego silnika wyszukiwania pełnotekstowego.

%prep
%setup -q -n LucenePlusPlus-rel_%{version}
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1

%build
mkdir -p build
cd build
# .pc file generation expects relative CMAKE_INSTALL_LIBDIR
%cmake .. \
	-DCMAKE_INSTALL_LIBDIR:PATH=%{_lib} \
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
%{_libdir}/liblucene++.so.*.*.*
%ghost %{_libdir}/liblucene++.so.0
%{_libdir}/liblucene++-contrib.so.*.*.*
%ghost %{_libdir}/liblucene++-contrib.so.0

%files devel
%defattr(644,root,root,755)
%{_libdir}/liblucene++.so
%{_libdir}/liblucene++-contrib.so
%{_includedir}/lucene++
%{_pkgconfigdir}/liblucene++.pc
%{_pkgconfigdir}/liblucene++-contrib.pc
%{_libdir}/cmake/liblucene++
%{_libdir}/cmake/liblucene++-contrib
