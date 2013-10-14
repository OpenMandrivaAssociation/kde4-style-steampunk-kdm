Summary:	"SteampunK Powered Linux" KDM theme
Name:		kde4-style-steampunk-kdm
Version:	3.0
Release:	1
License:	Creative Commons Attribution-ShareAlike
Group:		Graphical desktop/KDE
Url:		http://kde-look.org/content/show.php?content=142139
Source:		http://sites.google.com/site/binaryinspiration/download/SPL_KDM.tar.gz
Requires:	kdm >= 2:4.10
BuildRequires:	kde4-macros
BuildArch:	noarch

%description
This package contains the "SteampunK Powered Linux" theme for KDM.

%files
%{_kde_appsdir}/kdm/themes/SteampunK

#----------------------------------------------------------------------------

%prep
%setup -q -c
find . -type f | xargs chmod 0644

%build
# nothing

%install
mkdir -p %{buildroot}%{_kde_appsdir}/kdm/themes/

cp -r SteampunK %{buildroot}%{_kde_appsdir}/kdm/themes/

