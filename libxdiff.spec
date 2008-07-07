%define	major 0
%define	libname %mklibname xdiff %{major}
%define develname %mklibname xdiff -d

Summary:	Create diffs/patches for text/binary files
Name:		libxdiff
Version:	0.22
Release:	%mkrel 3
License:	LGPL
Group:		System/Libraries
URL:		http://www.xmailserver.org/xdiff-lib.html
Source0:	http://www.xmailserver.org/libxdiff-%{version}.tar.gz
Patch0:		am-fixes.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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

%setup -q
%patch0 -p0

%build
%serverbuild
autoreconf -fis

%configure2_5x \
    --with-pic \
    --disable-rpath

%make

%install
rm -rf %{buildroot}

%makeinstall_std

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun	-n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog
%{_libdir}/*.so.*

%files -n %{develname}
%defattr(-,root,root)
%{_includedir}/*.h
%{_libdir}/*.so
%{_libdir}/*.*a
%{_mandir}/man3/xdiff.3*
