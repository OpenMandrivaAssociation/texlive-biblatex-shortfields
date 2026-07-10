%global tl_name biblatex-shortfields
%global tl_revision 45858

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0.1
Release:	%{tl_revision}.1
Summary:	Use short forms of fields with BibLaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-contrib/biblatex-shortfields
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-shortfields.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-shortfields.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The BibLaTeX package provides shortseries and shortjournal field, but
the default styles don't use them. It also provides a mechanism to print
the equivalence between short forms of fields and long fields
(\printbiblist), but this mechanism does not allow to mix between
different type of short fields, for example, between short forms of
journal title and short forms of series titles. This package provides a
solution to these two problems: If a shortjournal field is defined, it
prints it instead of the \journal field. If a shortseries field is
defined, it prints it instead of the \series field. It provides a
\printbibshortfields command to print a list of the sort forms of the
fields. This list also includes the claves defined with the biblatex-
claves package version 1.2 or later.

