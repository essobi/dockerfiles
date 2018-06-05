FROM ubuntu:16.04  
LABEL maintainer="me@alexcreek.com"  
RUN useradd dropbox -m  
WORKDIR /home/dropbox  
  
RUN apt-get update \  
&& apt-get -y install wget python \  
&& apt-get clean  
  
RUN wget --quiet -O dropbox.py
"https://www.dropbox.com/download?dl=packages/dropbox.py" \  
&& chmod +x dropbox.py \  
&& wget --quiet -O - "https://www.dropbox.com/download?plat=lnx.x86_64" | tar
xzf -  
  
USER dropbox  
CMD ./.dropbox-dist/dropboxd  

