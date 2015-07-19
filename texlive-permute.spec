# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/permute
# catalog-date 2007-01-12 23:55:10 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-permute
Version:	20070112
Release:	10
Summary:	Support for symmetric groups
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/permute
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/permute.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/permute.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/permute.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A package for symmetric groups, allowing you to input, output,
and calculate with them.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/permute/permute.sty
%doc %{_texmfdistdir}/doc/latex/permute/permute.pdf
#- source
%doc %{_texmfdistdir}/source/latex/permute/permute.dtx
%doc %{_texmfdistdir}/source/latex/permute/permute.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20070112-2
+ Revision: 754810
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20070112-1
+ Revision: 719235
- texlive-permute
- texlive-permute
- texlive-permute
- texlive-permute

