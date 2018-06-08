FROM phusion/baseimage:0.9.16  
MAINTAINER https://m-ko-x.de Markus Kosmal <code@m-ko-x.de>  
  
RUN apt-get update -y && apt-get install -y \  
build-essential \  
ca-certificates \  
curl \  
git \  
nodejs \  
npm \  
python  
RUN ln -s /usr/bin/nodejs /usr/bin/node  
  
RUN curl https://raw.githubusercontent.com/creationix/nvm/v0.24.0/install.sh |
bash && \  
. /root/.nvm/nvm.sh && \  
nvm install stable  
  
CMD ["/sbin/my_init"]

