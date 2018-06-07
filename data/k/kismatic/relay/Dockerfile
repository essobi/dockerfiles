FROM ubuntu:14.04  
MAINTAINER patrick@kismatic.com  
  
RUN apt-get update -qq && apt-get install -qqy \  
apt-transport-https \  
ca-certificates \  
curl \  
iptables \  
socat  
  
ADD ./wrapdocker /usr/local/bin/wrapdocker  
RUN chmod +x /usr/local/bin/wrapdocker  
  
CMD ["wrapdocker"]  

