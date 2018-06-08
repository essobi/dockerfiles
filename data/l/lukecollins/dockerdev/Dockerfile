FROM centos:7  
MAINTAINER "Luke Collins" <your@email.here>  
  
ENV container docker  
  
RUN yum -y swap -- remove fakesystemd -- install systemd systemd-libs  
RUN yum -y update; yum -y clean all; \  
(cd /lib/systemd/system/sysinit.target.wants/; for i in *; do [ $i == systemd-
tmpfiles-setup.service ] || rm -f $i; done); \  
rm -f /lib/systemd/system/multi-user.target.wants/*;\  
rm -f /etc/systemd/system/*.wants/*;\  
rm -f /lib/systemd/system/local-fs.target.wants/*; \  
rm -f /lib/systemd/system/sockets.target.wants/*udev*; \  
rm -f /lib/systemd/system/sockets.target.wants/*initctl*; \  
rm -f /lib/systemd/system/basic.target.wants/*;\  
rm -f /lib/systemd/system/anaconda.target.wants/*;  
VOLUME [ "/sys/fs/cgroup" ]  
RUN yum -y install httpd wget screen sudo time telnet sed tar unzip bzip2
which crontabs man man-pages man-pages-overrides lynx MAKEDEV passwd nano; yum
-y clean all; systemctl enable httpd.service;  
RUN yum -y install net-tools; yum -y clean all;  
RUN cd /tmp; \  
wget http://dl.fedoraproject.org/pub/epel/7/x86_64/e/epel-
release-7-5.noarch.rpm; \  
wget http://rpms.famillecollet.com/enterprise/remi-release-7.rpm; \  
rpm -Uvh epel-release-7*.rpm;\  
rpm -Uvh remi-release-7*.rpm; \  
sed -i "s/enabled=0/enabled=1/g" /etc/yum.repos.d/remi.repo;\  
yum -y install ImageMagick-last ImageMagick-last-libs;  
RUN yum --disablerepo remi-test -y install php php-bcmath php-channel-
phpseclib php-cli php-common php-gd php-gmp php-imap php-intl php-kolab-net-
ldap3 php-ldap php-mbstring php-mcrypt php-mysqlnd php-pdo php-pear php-pear-
Auth-SASL php-pear-Mail-Mime php-pear-Mail-mimeDecode php-pear-Net-IDNA2 php-
pear-Net-LDAP2 php-pear-Net-SMTP php-pear-Net-Sieve php-pear-Net-Socket php-
pecl-apcu php-pecl-igbinary php-pecl-imagick php-pecl-jsonc php-pecl-memcache
php-pecl-memcached php-pecl-mongo php-pecl-msgpack php-pecl-sqlite php-pecl-
zip php-pgsql php-php-gettext php-phpseclib-crypt-aes php-phpseclib-crypt-base
php-phpseclib-crypt-random php-phpseclib-crypt-rijndael php-process php-pspell
php-recode php-soap php-suhosin php-tcpdf php-tcpdf-dejavu-sans-fonts php-tidy
php-xml php-xmlrpc phpMyAdmin;  
RUN yum -y install dovecot dovecot-mysql dovecot-pigeonhole aspell aspell-en
amavisd-new clamav clamav-db clamd fetchmail postfix procmail roundcubemail
spamassassin;  
RUN yum -y install perl-Authen-PAM perl-Class-C3 perl-Class-MOP perl-Compress-
Zlib perl-Data-OptList perl-Data-Uniqid perl-Date-Manip perl-DBD-MySQL perl-
DBD-Pg perl-Devel-GlobalDestruction perl-Email-Date-Format perl-Email-Valid
perl-ExtUtils-CBuilder perl-File-Copy-Recursive perl-Git perl-IO-Compress-Base
perl-IO-Compress-Zlib perl-IO-Tee perl-IO-Tty perl-List-MoreUtils perl-
LockFile-Simple perl-Log-Dispatch perl-Log-Dispatch-FileRotate perl-Log-
Log4perl perl-Mail-IMAPClient perl-Mail-Sender perl-Mail-Sendmail perl-MIME-
Charset perl-MIME-EncWords perl-MIME-Lite perl-MIME-Types perl-Module-Build
perl-Module-Pluggable perl-Moose perl-MRO-Compat perl-NTLM perl-Package-
DeprecationManager perl-Package-Stash perl-Package-Stash-XS perl-Params-Util
perl-Params-Validate perl-Parse-RecDescent perl-Sub-Exporter perl-Sub-Install
perl-Sub-Name perl-Sub-Uplevel perl-Task-Weaken perl-TermReadKey perl-Test-
Exception perl-Test-Pod perl-Test-Simple perl-Text-Iconv perl-Try-Tiny perl-
Unicode-String perl-XML-DOM perl-XML-LibXML perl-XML-Parser perl-XML-RegExp
perl-XML-SAX perl-YAML-Syck;  
RUN yum -y install openssh openssh-clients openssh-server openssl-devel;  
RUN yum -y install mod_evasive mutt mysql mod_ssl mysql-libs mysql-server
mlocate quota traceroute git subversion htop jwhois finger jre libproxy
libproxy-bin libproxy-python logrotate lsof yum-utils zip;  
RUN yum -y install acl aic94xx-firmware alsa-lib alsa-utils apr-util-ldap;  
RUN yum -y install at atmel-firmware attr audit authconfig b43-openfwwf bc
bfa-firmware bind bind-chroot bind-libs bind-utils;  
RUN yum -y install bridge-utils btrfs-progs centos-indexhtml checkpolicy
compat-mysql51 ConsoleKit ConsoleKit-libs coreutils-libs crda cyrus-sasl
cyrus-sasl-devel cyrus-sasl-plain cyrus-sasl-sql dash db4 db4-cxx db4-devel
db4-utils dbus dbus-glib dbus-python dejavu-lgc-sans-mono-fonts device-mapper
device-mapper-event device-mapper-event-libs device-mapper-libs device-mapper-
persistent-data dhclient dhcp-common dmidecode e2fsprogs ed efibootmgr eggdbus
fftw gamin gamin-python GConf2 glibc gpm-libs groff grub grubby imapsync ipset
ipw2100-firmware ipw2200-firmware ivtv-firmware iw iwl1000-firmware
iwl3945-firmware iwl4965-firmware iwl5000-firmware iwl5150-firmware
iwl6000-firmware iwl6050-firmware kbd kbd-misc lcms-libs libcgroup libertas-
usb8388-firmware libevent-last libgsf libicu-last libIDL libmemcached-last-
libs libnih libudev;  
RUN yum -y install libusb libwmf libXdmcp libxkbfile libXtst lvm2 lvm2-libs m4
mailx mdadm mesa-dri1-drivers mesa-dri-drivers mesa-dri-filesystem mesa-
private-llvm mingetty module-init-tools mtr nc nmap nss-softokn-freebl ntpdate
ntsysv offlineimap ORBit2 pakchois parted pciutils pciutils-libs plymouth-
core-libs plymouth-scripts polkit procps;  
RUN yum -y install psacct python-ethtool python-inotify python-iwlib python-
setproctitle python-setuptools ql2100-firmware ql2200-firmware ql23xx-firmware
ql2400-firmware ql2500-firmware rsyslog rt61pci-firmware rt73usb-firmware
selinux-policy selinux-policy-targeted setserial setuptool sgml-common
smartmontools ssmtp strace system-config-firewall-base system-config-firewall-
tui system-config-network-tui tcpdump tcp_wrappers-libs tcsh;  
RUN yum -y install usermode util-linux-ng vconfig vim-common vim-enhanced vim-
filesystem wbm-virtual-server wbt-virtual-server-theme;  
RUN yum -y install xkeyboard-config xorg-x11-drv-ati-firmware xorg-x11-fonts-
misc xorg-x11-xauth xorg-x11-xkb-utils xz-lzma-compat zd1211-firmware;  
RUN rpm -ivh http://pkg.cloudflare.com/cloudflare-release-latest.el7.rpm; yum
-y clean all; yum -y update; yum -y install mod_cloudflare;  
  
EXPOSE 80  
EXPOSE 443  
CMD ["/usr/sbin/init"]  
  

