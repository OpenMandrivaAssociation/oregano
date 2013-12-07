Summary:	A GUI to simulate electronic circuit
Name:		oregano
Version:	0.70
Release:	3
License:	GPLv2+
Group:		Graphics
Url:		https://github.com/marc-lorber/oregano
Source0:	%{name}-%{version}.tar.gz
Patch0:		oregano-0.70-sfmt.patch
Patch1:		oregano-0.70-linkage.patch
Patch2:		oregano-automake-1.13.patch
BuildRequires:	gettext
BuildRequires:	gnome-common
BuildRequires:	intltool
BuildRequires:	perl-XML-Parser
BuildRequires:	rarian
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(gtksourceview-2.0)
BuildRequires:	pkgconfig(libglade-2.0)
BuildRequires:	pkgconfig(libgnomecanvas-2.0)
BuildRequires:	pkgconfig(libgnomeprintui-2.2)
BuildRequires:	pkgconfig(libgnomeui-2.0)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(xpm)

%description
Oregano is an application for schematic capture and simulation of
electrical circuits. For the actual simulation, Oregano acts as a
front-end for SPICE, which is more or less the industry standard for
circuit simulation.

%prep
%setup -q
%apply_patches

%build
./autogen.sh
%configure2_5x
%make

%install
%makeinstall_std

mkdir -p %{buildroot}%{_iconsdir}/hicolor/scalable/apps
cp data/mime/gnome-oregano.svg %{buildroot}%{_iconsdir}/hicolor/scalable/apps/gnome-oregano.svg
perl -pi -e 's,gnome-oregano.svg,gnome-oregano,g' %{buildroot}%{_datadir}/applications/%{name}.desktop

rm -rf %{buildroot}%{_datadir}/mime/{XMLnamespaces,generic-icons,globs,globs2,icons,magic,mime.cache,treemagic,types,aliases,subclasses}
rm -rf %{buildroot}%{_datadir}/mime/application/*.xml

%find_lang %{name} --with-gnome

%files -f %{name}.lang
%doc AUTHORS
%{_bindir}/*
%{_datadir}/oregano
%{_datadir}/applications/*
%{_iconsdir}/hicolor/scalable/apps/gnome-oregano.svg
%{_datadir}/mime/packages/*.xml

