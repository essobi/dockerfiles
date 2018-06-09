FROM debian:stretch  
  
#install subversion  
RUN mkdir -p /home/svn \  
&& apt-get update \  
&& apt-get install -y subversion \  
curl \  
nano \  
sudo \  
apache2 \  
libapache2-mod-svn  
  
RUN mkdir /opt/svn && chmod -R 777 /opt/svn  

