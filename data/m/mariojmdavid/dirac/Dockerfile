# docker build --rm -t dirac .  
FROM centos:7  
LABEL maintainer "Mario David <mariojmdavid@gmail.com>"  
  
ENV DIRAC=/usr/local/dirac  
  
ENV ARC_PLUGIN_PATH=${DIRAC}/Linux_x86_64_glibc-2.17/lib/arc \  
DIRACBIN=${DIRAC}/Linux_x86_64_glibc-2.17/bin \  
DIRACLIB=${DIRAC}/Linux_x86_64_glibc-2.17/lib \  
DIRACPLAT=Linux_x86_64_glibc-2.17 \  
DIRACSCRIPTS=${DIRAC}/scripts \  
DYLD_LIBRARY_PATH=${DIRAC}/Linux_x86_64_glibc-2.17/lib/mysql:/home/Linux_x86_64_glibc-2.17/lib
\  
GFAL_CONFIG_DIR=${DIRAC}/Linux_x86_64_glibc-2.17/etc/gfal2.d \  
GFAL_PLUGIN_DIR=${DIRAC}/Linux_x86_64_glibc-2.17/lib/gfal2-plugins \  
GLOBUS_FTP_CLIENT_IPV6=TRUE \  
GLOBUS_IO_IPV6=TRUE \  
LD_LIBRARY_PATH=${DIRAC}/Linux_x86_64_glibc-2.17/lib/mysql:/home/Linux_x86_64_glibc-2.17/lib
\  
OPENSSL_CONF=/tmp \  
PATH=${DIRAC}/scripts:${DIRAC}/Linux_x86_64_glibc-2.17/bin:${PATH} \  
PYTHONOPTIMIZE=x \  
PYTHONPATH=${DIRAC} \  
PYTHONUNBUFFERED=yes \  
REQUESTS_CA_BUNDLE=/etc/grid-security/certificates \  
RRD_DEFAULT_FONT=${DIRAC}/Linux_x86_64_glibc-2.17/share/rrdtool/fonts/DejaVuSansMono-
Roman.ttf \  
SSL_CERT_DIR=/etc/grid-security/certificates \  
TERMINFO=${DIRAC}/Linux_x86_64_glibc-2.17/share/terminfo:/usr/share/terminfo:/etc/terminfo
\  
X509_CERT_DIR=/etc/grid-security/certificates \  
X509_VOMS_DIR=/etc/grid-security/vomsdir  
  
RUN yum -y update && \  
yum -y install epel-release tar wget && \  
cd /etc/yum.repos.d/ && \  
wget http://www.lip.pt/~david/dirac/EGI.repo && \  
yum -y update && \  
yum -y install \  
ca-certificates \  
ca-policy-egi-core \  
ca-policy-lcg \  
python-pip && \  
yum clean all && \  
cd /etc/grid-security && \  
wget http://www.lip.pt/~david/dirac/voms.tgz && \  
tar zxvf voms.tgz && \  
mkdir -p ${DIRAC} && \  
cd ${DIRAC} && \  
wget -np -O dirac-install \  
https://github.com/DIRACGrid/DIRAC/raw/integration/Core/scripts/dirac-
install.py --no-check-certificate && \  
chmod +x dirac-install && \  
./dirac-install -V egi  
  
WORKDIR /root  
  

