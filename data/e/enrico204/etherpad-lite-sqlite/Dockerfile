# Stable version of etherpad doesn't support npm 2  
FROM debian:jessie  
MAINTAINER Enrico204 <enrico204@gmail.com>  
  
ENV ETHERPAD_VERSION 1.6.1  
RUN apt-get update && \  
apt-get install -y curl unzip nodejs-legacy npm && \  
rm -r /var/lib/apt/lists/*  
  
WORKDIR /opt/  
  
RUN curl -SL \  
https://github.com/ether/etherpad-lite/archive/${ETHERPAD_VERSION}.zip \  
> etherpad.zip && unzip etherpad && rm etherpad.zip && \  
mv etherpad-lite-${ETHERPAD_VERSION} etherpad-lite  
  
WORKDIR etherpad-lite  
  
RUN bin/installDeps.sh  
  
RUN sed -i 's/^node/exec\ node/' bin/run.sh  
  
VOLUME ["/opt/etherpad-lite/var"]  
  
EXPOSE 9001  
RUN ln -s var/SESSIONKEY.txt SESSIONKEY.txt  
RUN ln -s var/APIKEY.txt APIKEY.txt  
RUN useradd -d /opt/etherpad-lite/ -M -U epad  
RUN chown epad.epad . -R  
USER epad:epad  
  
CMD ["bin/run.sh"]  
  

