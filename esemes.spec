Summary:	Send SMS via Polish GSM operators
Summary(pl):	Program do wysy�ania kr�tkich wiadomo�ci (SMS)
Name:		esemes
Version:	0.11
Release:	1
License:	BSD
Group:		Applications/Communications
Source0:	http://download.berlios.de/sms/%{name}-%{version}.tar.bz2
# Source0-md5:	ce77b7ad8462b8846e4b1eadb9f5b00f
URL:		http://sms.berlios.de/
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRequires:	sed >= 4.0
%pyrequires_eq  python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program sends SMS to mobile phones operaterd by Polish GSM
operators: Era, Plus and Orange.

%description -l pl
Program potrafi wysy�a� wiadomo�ci na telefony sieci Era, Plus oraz
Orange.

%prep
%setup -q

%build
%{__sed} -e -i "s@python2.4@python@g" esemes misc.py

%install
rm -rf $RPM_BUILD_ROOT
install -D %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}
install -d $RPM_BUILD_ROOT%{py_scriptdir}
install *.py $RPM_BUILD_ROOT%{py_scriptdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README*
%attr(755,root,root) %{_bindir}/%{name}
%{py_scriptdir}/*.py
