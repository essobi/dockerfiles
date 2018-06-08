FROM cdbishop89/linux-mint-18:latest  
MAINTAINER VCA Technology <developers@vcatechnology.com>  
  
# Install useful packages  
RUN apt-get install -y \  
python \  
git \  
openssh-client \  
sudo  
  
RUN echo 'APT::Update::Post-Invoke-Success {"touch
/var/lib/apt/periodic/update-success-stamp 2>/dev/null || true";};' >
/etc/apt/apt.conf.d/15update-stamp  
RUN apt-get update  

