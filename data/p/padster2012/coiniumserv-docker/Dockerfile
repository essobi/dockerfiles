FROM centos:7  
MAINTAINER The CentOS Project <cloud-ops@centos.org>  
LABEL Vendor="CentOS" \  
License=GPLv2 \  
Version=2.4.6-40  
  
  
RUN yum -y update; yum clean all \  
&& rpm --import
"http://keyserver.ubuntu.com/pks/lookup?op=get&search=0x3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF"
\  
&& yum-config-manager --add-repo http://download.mono-project.com/repo/centos/
\  
&& yum check-update \  
&& yum -y install mono-complete \  
  
RUN yum -y install git; yum clean all \  
  
&& git clone https://github.com/CoiniumServ/CoiniumServ.git
/usr/local/bin/CoiniumServ \  
&& cd /usr/local/bin/CoiniumServ; git submodule init; git submodule update \  
&& ls \  
&& pwd \  
&& cd /usr/local/bin/CoiniumServ/build/release \  
&& ls \  
&& pwd \  
&& sh /usr/local/bin/CoiniumServ/build/release/build.sh  
  
  
EXPOSE 8081  
  
CMD ["mono", "/usr/local/bin/CoiniumServ/build/release/CoiniumServ.exe"]  

