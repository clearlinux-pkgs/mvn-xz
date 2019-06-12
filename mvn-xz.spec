#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-xz
Version  : 1.5
Release  : 1
URL      : https://repo1.maven.org/maven2/org/tukaani/xz/1.5/xz-1.5.jar
Source0  : https://repo1.maven.org/maven2/org/tukaani/xz/1.5/xz-1.5.jar
Source1  : https://repo1.maven.org/maven2/org/tukaani/xz/1.5/xz-1.5.pom
Source2  : https://repo1.maven.org/maven2/org/tukaani/xz/1.6/xz-1.6.jar
Source3  : https://repo1.maven.org/maven2/org/tukaani/xz/1.6/xz-1.6.pom
Source4  : https://repo1.maven.org/maven2/org/tukaani/xz/1.8/xz-1.8.jar
Source5  : https://repo1.maven.org/maven2/org/tukaani/xz/1.8/xz-1.8.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Public-Domain
Requires: mvn-xz-data = %{version}-%{release}

%description
No detailed description available

%package data
Summary: data components for the mvn-xz package.
Group: Data

%description data
data components for the mvn-xz package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/tukaani/xz/1.5
cp %{SOURCE0} %{buildroot}/usr/share/java/.m2/repository/org/tukaani/xz/1.5

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/tukaani/xz/1.5
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/tukaani/xz/1.5

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/tukaani/xz/1.6
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/tukaani/xz/1.6

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/tukaani/xz/1.6
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/org/tukaani/xz/1.6

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/tukaani/xz/1.8
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/org/tukaani/xz/1.8

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/tukaani/xz/1.8
cp %{SOURCE5} %{buildroot}/usr/share/java/.m2/repository/org/tukaani/xz/1.8


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/tukaani/xz/1.5/xz-1.5.jar
/usr/share/java/.m2/repository/org/tukaani/xz/1.5/xz-1.5.pom
/usr/share/java/.m2/repository/org/tukaani/xz/1.6/xz-1.6.jar
/usr/share/java/.m2/repository/org/tukaani/xz/1.6/xz-1.6.pom
/usr/share/java/.m2/repository/org/tukaani/xz/1.8/xz-1.8.jar
/usr/share/java/.m2/repository/org/tukaani/xz/1.8/xz-1.8.pom
