Name:		texlive-shadow
Version:	20190228
Release:	1
Summary:	Shadow boxes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/shadow
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/shadow.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/shadow.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Defines a command \shabox (analgous to \fbox), and supporting
mechanisms.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/shadow
%doc %{_texmfdistdir}/doc/latex/shadow

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
