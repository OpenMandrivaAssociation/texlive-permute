Name:		texlive-permute
Version:	15878
Release:	2
Summary:	Support for symmetric groups
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/permute
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/permute.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/permute.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/permute.source.r%{version}.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
