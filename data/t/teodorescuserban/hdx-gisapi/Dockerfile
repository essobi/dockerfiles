FROM teodorescuserban/hdx-base-gisapi:latest  
  
MAINTAINER Serban Teodorescu, teodorescu.serban@gmail.com  
  
COPY run_gisapi settings.js.tpl /tmp/  
  
RUN mkdir -p /etc/service/gisapi /srv /var/log/gisapi && \  
mv /tmp/settings.js.tpl /srv/ && \  
mv /tmp/run_gisapi /etc/service/gisapi/run && \  
chmod +x /etc/service/gisapi/run && \  
git clone --depth 1 https://bitbucket.org/agartner/hdx-pgrestapi.git
/srv/gisapi && \  
cd /srv/gisapi && \  
npm install && \  
apt-get -qq update && apt-get -qq -y install libc-bin && apt-get clean && rm
-rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
EXPOSE 80 5858  

