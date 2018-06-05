FROM ubuntu:14.04  
WORKDIR /opt  
  
RUN apt-get update && apt-get install -y \  
wget \  
unzip \  
build-essential \  
apt-utils --yes --force-yes \  
openssh-client \  
curl \  
zlib1g-dev \  
libncurses5-dev \  
git  
  
ADD http://download.asperasoft.com/download/sw/ascp-client/3.5.4/ascp-
install-3.5.4.102989-linux-64.sh /opt/  
  
# No https, so verify sha1  
RUN test $(sha1sum /opt/ascp-install-3.5.4.102989-linux-64.sh |cut -f1 -d\ ) =
a99a63a85fee418d16000a1a51cc70b489755957 && \  
sh /opt/ascp-install-3.5.4.102989-linux-64.sh  

