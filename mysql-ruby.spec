%define	ruby_archdir	%(ruby -r rbconfig -e 'print Config::CONFIG["archdir"]')
%define	tarname			mysql-ruby
Summary:	MySQL module for Ruby
Summary(pl):	Modu³ MySQL dla Ruby
Name:		ruby-Mysql
Version:	2.4.5
Release:	2
License:	GPL
Group:		Development/Languages
Source0:	http://www.tmtm.org/mysql/ruby/%{tarname}-%{version}.tar.gz
# Source0-md5:	345292e3f09f60f446fc36e5e841548f
URL:		http://www.tmtm.org/mysql/ruby/
BuildRequires:	mysql-devel
BuildRequires:	ruby
BuildRequires:	ruby-devel
Requires:	ruby
Obsoletes:	ruby-mysql
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MySQL module for Ruby.

%description -l pl
Modu³ MySQL dla Ruby.

%prep
%setup -q -n %{tarname}-%{version}

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
#install -d $RPM_BUILD_ROOT{%{ruby_archdir},%{ruby_ridir}}
install -d $RPM_BUILD_ROOT%{ruby_archdir}

%{__make} install \
	archdir=$RPM_BUILD_ROOT%{ruby_archdir} \
	sitearchdir=$RPM_BUILD_ROOT%{ruby_archdir}

#cp -a ri/ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README* rdoc
%attr(755,root,root) %{ruby_archdir}/mysql.so
