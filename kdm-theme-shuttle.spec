
%define		_theme		shuttle

Summary:	Shuttle KDM theme
Summary(pl.UTF-8):   Motyw KDM Shuttle
Name:		kdm-theme-%{_theme}
Version:	01
Release:	2
License:	GPL
Group:		X11/Amusements
Source0:	http://www.kde-look.org/content/files/25503-%{_theme}.tar.gz
# Source0-md5:	29a9c1c9f9903cb8dd1b0044d60d484e
Patch0:		%{name}-pl.patch
URL:		http://www.kde-look.org/content/show.php?content=25503
Requires:	kdebase-desktop >= 9:3.2.0
Requires:	kdm >= 9:3.4.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Shuttle KDM Theme.

%description -l pl.UTF-8
Motyw KDM Shuttle.

%prep
%setup -q -c
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/apps/kdm/themes/%{_theme}

install %{_theme}/*.{desktop,jpg,png,xml} $RPM_BUILD_ROOT%{_datadir}/apps/kdm/themes/%{_theme}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/apps/kdm/themes/%{_theme}
