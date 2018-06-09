FROM debian:jessie  
RUN apt-get update && apt-get install -y 0install-core python-gobject unzip
make gcc --no-install-recommends  
COPY trustdb.xml /root/.config/0install.net/injector/trustdb.xml  
RUN 0install add 0test http://0install.net/2008/interfaces/0test.xml  

