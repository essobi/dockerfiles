FROM ubuntu:latest  
  
COPY ./certified /certified  
WORKDIR /certified  
RUN rm -f .git  
RUN apt-get update && \  
apt-get install -y make ruby-ronn git && \  
make install && \  
apt-get -y autoremove --purge && \  
apt-get -y clean && \  
apt-get -y autoclean  
  
RUN git config --global user.email "vvrantchan@whitbyschool.org"  
RUN git config --global user.name "Victor Vrantchan"  
  
VOLUME /certified/etc  
ENTRYPOINT /usr/local/bin/certified  
  
CMD [ '-h' ]  
  

