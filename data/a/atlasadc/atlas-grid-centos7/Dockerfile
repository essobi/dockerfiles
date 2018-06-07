FROM atlasadc/atlas-grid-centos7-base:latest  
ENV UMD_REL_VER 4.1.3-1.el7.centos  
LABEL maintainer="Alessandro.DeSalvo@roma1.infn.it"  
  
RUN yum -y groupinstall "Development Tools" && \  
yum -y install vim-minimal vim-enhanced man-db wget ntp nfs-utils git perl
perl-Data-Dumper automake autoconf libtool gcc gcc-c++ glibc flex make autofs
&& \  
#  
yum -y install time alsa-lib alsa-lib audit-libs autoconf automake \  
bzip2-devel bzip2-libs compat-db compat-db compat-db42 compat-db42 \  
compat-db43 compat-db43 compat-expat1 compat-expat1 compat-glibc \  
compat-glibc-headers compat-libf2c-34 compat-libf2c-34 compat-libgfortran-41 \  
compat-libgfortran-41 compat-libstdc++-33 compat-libstdc++-33 \  
compat-libtermcap compat-libtermcap compat-openldap compat-openldap \  
compat-readline5 cracklib cyrus-sasl-lib db4 db4-cxx db4-devel e2fsprogs-libs
\  
elfutils-libelf expat fontconfig fontconfig-devel freetype freetype-devel \  
freetype-devel gamin gdbm giflib giflib glib2 glibc glibc-devel glibmm24 \  
gmp keyutils-libs krb5-libs libICE libICE libSM libSM libX11 libX11-devel \  
libX11-devel libXau libXau-devel libXau-devel libXcursor libXdamage \  
libXdamage-devel libXdamage-devel libXdmcp libXdmcp libXdmcp-devel \  
libXdmcp-devel libXext libXext-devel libXext-devel libXfixes libXfixes-devel \  
libXfixes-devel libXft libXft-devel libXi libXinerama libXmu libXmu libXp \  
libXp libXpm libXpm libXpm-devel libXrandr libXrender libXrender-devel \  
libXt libXt libXtst libXtst libXxf86vm libXxf86vm libXxf86vm-devel \  
libXxf86vm-devel libaio libcom_err libdrm libdrm-devel libdrm-devel libgcc \  
libgfortran libgfortran libidn libjpeg-turbo libpciaccess libpng libpng-devel
\  
libpng-devel libselinux libsepol libsigc++20 libstdc++ libtiff libtool \  
libtool-ltdl libtool-ltdl libuuid libuuid-devel libuuid-devel libxcb \  
libxcb-devel libxcb-devel libxml2 libxml2-devel libxml2-devel \  
libxslt mesa-dri-drivers mesa-dri-drivers mesa-dri-filesystem \  
mesa-dri-filesystem mesa-dri1-drivers mesa-libGL mesa-libGL mesa-libGL-devel \  
mesa-libGL-devel mesa-libGLU mesa-libGLU mesa-libGLU-devel mesa-libGLU-devel \  
mesa-private-llvm mesa-private-llvm ncurses-devel ncurses-libs nspr nss \  
nss-softokn nss-softokn-freebl nss-util openldap openmotif openmotif \  
openmotif22 openmotif22 openssl openssl098e pam perl-CGI perl-ExtUtils-Embed \  
perl-ExtUtils-MakeMaker perl-ExtUtils-ParseXS perl-Test-Harness perl-devel \  
procmail readline sqlite tcl tcsh tk tk xorg-x11-proto-devel zlib zlib-devel \  
zsh Updating expat libblkid libuuid nss nss-sysinit \  
nss-tools nss-util util-linux-ng && \  
#  
# Additional packages  
yum -y install binutils-devel python-devel && \  
yum -y install
http://repository.egi.eu/sw/production/umd/4/centos7/x86_64/updates/umd-
release-${UMD_REL_VER}.noarch.rpm && \  
yum -y install gfal2-all gfal2-util xrootd-client lcg-util && \  
yum -y install java-1.8.0-openjdk lsof && \  
#  
# Kerberos  
yum -y install krb5-libs krb5-workstation && \  
# Final update and creation of the package list  
yum -y update && \  
rpm -qa > /var/lib/package-list && \  
# Remove unuseful stuff  
rm -fr /var/lib/yum/* /var/cache/yum/* /usr/share/doc/* /boot/*  
  
COPY krb5.conf /etc  
# Create the dbus machine-id  
RUN dbus-uuidgen > /var/lib/dbus/machine-id  
  
# Timestamp  
RUN echo `date +%Y%m%d%H%M%S` > /docker-creation-date && \  
echo "export CDATE_DOCKER=\"`cat /docker-creation-date`\"" >
/etc/profile.d/container-date.sh && \  
echo "setenv CDATE_DOCKER \"`cat /docker-creation-date`\"" >
/etc/profile.d/container-date.csh  

