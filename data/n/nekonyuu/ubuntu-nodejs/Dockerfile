FROM nekonyuu/ubuntu-devel:trusty  
MAINTAINER Jonathan Raffre <nk@nyuu.eu>  
  
# prepare system environment  
RUN apt-get update \  
&& apt-get install -y apt-transport-https curl socat build-essential \  
&& curl -s https://deb.nodesource.com/gpgkey/nodesource.gpg.key | apt-key add
\- \  
&& echo "deb https://deb.nodesource.com/node trusty main" | tee
/etc/apt/sources.list.d/nodejs.list \  
&& apt-get update \  
&& apt-get install -y \--no-install-recommends \  
nodejs \  
&& rm -rf /var/lib/apt/lists/*  

