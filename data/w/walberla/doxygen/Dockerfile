FROM walberla/buildenv-ubuntu-basic:16.04  
MAINTAINER Christian Godenschwager "christian.godenschwager@fau.de"  
ADD 01_nodoc /etc/dpkg/dpkg.cfg.d/01_nodoc  
  
RUN apt-get update && apt-get install -y \  
texlive \  
perl \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  

