Summary:	A GUI to simulate electronic circuit
Name:		oregano
Version:	0.70
Release:	1
License:	GPLv2+
Group:		Graphics
URL:		https://github.com/marc-lorber/oregano
Source:		%{name}-%{version}.tar.gz
Patch0:		oregano-0.70-sfmt.patch
Patch1:		oregano-0.70-linkage.patch
Patch2:		oregano-automake-1.13.patch
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libglade-2.0)
BuildRequires:	pkgconfig(libgnomeui-2.0)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(libgnomecanvas-2.0)
BuildRequires:	pkgconfig(gtksourceview-2.0)
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(libgnomeprintui-2.2)
BuildRequires:	pkgconfig(xpm)

BuildRequires:	gettext
BuildRequires:	intltool
BuildRequires:	perl-XML-Parser
BuildRequires:	scrollkeeper
BuildRequires:	gnome-common

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


%changelog
* Mon Sep  17 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru>
+ Commit: 968bb84
- Add patch to fix format is not a string literal build error
  
* Mon Sep  17 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru>
+ Commit: f972330
- Add intltool to BuildRequires
  
* Mon Sep  17 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru>
+ Commit: 6ea9c4e
- New version 0.70, convert BR to pkgconfig style, no longer uses scons
  
  
