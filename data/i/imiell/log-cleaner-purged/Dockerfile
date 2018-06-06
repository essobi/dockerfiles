FROM imiell/log-cleaner  
RUN apt-get purge -y ucf xkb-data vim-tiny vim-common perl whiptail ureadahead
python3 python3-minimal python3.4-minimal python3.4 cron rsyslog plymouth net-
tools netcat-openbsd ntpdate makedev mime-support netbase logrotate lockfile-
progs module-init-tools cpio less apt-utils busybox-initramfs anacron
keyboard-configuration bzip2 file init-system-helpers initramfs-tools-bin
iproute2 iputils-ping isc-dhcp-common klibc-utils adduser kmod debconf-i18n
libapt-inst1.5:amd64 libtext-wrapi18n-perl libtext-iconv-perl libtext-
charwidth-perl libtasn1-6:amd64 libsqlite3-0:amd64 liblockfile-bin
libssl1.0.0:amd64 libudev1:amd64 libprocps3:amd64 libpopt0:amd64
libpng12-0:amd64 libp11-kit0:amd64 libnih1:amd64 libmpdec2:amd64
libmagic1:amd64 libnewt0.52:amd64 liblocale-gettext-perl libklibc
libkmod2:amd64 libjson0:amd64 libjson-c2:amd64 libgpg-error0:amd64
libgdbm3:amd64 libfribidi0:amd64 libexpat1:amd64 libffi6:amd64 libestr0
libdrm2:amd64 libcap2-bin libbsd0:amd64  
RUN apt-get autoremove -y  
RUN apt-get clean  

