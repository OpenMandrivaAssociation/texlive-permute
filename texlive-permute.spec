Name:		texlive-permute
Version:	20070112
Release:	1
Summary:	Support for symmetric groups
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/permute
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/permute.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/permute.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/permute.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
A package for symmetric groups, allowing you to input, output,
and calculate with them.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
