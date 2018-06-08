FROM centos:6.7  
  
MAINTAINER Miguel Gila <miguel.gila@cscs.ch>  
LABEL Description="This image is used to test WLCG WN workloads via Docker"
Vendor="CSCS" Version="20151214" URL="https://github.com/miguelgila/docker-
wlcg_wn"  
  
ADD http://repository.egi.eu/sw/production/cas/1/current/repo-files/EGI-
trustanchors.repo /etc/yum.repos.d/  
  
VOLUME /cvmfs  
  
RUN yum -y install https://ecsft.cern.ch/dist/cvmfs/cvmfs-release/cvmfs-
release-2-5.noarch.rpm \  
http://linuxsoft.cern.ch/wlcg/sl6/x86_64/wlcg-repo-1.0.0-1.el6.noarch.rpm \  
http://emisoft.web.cern.ch/emisoft/dist/EMI/3/sl6/x86_64/base/emi-
release-3.0.0-2.el6.noarch.rpm  
  
RUN yum -y install epel-release cvmfs HEP_OSlibs_SL6 wlcg-voms-alice wlcg-
voms-atlas wlcg-voms-lhcb \  
wlcg-voms-cms wlcg-voms-ops autofs ca-policy-egi-core iputils  
  
RUN yum -y groupinstall 'Development Tools'  
  
RUN yum -y install emi-slurm-client emi-wn emi-glexec_wn \  
globus-proxy-utils globus-gass-copy-progs \  
boost-devel cyrus-sasl-devel e2fsprogs-devel expat-devel \  
file-devel giflib-devel gmp-devel gpm-devel kernel-devel libacl-devel \  
libattr-devel libcap-devel libcom_err-devel libcurl-devel libdrm-devel \  
libdrm-devel libstdc++-devel libuuid-devel libxml2-devel lockdev-devel \  
libjpeg-turbo-devel openldap-devel netpbm-devel popt-devel python-devel \  
rpm-devel tcl-devel tk-devel openssh-clients PyXML  
  
