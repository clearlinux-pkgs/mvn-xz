#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-xz
Version  : 1.5
Release  : 4
URL      : https://repo1.maven.org/maven2/org/tukaani/xz/1.5/xz-1.5.jar
Source0  : https://repo1.maven.org/maven2/org/tukaani/xz/1.5/xz-1.5.jar
Source1  : https://repo1.maven.org/maven2/org/tukaani/xz/1.0/xz-1.0.jar
Source2  : https://repo1.maven.org/maven2/org/tukaani/xz/1.0/xz-1.0.pom
Source3  : https://repo1.maven.org/maven2/org/tukaani/xz/1.2/xz-1.2.jar
Source4  : https://repo1.maven.org/maven2/org/tukaani/xz/1.2/xz-1.2.pom
Source5  : https://repo1.maven.org/maven2/org/tukaani/xz/1.4/xz-1.4.jar
Source6  : https://repo1.maven.org/maven2/org/tukaani/xz/1.4/xz-1.4.pom
Source7  : https://repo1.maven.org/maven2/org/tukaani/xz/1.5/xz-1.5.pom
Source8  : https://repo1.maven.org/maven2/org/tukaani/xz/1.6/xz-1.6.jar
Source9  : https://repo1.maven.org/maven2/org/tukaani/xz/1.6/xz-1.6.pom
Source10  : https://repo1.maven.org/maven2/org/tukaani/xz/1.8/xz-1.8.jar
Source11  : https://repo1.maven.org/maven2/org/tukaani/xz/1.8/xz-1.8.pom
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
cp %{SOURCE0} %{buildroot}/usr/share/java/.m2/repository/org/tukaani/xz/1.5/xz-1.5.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/tukaani/xz/1.0
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/tukaani/xz/1.0/xz-1.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/tukaani/xz/1.0
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/tukaani/xz/1.0/xz-1.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/tukaani/xz/1.2
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/org/tukaani/xz/1.2/xz-1.2.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/tukaani/xz/1.2
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/org/tukaani/xz/1.2/xz-1.2.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/tukaani/xz/1.4
cp %{SOURCE5} %{buildroot}/usr/share/java/.m2/repository/org/tukaani/xz/1.4/xz-1.4.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/tukaani/xz/1.4
cp %{SOURCE6} %{buildroot}/usr/share/java/.m2/repository/org/tukaani/xz/1.4/xz-1.4.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/tukaani/xz/1.5
cp %{SOURCE7} %{buildroot}/usr/share/java/.m2/repository/org/tukaani/xz/1.5/xz-1.5.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/tukaani/xz/1.6
cp %{SOURCE8} %{buildroot}/usr/share/java/.m2/repository/org/tukaani/xz/1.6/xz-1.6.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/tukaani/xz/1.6
cp %{SOURCE9} %{buildroot}/usr/share/java/.m2/repository/org/tukaani/xz/1.6/xz-1.6.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/tukaani/xz/1.8
cp %{SOURCE10} %{buildroot}/usr/share/java/.m2/repository/org/tukaani/xz/1.8/xz-1.8.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/tukaani/xz/1.8
cp %{SOURCE11} %{buildroot}/usr/share/java/.m2/repository/org/tukaani/xz/1.8/xz-1.8.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/tukaani/xz/1.0/xz-1.0.jar
/usr/share/java/.m2/repository/org/tukaani/xz/1.0/xz-1.0.pom
/usr/share/java/.m2/repository/org/tukaani/xz/1.2/xz-1.2.jar
/usr/share/java/.m2/repository/org/tukaani/xz/1.2/xz-1.2.pom
/usr/share/java/.m2/repository/org/tukaani/xz/1.4/xz-1.4.jar
/usr/share/java/.m2/repository/org/tukaani/xz/1.4/xz-1.4.pom
/usr/share/java/.m2/repository/org/tukaani/xz/1.5/xz-1.5.jar
/usr/share/java/.m2/repository/org/tukaani/xz/1.5/xz-1.5.pom
/usr/share/java/.m2/repository/org/tukaani/xz/1.6/xz-1.6.jar
/usr/share/java/.m2/repository/org/tukaani/xz/1.6/xz-1.6.pom
/usr/share/java/.m2/repository/org/tukaani/xz/1.8/xz-1.8.jar
/usr/share/java/.m2/repository/org/tukaani/xz/1.8/xz-1.8.pom
