# Author: Ensky Lin  
# Date: 07/08/2015  
FROM ubuntu:trusty  
MAINTAINER enskylin "enskylin@gmail.com"  
RUN echo "==> Upgrade source" && \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get -y upgrade && \  
\  
echo "==> Install Unoconv" && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get install -y unoconv imagemagick && \  
\  
echo "==> Install supervisor" && \  
apt-get install -y supervisor && \  
\  
echo "==> Install Fonts" && \  
echo ttf-mscorefonts-installer msttcorefonts/accepted-mscorefonts-eula select
true | debconf-set-selections && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get install -y \  
fonts-arphic-ukai fonts-arphic-uming fonts-ipafont-mincho fonts-ipafont-gothic
fonts-unfonts-core \  
language-pack-zh-hant \  
ttf-wqy-zenhei && \  
\  
echo "==> Clean up" && \  
apt-get clean && \  
apt-get autoremove -y && \  
rm -rf /var/lib/apt/lists  
  
COPY libreofficed.conf /etc/supervisor/conf.d/libreofficed.conf  
COPY restart.sh /restart.sh  
  
CMD ["/usr/bin/supervisord"]  
ENV LC_ALL zh_TW.UTF-8  
  

