# base image  
FROM python:3  
# update and install  
RUN apt-get update && apt-get install -y \  
curl \  
lynx \  
nano \  
openssl \  
pandoc \  
tree \  
wget \  
vim  
  
# copy source  
WORKDIR /usr/src  
COPY README.md .  
ADD python/ python/  
ADD shell/ shell/  
  
# install python requirements  
RUN pip install -r python/requirements.txt  
  
# link scripts  
RUN ln /usr/src/shell/scrape.sh /usr/bin/scrape  
RUN ln /usr/src/shell/extract_token.sh /usr/bin/extract_token  
  
# setup env  
ENV FACEBOOK_TOKEN=''  
ENV FACEBOOK_ID=''  
ENV TINDERPICS_DIR=''  
ENV FBACCOUNT_EMAIL=''  
ENV FBACCOUNT_USERNAME=''  
# setup rc file  
COPY .bashrc /root/  
  
# make working dir  
RUN mkdir -p /home/tndrscrpr  
WORKDIR /home/tndrscrpr  

