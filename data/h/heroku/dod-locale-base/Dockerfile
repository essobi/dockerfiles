FROM ubuntu:xenial  
  
# let's make apt list package versions, since those are handy during devel  
RUN echo 'APT::Get::Show-Versions "1";' > /etc/apt/apt.conf.d/verbose  
  
ENV HOME=/root \  
TERM=xterm-256color \  
DEBIAN_FRONTEND=noninteractive \  
LANG=en_US.UTF-8 \  
LANGUAGE=en_US:en \  
LC_ALL=en_US.UTF-8  
# get all available locales and configure them  
RUN apt-get update && apt-get install --yes locales && rm -rf
/var/lib/apt/lists/*  
RUN locale-gen en_US.UTF-8 && update-locale  
RUN cp /usr/share/i18n/SUPPORTED /etc/locale.gen  
RUN dpkg-reconfigure -f noninteractive locales  
  
# ensure distro is upgraded  
RUN apt-get update && \  
apt-get \  
\--yes \  
\--allow-downgrades \  
\--allow-remove-essential \  
\--allow-change-held-packages \  
dist-upgrade && \  
rm -rf /var/lib/apt/lists/*  

