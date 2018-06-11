FROM debian:jessie  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install -y \  
git-buildpackage \  
locales \  
python-all-dev \  
python-pip \  
python-setuptools  
  
# The locales package resets debconf selections upon install for some  
# reason, so we need to reconfigure after install instead of  
# preseeding.  
# see https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=684134  
RUN printf "\  
locales locales/locales_to_be_generated multiselect en_US.UTF-8 UTF-8 \n\  
locales locales/default_environment_locale select en_US.UTF-8 \  
" | debconf-set-selections  
RUN dpkg-reconfigure --frontend=noninteractive locales  
  
# pip version 1.5.6 seems to have problems with SSL.  
RUN pip install --upgrade pip  
  
# Type A version of stdeb has needed patches to handle hardlinking  
# correctly on boot2docker.  
RUN pip install https://github.com/typeamachines/stdeb/archive/type-
a_0.8.6.zip  
  
RUN adduser user  
RUN echo 'user ALL=(ALL) NOPASSWD:ALL' > /etc/sudoers.d/user  

