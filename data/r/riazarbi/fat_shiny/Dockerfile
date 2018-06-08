FROM rocker/shiny  
  
MAINTAINER Riaz Arbi  
  
# INSTALL DEPENDENCIES  
RUN \  
echo 'DPkg::Post-Invoke {"/bin/rm -f /var/cache/apt/archives/*.deb ||
true";};' | tee /etc/apt/apt.conf.d/no-cache && \  
apt-get update -q -y && \  
apt-get dist-upgrade -y && \  
apt-get clean && \  
rm -rf /var/cache/apt/*  
  
RUN DEBIAN_FRONTEND=noninteractive \  
apt-get install -y \  
libxml2-dev \  
bash \  
python-pip \  
software-properties-common \  
libssh2-1-dev \  
zlib1g-dev \  
libxml2-dev \  
wget && \  
apt-get clean  
  
# INSTALL R AND PYTHON PACKAGES  
COPY additions.sh .  
COPY R_additions.r .  
COPY Python_additions.sh .  
  
RUN ./additions.sh  
  
# EXPOSE PORTS  
EXPOSE 3838  

