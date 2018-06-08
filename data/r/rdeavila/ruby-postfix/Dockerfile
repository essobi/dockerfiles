FROM mailtop/passenger-ruby24  
  
MAINTAINER Rodrigo de Avila <rodrigo@syonet.com>  
  
# Update, upgrade, install, clean...  
RUN apt-get -qq update && \  
apt-get -qq upgrade -y -o Dpkg::Options::="--force-confold" && \  
apt-get -qq -y dist-upgrade && \  
apt-get -qq -y install && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get -qq -y install curl \  
jq \  
opendkim \  
opendkim-tools \  
postfix \  
sasl2-bin \  
software-properties-common \  
syslog-ng && \  
apt-get -qq clean && \  
apt-get -qq autoclean && \  
apt-get -qq -y autoremove && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# ForeGo  
RUN curl -fsSL -o forego-stable-linux-amd64.tgz
https://bin.equinox.io/c/ekMN3bCZFUn/forego-stable-linux-amd64.tgz && \  
tar xf forego-stable-linux-amd64.tgz && \  
mv forego /usr/bin && \  
rm forego-stable-linux-amd64.tgz  
  
# Upgrade RubyGems  
RUN gem update --system  
  
# Add files  
ADD assets/install.sh /opt/install.sh  
  
# Run  
CMD /opt/install.sh; \  
forego start  

