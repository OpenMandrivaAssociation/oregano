%define	name	oregano
%define	version	0.69.0

Summary:	A GUI to simulate electronic circuit
Name: 		%{name}
Version: 	%{version}
Release: 	%mkrel 2
License: 	GPLv2+
Group: 		Graphics

BuildRequires:	freetype2-devel
BuildRequires:	gettext
BuildRequires:	libcairo-devel
BuildRequires:	libglade2.0-devel
BuildRequires:	gnomeui2-devel
BuildRequires:	libgnomeprintui-devel
BuildRequires:	gtksourceview1-devel
BuildRequires:	perl-XML-Parser
BuildRequires:	scrollkeeper
BuildRequires:	texinfo
BuildRequires:	xpm-devel
BuildRequires:	gnome-common
BuildRequires:  scons

Requires(post):		desktop-file-utils
Requires(postun):	desktop-file-utils


Source: 	https://gforge.lug.fi.uba.ar/frs/download.php/62/%{name}-%{version}.tar.gz
URL:		http://oregano.gforge.lug.fi.uba.ar/index.php	
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

%description
Oregano is an application for schematic capture and simulation of
electrical circuits. For the actual simulation, Oregano acts as a
front-end for SPICE, which is more or less the industry standard for
circuit simulation.

%prep
%setup -q

%build
perl -pi -e 's/update-mime-database/true/g' SConstruct
scons PREFIX=%{_prefix}/

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
scons  DESTDIR=$RPM_BUILD_ROOT/ PREFIX=%{_prefix}/  install 
mkdir -p %{buildroot}%{_iconsdir}/hicolor/scalable/apps
mv %{buildroot}%{_datadir}/pixmaps/gnome-oregano.svg %{buildroot}%{_iconsdir}/hicolor/scalable/apps/gnome-oregano.svg
perl -pi -e 's,gnome-oregano.svg,gnome-oregano,g' %{buildroot}%{_datadir}/applications/%{name}.desktop

%{find_lang} %{name}

rm -rf $RPM_BUILD_ROOT/%_datadir/mime/{XMLnamespaces,globs,magic,aliases,subclasses}
rm -rf $RPM_BUILD_ROOT/var

%post
%update_menus
%{update_desktop_database}


%postun
%clean_menus
%{clean_desktop_database}


%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-, root, root)
%doc AUTHORS 
%{_bindir}/*
%{_datadir}/mime-info/*
%{_datadir}/oregano
%{_datadir}/applications/*
%{_iconsdir}/hicolor/scalable/apps/gnome-oregano.svg
%{_datadir}/mime/packages/*.xml

