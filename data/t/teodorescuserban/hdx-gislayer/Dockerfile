FROM teodorescuserban/hdx-base-gislayer:latest  
  
MAINTAINER Serban Teodorescu, teodorescu.serban@gmail.com  
  
RUN mkdir -p /srv && \  
cd /srv && \  
git clone https://bitbucket.org/agartner/gisrestlayer.git gislayer && \  
cd /srv/gislayer && \  
pip install -r requirements.txt  
  
RUN mkdir -p /etc/service/gislayer  
COPY run /etc/service/gislayer/  
RUN chmod +x /etc/service/gislayer/run  
  
RUN apt-get -qq update && apt-get -qq -y install libc-bin && apt-get clean &&
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
COPY app.conf.tpl /srv/  
  
EXPOSE 5000  

