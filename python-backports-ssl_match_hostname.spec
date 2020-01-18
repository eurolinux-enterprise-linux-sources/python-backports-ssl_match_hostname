%global module_name backports.ssl_match_hostname
%global alphatag a3
%global fullversion %{version}%{alphatag}

Name:           python-backports-ssl_match_hostname
Version:        3.2
Release:        0.3.%{alphatag}%{?dist}
Summary:        The ssl.match_hostname() function from Python 3.2

# Webpages claim MIT but the code is cut-and-paste from Python source code
License:        Python
URL:            https://bitbucket.org/brandon/backports.ssl_match_hostname
Source0:        http://pypi.python.org/packages/source/b/backports.ssl_match_hostname/backports.ssl_match_hostname-%{fullversion}.tar.gz
# From the upstream scm
Patch0:         ssl_match_hostname-issue12000.patch
# Slightly modified version of patch against python3.2+
# http://bugs.python.org/issue17980#msg189525
Patch1:         00183-cve-2013-2099-fix-ssl-match_hostname-dos.patch

BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  python-setuptools

%description
The Secure Sockets layer is only actually secure if you check the hostname in
the certificate returned by the server to which you are connecting, and verify
that it matches to hostname that you are trying to reach.

But the matching logic, defined in RFC2818, can be a bit tricky to implement on
your own. So the ssl package in the Standard Library of Python 3.2 now includes
a match_hostname() function for performing this check instead of requiring
every application to implement the check separately.

This backport brings match_hostname() to users of earlier versions of Python.
The actual code inside comes verbatim from Python 3.2.


%prep
%setup -qn %{module_name}-%{fullversion}
%patch0 -p1
%patch1 -p1
mv src/backports/ssl_match_hostname/README.txt ./


%build
python setup.py build


%install
python setup.py install --skip-build --root %{buildroot}

 
%files
%doc README.txt
%{python_sitelib}/*


%changelog
* Mon May 20 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 3.2-0.3.a3
- Add patch for CVE 2013-2099 https://bugzilla.redhat.com/show_bug.cgi?id=963260

* Tue Feb 05 2013 Ian Weller <iweller@redhat.com> - 3.2-0.2.a3
- Fix Python issue 12000

* Fri Dec 07 2012 Ian Weller <iweller@redhat.com> - 3.2-0.1.a3
- Initial package build
