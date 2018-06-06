FROM codered/centos-minimal:7  
  
MAINTAINER Ronan Gill <ronan.gill@code.red>  
  
# enable proxy  
#RUN echo "proxy=http://192.168.1.178:8000" >> /etc/yum.conf  
  
RUN yum update -y && \  
yum install -y audit-libs basesystem bash binutils bzip2-libs ca-certificates
centos-release chkconfig coreutils cpio cracklib cracklib-dicts curl cyrus-
sasl-lib dbus-libs device-mapper device-mapper-libs diffutils elfutils-libelf
expat fakesystemd file file-libs filesystem findutils gawk gdbm git glib2
glibc glibc-common gmp gnupg2 gpgme grep groff-base gzip hardlink htop info
iproute iptables iptables-services iputils keyutils-libs kmod-libs kpartx
krb5-libs less libacl libassuan libattr libblkid libcap libcap-ng libcom_err
libcroco libcurl libdb libdb-utils libffi libgcc libgcrypt libgomp libgpg-
error libidn libmnl libmount libnetfilter_conntrack libnfnetlink libpwquality
libselinux libsemanage libsepol libssh2 libstdc++ libtasn1 libunistring
libuser libutempter libuuid libverto libxml2 lua ncurses ncurses-base ncurses-
libs nspr nss nss-softokn nss-softokn-freebl nss-sysinit nss-tools nss-util
openldap openssl-libs p11-kit p11-kit-trust pam pcre pinentry pkgconfig popt
procps-ng pth pygpgme pyliblzma python python-iniparse python-libs python-
pycurl python-urlgrabber pyxattr readline rootfiles rpm rpm-build-libs rpm-
libs rpm-python sed setup shadow-utils shared-mime-info sqlite systemd-libs
tzdata ustr util-linux unzip vim-minimal wget which xz xz-libs yum yum-
metadata-parser zlib && \  
yum update -y && yum clean all && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
# remove proxy if used above  
#RUN sed -i '/proxy=http/,+1 d' /etc/yum.conf  
  
ENV LANG en_GB.UTF-8  
ENV LANGUAGE $LANG  
ENV LC_ALL $LANG  
  
CMD /bin/bash  

