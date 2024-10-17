%define	major 1
%define	libname %mklibname xdiff %{major}
%define develname %mklibname xdiff -d

Summary:	Create diffs/patches for text/binary files
Name:		libxdiff
Version:	1.0
Release:	1
License:	LGPL
Group:		System/Libraries
URL:		https://www.xmailserver.org/xdiff-lib.html
Source0:	https://github.com/spotrh/libxdiff/archive/refs/tags/%{version}/%{name}-%{version}.tar.gz
Patch0:	libxdiff-1.0-big-endian.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool

%description
The LibXDiff library implements basic and yet complete functionalities
to create file differences/patches to both binary and text files. It
uses memory files as file abstraction to achieve both performance and
portability. For binary files, it implements (with some modification)
the algorithm described in "File System Support for Delta Compression"
by Joshua P. MacDonald. For text files, it follows directives described
in "An O(ND) Difference Algorithm and Its Variations" by Eugene W.
Myers. Memory files used by the library are basically a collection of
buffers that store the file content.

%package -n	%{libname}
Summary:	Shared libxdiff library
Group:		System/Libraries

%description -n	%{libname}
The LibXDiff library implements basic and yet complete functionalities
to create file differences/patches to both binary and text files. It
uses memory files as file abstraction to achieve both performance and
portability. For binary files, it implements (with some modification)
the algorithm described in "File System Support for Delta Compression"
by Joshua P. MacDonald. For text files, it follows directives described
in "An O(ND) Difference Algorithm and Its Variations" by Eugene W.
Myers. Memory files used by the library are basically a collection of
buffers that store the file content

%package -n	%{develname}
Summary:	Header files for libxdiff library
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{develname}
The LibXDiff library implements basic and yet complete functionalities
to create file differences/patches to both binary and text files. It
uses memory files as file abstraction to achieve both performance and
portability. For binary files, it implements (with some modification)
the algorithm described in "File System Support for Delta Compression"
by Joshua P. MacDonald. For text files, it follows directives described
in "An O(ND) Difference Algorithm and Its Variations" by Eugene W.
Myers. Memory files used by the library are basically a collection of
buffers that store the file content

Header files for libxdiff library.

%prep

%setup -q -n %{name}-%{version}
%autopatch -p1

%build
%configure --disable-static

%make_build

%install
%make_install

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun	-n %{libname} -p /sbin/ldconfig
%endif

%files -n %{libname}
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog
%doc AUTHORS COPYING ChangeLog
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%{_includedir}/xdiff
%{_libdir}/*.so
%{_libdir}/pkgconfig/libxdiff.pc


%changelog
* Sat Aug 20 2011 Oden Eriksson <oeriksson@mandriva.com> 0.23-1mdv2012.0
+ Revision: 695869
- 0.23

* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.22-5mdv2011.0
+ Revision: 620239
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.22-4mdv2010.0
+ Revision: 429849
- rebuild

* Mon Jul 07 2008 Oden Eriksson <oeriksson@mandriva.com> 0.22-3mdv2009.0
+ Revision: 232376
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Fri Dec 21 2007 Olivier Blin <blino@mandriva.org> 0.22-2mdv2008.1
+ Revision: 136571
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Sep 04 2007 Oden Eriksson <oeriksson@mandriva.com> 0.22-2mdv2008.0
+ Revision: 79447
- fix deps

* Tue Sep 04 2007 Oden Eriksson <oeriksson@mandriva.com> 0.22-1mdv2008.0
+ Revision: 79366
- Import libxdiff



* Tue Sep 04 2007 Oden Eriksson <oeriksson@mandriva.com> 0.22-1mdv2008.0
- initial Mandriva package (opensuse import)
