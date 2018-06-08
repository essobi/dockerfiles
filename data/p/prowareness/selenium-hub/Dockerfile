FROM ubuntu  
  
MAINTAINER Harm Pauw <h.pauw@prowareness.nl>  
  
RUN export DEBIAN_FRONTEND=noninteractive && \  
apt-get update && \  
apt-get install -y \  
default-jre \  
wget  
  
COPY starthub.sh .  
  
# Download latest version of selenium server  
RUN SELENIUM_URL=http://selenium-release.storage.googleapis.com/`wget -qO -
http://selenium-release.storage.googleapis.com/ | \  
awk -vRS="</Key>" '{gsub(/.*<Key>/,"");print}' | \  
grep standalone | \  
sort -rn | \  
head -n 1` && \  
wget -qO selenium-server-standalone.jar $SELENIUM_URL  
  
RUN useradd -m -U selenium  
RUN chmod 755 /starthub.sh && chmod 644 /selenium-server-standalone.jar  
  
USER selenium  
ENV HOME /home/selenium  
  
EXPOSE 4444  
CMD ["/starthub.sh"]  

