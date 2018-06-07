FROM uwitech/ohie-base  
  
USER root  
  
#install openinfoman  
RUN apt-get update  
COPY BaseX862.zip /root/BaseX862.zip  
RUN apt-get -y install software-properties-common \  
python-software-properties \  
wget \  
inotify-tools \  
debconf-utils unzip \  
git \  
default-jre \  
openjdk-7-jre  
RUN unzip ~/BaseX862.zip -d ~/  
RUN touch ~/basex/.basexhome  
RUN chmod 777 -R ~/basex  
RUN git clone https://github.com/openhie/openinfoman ~/openinfoman && \  
mkdir -p ~/basex/resources/stored_query_definitions && \  
mkdir -p ~/basex/resources/stored_updating_query_definitions && \  
cd ~/basex/resources/stored_query_definitions && \  
ln -sf ~/openinfoman/resources/stored_query_definitions/* . && \  
cd ~/basex/resources/stored_updating_query_definitions && \  
ln -sf ~/openinfoman/resources/stored_updating_query_definitions/* . && \  
mkdir -p ~/basex/resources/shared_value_sets && \  
cd ~/basex/resources/shared_value_sets && \  
ln -sf ~/openinfoman/resources/shared_value_sets/* . && \  
mkdir -p ~/basex/resources/service_directories && \  
cd ~/basex/resources/service_directories && \  
ln -sf ~/openinfoman/resources/service_directories/* .  
  
COPY basex.sh /root/basex.sh  
RUN chmod +x ~/basex.sh  
RUN ~/basex.sh  
  
COPY web.xml /root/basex/webapp/WEB-INF/web.xml  
  
#install openinfoman-ilr  
COPY openinfoman-ilr.sh /root/openinfoman-ilr.sh  
RUN chmod +x ~/openinfoman-ilr.sh  
RUN ~/openinfoman-ilr.sh  
  
#install openinfoman-hwr  
RUN apt-get -y install openinfoman-hwr  
COPY csd_lsd.xqm
/var/lib/openinfoman/repo/com/github/openhie/openinfoman/csd_lsd.xqm  
  
COPY csd_webconf.xqm
/var/lib/openinfoman/repo/com/github/openhie/openinfoman/csd_webconf.xqm  
  
COPY cmd.sh /root/cmd.sh  
RUN chmod +x ~/cmd.sh  
  
VOLUME /var/lib/openinfoman/data  
  
CMD ~/cmd.sh  

