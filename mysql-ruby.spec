%define	ruby_archdir	%(ruby -r rbconfig -e 'print Config::CONFIG["archdir"]')
%define	ruby_ridir	%(ruby -r rbconfig -e 'include Config; print File.join(CONFIG["datadir"], "ri", CONFIG["ruby_version"], "system")')
Summary:	MySQL module for Ruby
Summary(pl):	Modu� MySQL dla Ruby
Name:		mysql-ruby
Version:	2.5.1
Release:	2
License:	GPL
Group:		Development/Languages
Source0:	http://www.tmtm.org/mysql/ruby/%{name}-%{version}.tar.gz
# Source0-md5:	9c7026eb38ec8252de8bc89c5f263208
URL:		http://www.tmtm.org/mysql/ruby/
BuildRequires:	mysql-devel
BuildRequires:	ruby
BuildRequires:	ruby-devel
Requires:	ruby
Obsoletes:	ruby-mysql
Conflicts:	ruby-mysql
Obsoletes:	ruby-Mysql
Provides:	ruby-mysql-library
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MySQL module for Ruby.

%description -l pl
Modu� MySQL dla Ruby.

%prep
%setup -q

%build
ruby extconf.rb \
	--with-mysql-dir=%{_prefix}
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -fPIC"

rdoc -o rdoc
rdoc --ri -o ri

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_archdir},%{ruby_ridir}}

%{__make} install \
	archdir=$RPM_BUILD_ROOT%{ruby_archdir} \
	sitearchdir=$RPM_BUILD_ROOT%{ruby_archdir}

cp -a ri/ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README* rdoc
%attr(755,root,root) %{ruby_archdir}/mysql.so
%{ruby_ridir}/*
