FROM rodrigotsuru/wasnd-docker:8.5.5  
MAINTAINER Rodrigo Tsuru <caixapostal@gmail.com>  
# Add EPEL repository to install davfs2  
RUN wget http://download.fedoraproject.org/pub/epel/6/x86_64/epel-
release-6-8.noarch.rpm && \  
rpm -ivh epel-release-6-8.noarch.rpm  
#Bug https://docs.oracle.com/cd/E52668_01/E69348/html/uek4-czc_xmc_xt.html  
RUN touch /var/lib/rpm/*  
RUN rpm --rebuilddb; yum install -y yum-plugin-ovl  
RUN yum install -y unzip \  
davfs2 \  
libaio.i686 \  
libaio.x86_64 \  
pam.i686 \  
pam.x86_64 \  
libstdc++.i686 \  
libstdc++.x86_64 \  
compat-libstdc++-33.i686 \  
compat-libstdc++-33.x86_64 \  
glibc.i686 \  
glibc.x86_64 \  
libgcc.i686 \  
libgcc.x86_64 \  
sg3_utils \  
kernel-devel \  
gcc-c++ \  
wget \  
file \  
ksh.x86_64 \  
patch \  
ntpd \  
gcc \  
python-setuptools \  
megatools  
RUN easy_install supervisor  
COPY configs/supervisord.conf /etc/supervisord.conf  
RUN cd /tmp && \  
megadl
https://mega.nz/#\\!MwNR3RhC\\!bfhZZDRaLhj6XsvDL45qSQw1b-TkCks_2CJmnELBq7k &&
\  
unzip WSRR_8.5.5_TRIAL_LINUX_ON_INTEL_M.zip -d WSRR && \  
rm WSRR_8.5.5_TRIAL_LINUX_ON_INTEL_M.zip && \  
cd WSRR && \  
tar xvzf wsrrtrial.dvd.8550.linux.x86.tar.gz && \  
rm wsrrtrial.dvd.8550.linux.x86.tar.gz  
COPY install.xml /tmp/install.xml  
RUN /opt/IBM/InstallationManager/eclipse/tools/imcl input /tmp/install.xml
-acceptLicense -showProgress -masterPasswordFile /tmp/masterpw.txt
-secureStorageFile /tmp/secure.dat && \  
rm -Rf /tmp/install-package  

