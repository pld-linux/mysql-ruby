#
# Conditional build:
%bcond_without	doc			# don't build ri/rdoc

Summary:	MySQL module for Ruby
Summary(pl.UTF-8):	Moduł MySQL dla języka Ruby
Name:		mysql-ruby
Version:	2.8.2
Release:	14
License:	GPL
Group:		Development/Languages
Source0:	http://tmtm.org/downloads/mysql/ruby/%{name}-%{version}.tar.gz
# Source0-md5:	eb998b89b7e391cffe0a1f84bd426f9b
Patch0:		%{name}-amd64.patch
Patch1:		%{name}-encoding.patch
Patch2:		rbconfig-deprecation.patch
Patch3:		ruby-2.4.patch
URL:		http://www.tmtm.org/mysql/ruby/README.html
BuildRequires:	mysql-devel
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.665
BuildRequires:	ruby >= 1:1.8.6
BuildRequires:	ruby-devel
BuildRequires:	ruby-modules
Provides:	ruby-mysql-library
Conflicts:	ruby-mysql
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MySQL module for Ruby.

%description -l pl.UTF-8
Moduł MySQL dla języka Ruby.

%package rdoc
Summary:	HTML documentation for %{name}
Summary(pl.UTF-8):	Dokumentacja w formacie HTML dla %{name}
Group:		Documentation
Requires:	ruby >= 1:1.8.7-4
BuildArch:	noarch

%description rdoc
HTML documentation for %{name}.

%description rdoc -l pl.UTF-8
Dokumentacja w formacie HTML dla %{name}.

%package ri
Summary:	ri documentation for %{name}
Summary(pl.UTF-8):	Dokumentacja w formacie ri dla %{name}
Group:		Documentation
Requires:	ruby
BuildArch:	noarch

%description ri
ri documentation for %{name}.

%description ri -l pl.UTF-8
Dokumentacji w formacie ri dla %{name}.

%prep
%setup -q
%patch0 -p0
%patch1 -p1
%patch2 -p1
%patch3 -p1

find '(' -name '*~' -o -name '*.orig' ')' -print0 | xargs -0 -r -l512 rm -f

%build
ruby extconf.rb \
	--with-mysql-config

%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -fPIC"

%if %{with doc}
rdoc --ri --op ri
rdoc --op rdoc
rm -r ri/Object
rm ri/created.rid
rm ri/cache.ri
rm ri/page-*.ri
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_ridir},%{ruby_rdocdir}}
%{__make} install \
	archdir=$RPM_BUILD_ROOT%{ruby_vendorarchdir} \
	sitearchdir=$RPM_BUILD_ROOT%{ruby_vendorarchdir}

%if %{with doc}
cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}
cp -a rdoc $RPM_BUILD_ROOT%{ruby_rdocdir}/%{name}-%{version}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README*
%attr(755,root,root) %{ruby_vendorarchdir}/mysql.so

%if %{with doc}
%files rdoc
%defattr(644,root,root,755)
%{ruby_rdocdir}/%{name}-%{version}

%files ri
%defattr(644,root,root,755)
%{ruby_ridir}/Mysql
%{ruby_ridir}/TC_Mysql*
%endif
