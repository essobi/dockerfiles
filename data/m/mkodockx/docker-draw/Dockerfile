FROM mkodockx/docker-base  
MAINTAINER http://m-ko.de Markus Kosmal <code@cnfg.io>  
  
# install requirements  
RUN apt-get update -yq && \  
apt-get install -yq \  
curl \  
unzip \  
nodejs \  
git \  
npm \  
mysql-client \  
libcairo2-dev libjpeg8-dev libpango1.0-dev libgif-dev \  
build-essential \  
g++  
  
# support direct node calls  
RUN ln -s /usr/bin/nodejs /usr/bin/node  
  
# add a user to run app with  
RUN useradd -u 1000 -m -s /bin/bash drawer  
  
# fetch application repo  
RUN mkdir -p /opt/repo && \  
cd /opt/repo && \  
git clone git://github.com/JohnMcLear/draw.git && \  
chown -R drawer /opt/repo  
  
WORKDIR /opt/repo/draw  
  
COPY script/entrypoint.sh /entrypoint.sh  
  
VOLUME /opt/repo/draw/var  
RUN chown drawer /entrypoint.sh && chmod o+x /entrypoint.sh  
  
EXPOSE 9002  
USER drawer  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["bin/run.sh"]  