# Install extra RPMs present in emi3wn-latest reference  
RUN yum -y install a1_grid_env bouncycastle bouncycastle-mail canl-c canl-java
ca-policy-egi-core CGSI-gSOAP classads cleanup-grid-accounts davix-libs
dcache-srmclient dcap dcap-devel dcap-libs dcap-tunnel-gsi dcap-tunnel-krb
dcap-tunnel-ssl dcap-tunnel-telnet dpm dpm-devel dpm-libs dpm-perl dpm-python
editline emi.amga.amga-cli emi-release emi.saga-adapter.context-cpp emi.saga-
adapter.isn-common emi.saga-adapter.isn-cpp emi.saga-adapter.sd-cpp emi-
version emi-wn fetch-crl gfal gfal2 gfal2-all gfal2-devel gfal2-doc
gfal2-plugin-dcap gfal2-plugin-file gfal2-plugin-gridftp gfal2-plugin-http
gfal2-plugin-lfc gfal2-plugin-rfio gfal2-plugin-srm gfal2-plugin-xrootd
gfal2-python gfal2-util gfalFS gfal-python ginfo glite-jobid-api-c glite-lb-
client glite-lb-client-progs glite-lb-common glite-lbjp-common-gss glite-lbjp-
common-trio glite-service-discovery-api-c glite-wms-brokerinfo-access glite-
wms-brokerinfo-access-lib glite-wn-info glite-yaim-clients glite-yaim-core
globus-callout globus-common globus-ftp-client globus-ftp-control globus-gass-
copy globus-gass-copy-progs globus-gass-transfer globus-gsi-callback globus-
gsi-cert-utils globus-gsi-credential globus-gsi-openssl-error globus-gsi-
proxy-core globus-gsi-proxy-ssl globus-gsi-sysconfig globus-gssapi-error
globus-gssapi-gsi globus-gss-assist globus-io globus-openssl-module globus-
proxy-utils globus-xio globus-xio-gsi-driver globus-xio-popen-driver gridftp-
ifce gridsite-libs gsoap is-interface jclassads lcgdm-devel lcgdm-libs lcg-
info lcg-infosites lcg-ManageVOTag lcg-tags lcg-util lcg-util-libs lcg-util-
python lfc lfc-devel lfc-libs lfc-perl lfc-python pugixml python-argparse
SAGA.lsu-cpp.engine srm-ifce uberftp voms voms-api-java3 voms-clients3 voms-
devel xerces-c acpid aic94xx-firmware alsa-utils apr atmel-firmware audit
augeas-libs authconfig b43-fwcutter b43-openfwwf bfa-firmware biosdevname
blktrace bridge-utils busybox ca-policy-lcg ConsoleKit ConsoleKit-libs
cpuspeed crda cryptsetup-luks cryptsetup-luks-libs cyrus-sasl cyrus-sasl-plain
dapl dbus-python dejavu-fonts-common dejavu-lgc-sans-mono-fonts dejavu-sans-
mono-fonts desktop-file-utils device-mapper-event device-mapper-event-libs
device-mapper-persistent-data dhclient dhcp-common dmidecode dmraid dmraid-
events dosfstools e2fsprogs efibootmgr eggdbus eject elfutils elfutils-libs
facter fontpackages-filesystem fping fprintd fprintd-pam gd gpm-libs graphviz
graphviz-tcl grub hal hal-info hal-libs hdparm hiera htop hunspell hunspell-en
infiniband-diags ipmitool iptables-ipv6 ipw2100-firmware ipw2200-firmware
irqbalance ivtv-firmware iw iwl1000-firmware iwl100-firmware iwl3945-firmware
iwl4965-firmware iwl5000-firmware iwl5150-firmware iwl6000-firmware
iwl6000g2a-firmware iwl6050-firmware kernel kernel-devel kernel-devel kexec-
tools keyutils kpartx ksh lcg-CA ledmon libconfuse libcxgb3 libedit libertas-
usb8388-firmware libevent libfprint libibcm libibmad libibumad libipathverbs
libmcrypt libmthca libnes libnl libpcap librdmacm librdmacm-utils librelp
libselinux-ruby libss libtalloc libtdb libtevent libusb1 libXaw libxml2-python
lm_sensors lm_sensors-libs lsof lua-alt-getopt lua-filesystem lua-lxc lvm2
lvm2-libs lxc lxc-libs lzo man-pages man-pages-overrides mdadm microcode_ctl
mlocate mtr munge munge-devel munge-libs mysql-libs nano net-snmp-libs net-
snmp-utils newt newt-python nfs-utils nfs-utils-lib nrpe nsca-client ntp
ntpdate ntsysv numactl OpenIPMI OpenIPMI-libs opensm-libs openssh-server
pam_passwdqc parted pciutils pciutils-libs pcmciautils perl-Class-Accessor
perl-Config-Tiny perl-Math-Calc-Units perl-Nagios-Plugin perl-Params-Validate
pinfo pm-utils polkit postfix postgresql-libs prelink psacct python-ethtool
python-iwlib ql2100-firmware ql2200-firmware ql23xx-firmware ql2400-firmware
ql2500-firmware quota rdate rdma rds-tools readahead redhat-rpm-config rfkill
rng-tools rpcbind rpm-build rrdtool rsync rsyslog-gnutls rsyslog-relp rt61pci-
firmware rt73usb-firmware ruby ruby-augeas rubygem-json rubygems ruby-irb
ruby-libs ruby-rdoc ruby-shadow samba-client samba-common samba-winbind samba-
winbind-clients scl-utils selinux-policy selinux-policy-targeted setserial
setuptool sg3_utils-libs sgpio smartmontools snappy sos strace swig sysstat
system-config-firewall-base system-config-firewall-tui system-config-network-
tui systemtap-runtime tcpdump tcp_wrappers traceroute unzip usbutils usermode
vconfig vim-common vim-enhanced virt-what wget words xdg-utils xorg-x11-drv-
ati-firmware yum-plugin-security yum-plugin-versionlock yum-utils
zd1211-firmware zip  
  
# Update!  
RUN yum -y update  
  
RUN chgrp 496 /usr/sbin/glexec  
RUN chmod 4711 /usr/sbin/glexec  

