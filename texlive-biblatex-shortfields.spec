Name:		texlive-biblatex-shortfields
Version:	45858
Release:	1
Summary:	Use short forms of fields with BibLaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-shortfields
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-shortfields.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-shortfields.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The BibLaTeX package provides shortseries and shortjournal
field, but the default styles don't use them. It also provides
a mechanism to print the equivalence between short forms of
fields and long fields (\printbiblist), but this mechanism does
not allow to mix between different type of short fields, for
example, between short forms of journal title and short forms
of series titles. This package provides a solution to these two
problems: If a shortjournal field is defined, it prints it
instead of the \journal field. If a shortseries field is
defined, it prints it instead of the \series field. It provides
a \printbibshortfields command to print a list of the sort
forms of the fields. This list also includes the claves defined
with the biblatex-claves package version 1.2 or later.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/biblatex-shortfields
%doc %{_texmfdistdir}/doc/latex/biblatex-shortfields

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
