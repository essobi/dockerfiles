FROM ubuntu:14.04  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install Curl  
RUN apt-get update -qq \  
&& apt-get install -qqy \  
curl  
  
# Install Node.js and NPM  
RUN apt-get update -qq \  
&& curl -sL https://deb.nodesource.com/setup_6.x | sudo bash - \  
&& apt-get install -qqy \  
git \  
nodejs  
  
# Config Git  
RUN git config --global http.sslVerify false  
  
# Install Notify Osd for Gulp Notify  
RUN apt-get update -qq \  
&& apt-get install -qqy \  
notify-osd  
  
WORKDIR /src  
  
# Binarie install or start Node  
ADD assets/bin/node /bin/node  
RUN chmod +x /bin/node  
  
ENTRYPOINT ["/bin/node"]  

