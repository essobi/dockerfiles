FROM python:3  
  
RUN \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get -y install \  
less \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/  
RUN pip install http-prompt  
  
ENTRYPOINT [ "http-prompt" ]  

