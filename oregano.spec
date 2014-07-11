Summary:	A GUI to simulate electronic circuit
Name:		oregano
Version:	0.82
Release:	3
License:	GPLv2+
Group:		Graphics
Url:		https://github.com/marc-lorber/oregano
Source0:	%{name}-%{version}.tar.gz
Patch0:		oregano-0.70-sfmt.patch
Patch1:		oregano-0.70-linkage.patch
BuildRequires:	gettext
BuildRequires:	gnome-common
BuildRequires:	intltool
BuildRequires:	perl-XML-Parser
BuildRequires:	rarian
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(xpm)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(goocanvas-2.0)
BuildRequires:  pkgconfig(gtksourceview-3.0)

%description
Oregano is an application for schematic capture and simulation of
electrical circuits. For the actual simulation, Oregano acts as a
front-end for SPICE, which is more or less the industry standard for
circuit simulation.

%prep
%setup -q
%apply_patches

# this is a hack for glib2.0 >= 2.31.0
sed -i -e 's/-DGTK_DISABLE_DEPRECATED//g' \
        ./src/Makefile.* \
        ./src/*/Makefile.*


%build
./autogen.sh
%configure2_5x --disable-update-mimedb
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
%{_datadir}/glib-2.0/schemas/apps.oregano.gschema.xml

