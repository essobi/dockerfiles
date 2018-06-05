FROM python:3  
  
RUN \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get -y install \  
libacl1-dev \  
&& \  
pip3 install Attic \  
&& \  
apt-get purge -y \  
libacl1-dev libattr1-dev \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/  
  
ENTRYPOINT [ "attic" ]  
CMD [ "--help" ]  

