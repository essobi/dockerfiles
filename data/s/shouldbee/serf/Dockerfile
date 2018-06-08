FROM ubuntu  
  
RUN apt-get -y install unzip wget  
  
RUN cd /tmp/  
RUN wget --no-check-certificat
https://dl.bintray.com/mitchellh/serf/0.6.4_linux_amd64.zip -O serf.zip  
  
RUN unzip serf.zip  
RUN chmod +x serf  
RUN mv serf /usr/local/bin/serf  

