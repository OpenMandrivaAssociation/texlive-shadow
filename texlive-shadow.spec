# revision 20312
# category Package
# catalog-ctan /macros/latex/contrib/shadow
# catalog-date 2010-11-01 13:35:24 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-shadow
Version:	20101101
Release:	6
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
%{_texmfdistdir}/tex/latex/shadow/shadow.sty
%doc %{_texmfdistdir}/doc/latex/shadow/shadow-doc.pdf
%doc %{_texmfdistdir}/doc/latex/shadow/shadow-doc.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20101101-2
+ Revision: 755978
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20101101-1
+ Revision: 719522
- texlive-shadow
- texlive-shadow
- texlive-shadow
- texlive-shadow

