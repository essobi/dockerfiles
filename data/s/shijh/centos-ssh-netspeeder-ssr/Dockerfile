#
=============================================================================  
# shijh666/centos-ssh  
#  
# CentOS latest - SSH / SSR / Net Speeder.  
#  
#
=============================================================================  
FROM centos:latest  
  
MAINTAINER shijh666  
  
#
-----------------------------------------------------------------------------  
# Set default environment variables  
#
-----------------------------------------------------------------------------  
ENV SSHD_PORT 22  
ENV SSR_PORT 1000  
ENV SVD_PORT 1080  
ENV DEFAULT_USERNAME root  
ENV DEFAULT_PASSWORD password  
  
#
-----------------------------------------------------------------------------  
# Copy files into container  
#
-----------------------------------------------------------------------------  
ADD etc /etc/  
ADD root /root/  
  
#
-----------------------------------------------------------------------------  
# Install necessary packages  
#
-----------------------------------------------------------------------------  
RUN yum update -y && \  
yum install -y \  
gcc \  
libnet \  
libnet-devel \  
libpcap \  
libpcap-devel \  
openssh-server \  
openssh-clients \  
python-setuptools \  
git && \  
yum clean all  
  
#
-----------------------------------------------------------------------------  
# Configure SSH  
#
-----------------------------------------------------------------------------  
RUN sed -i \  
-e 's/^#\?Port 22/Port '$SSHD_PORT'/g' \  
-e 's/^#\?PermitRootLogin.*/PermitRootLogin yes/g' \  
-e 's/^#\?UsePAM.*/UsePAM no/g' \  
/etc/ssh/sshd_config  
  
RUN ssh-keygen -q -t rsa -b 2048 -f /etc/ssh/ssh_host_rsa_key -N ''  
RUN ssh-keygen -q -t ecdsa -f /etc/ssh/ssh_host_ecdsa_key -N ''  
RUN ssh-keygen -q -t dsa -f /etc/ssh/ssh_host_ed25519_key -N ''  
  
EXPOSE $SSHD_PORT  
  
#
-----------------------------------------------------------------------------  
# Install NetSpeeder  
#
-----------------------------------------------------------------------------  
RUN cd /root/ && \  
git clone -b master https://github.com/snooda/net-speeder.git && \  
cd net-speeder/ && \  
sh build.sh && \  
cp -nf net_speeder /usr/bin/ && \  
cd /root/ && \  
rm -rf net-speeder/  
  
#
-----------------------------------------------------------------------------  
# Install ShadowsocksR  
#
-----------------------------------------------------------------------------  
RUN cd /root/ && \  
git clone -b manyuser https://github.com/shadowsocksr/shadowsocksr.git && \  
cp -nf shadowsocksr/config.json shadowsocksr/shadowsocks/user-config.json  
  
EXPOSE $SSR_PORT  
  
#
-----------------------------------------------------------------------------  
# Install supervisor  
#
-----------------------------------------------------------------------------  
RUN easy_install supervisor  
  
EXPOSE $SVD_PORT  
  
CMD sh /root/sys_cfg.sh; \  
supervisord -c /etc/supervisord.conf  

