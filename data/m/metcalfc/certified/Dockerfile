FROM ubuntu:trusty  
  
ADD . /certified  
  
WORKDIR /certified  
  
VOLUME /certified/etc  
  
RUN apt-get update && \  
apt-get install -y make ruby-ronn git && \  
make install && \  
apt-get -y autoremove --purge && \  
apt-get -y clean && \  
apt-get -y autoclean  
  
ENTRYPOINT /usr/local/bin/certified  
  
CMD [ '-h' ]  

