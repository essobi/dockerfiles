FROM httpd  
MAINTAINER Micah J Cowan "micah@addictivecode.org"  
  
ENV SNAP_ZIP https://github.com/micahcowan/Snap--Build-Your-Own-
Blocks/archive/faves.zip  
  
RUN set -x && \  
cd /usr/local/apache2/htdocs && \  
apt-get update -y && \  
apt-get install -y wget unzip && \  
wget "$SNAP_ZIP" -O snap.zip && \  
unzip snap.zip && \  
mv Snap--Build*/* . && \  
rm -rv Snap--Build*/ && \  
chown -R 501:staff * && \  
apt-get remove --purge -y wget unzip  

