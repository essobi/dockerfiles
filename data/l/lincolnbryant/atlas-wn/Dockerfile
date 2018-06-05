FROM opensciencegrid/osg-wn:3.3-el6  
  
LABEL maintainer "lincolnb@uchicago.edu"  
  
# The all-important HEP_OS_Libs  
RUN yum localinstall -y
http://linuxsoft.cern.ch/cern/slc6X/x86_64/yum/extras/HEP_OSlibs_SL6-1.0.16-0.el6.x86_64.rpm  
  
# Big pile of RPMs that jobs may use. This was essentially pulled off of a
worker node at MWT2.  
# This should be cleaned up and moved into appropriate areas below. Delete if
they aren't necessary.  
RUN yum install -y apr apr-util attr augeas-libs authconfig authconfig-gtk
avahi-glib binutils-devel cairo-devel cdparanoia-libs compat-xcb-util
cryptsetup-luks cryptsetup-luks-libs cyrus-sasl cyrus-sasl-devel cyrus-sasl-
plain dbus-devel docbook-dtds ecryptfs-utils elfutils elfutils-devel elfutils-
libelf-devel elfutils-libs expat-devel flex gdk-pixbuf2-devel ghostscript
ghostscript-fonts glx-utils gmp-devel gstreamer-plugins-base gtk2-devel
gtk2-engines iso-codes jasper-devel json-c keyutils lapack lsof mysql-libs
neon newt newt-devel nspr-devel nss-devel nss-softokn-devel nss-softokn-
freebl-devel nss-util-devel openldap-devel openmotif-devel openssl-devel
pakchois pam-devel pango-devel pciutils pciutils-libs portreserve rarian
rarian-compat readline-devel satyr sharutils slang slang-devel smp_utils swig
tcl-devel tk-devel trousers udisks ustr-devel xdg-utils xml-common xmlrpc-c
xmlrpc-c-client zenity  
  
#  
# Moving all of the needed utilities down here onto their own lines  
#  
# Libraries  
RUN yum install -y lapack-devel lcms-devel lcms-libs libaio-devel libart_lgpl
libattr-devel libblkid-devel libbonobo libbonoboui libcanberra libcanberra-
gtk2 libcap-devel libcap-ng-devel libcdio libconfuse libcroco libcurl-devel
libcurl-devel libdmx libedit-devel libevent libevent-devel libevent-doc
libevent-headers libglade2 libgnome libgnomecanvas libgnomeui libgsf
libgssglue libgssglue-devel libgudev1 libICE-devel libidn-devel libjpeg-turbo-
devel libmcpp libmng libnl libnl libnl-devel liboil libpcap libreport
libreport-compat libreport-filesystem libreport-gtk libreport-newt libreport-
plugin-reportuploader libreport-plugin-rhtsupport libreport-python librsvg2
libselinux-ruby libsemanage-devel libSM-devel libtar libtdb libtheora libtiff-
devel libtirpc libudev-devel libusb1 libuser-python libuv libuv-devel
libvisual libwnck libXaw libXcomposite-devel libXcursor-devel libXi-devel
libXinerama-devel libxkbfile libXmu-devel libXp-devel libXrandr-devel libXres
libXt-devel libXv libXvMC libXxf86dga libXxf86misc gsl gsl-devel net-snmp-libs
gd blas blas-devel sqlite-devel  
  
# Compilers  
RUN yum install -y compat-gcc-34 compat-gcc-34-c++ compat-gcc-34-g77 gdb
glib2-devel glibc-utils gcc-gfortran  
  
# Python  
RUN yum install -y pycairo pygtk2 pygtk2-libglade python-babel python-
backports python-backports-ssl_match_hostname python-chardet python-dateutil
python-devel python-ethtool python-flask python-jinja2-26 python-magic python-
markupsafe python-meh python-nose python-pip python-requests python-setuptools
python-simplejson python-six python-urllib3 python-virtualenv python-werkzeug
pyxf86config cracklib-python newt-python  
  
# Perl  
RUN yum install -y pcre-devel perl-Archive-Tar perl-IO-Zlib perl-Package-
Constants perl-Time-HiRes perl-XML-Parser perl-XML-Simple pixman-devel  
  
#X11 misc  
RUN yum install -y xorg-x11-apps xorg-x11-utils xorg-x11-xauth qt qt-devel qt-
sqlite qt-x11 -y gnuplot gnuplot-common  
  
# Globus misc  
RUN yum install -y globus-gram-client globus-gram-protocol globus-rsl  
  
# Tools and shells  
RUN yum install -y zip nc dmidecode rsync unzip subversion ksh  

