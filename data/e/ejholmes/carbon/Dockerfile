FROM ubuntu:12.04  
MAINTAINER Eric Holmes <eric@ejholmes.io>  
  
VOLUME ["/opt/graphite/storage/whisper"]  
  
ADD ./bin/start /bin/start  
ADD ./bin/build /bin/build  
RUN /bin/build  
  
EXPOSE 2003  
EXPOSE 2004  
ENTRYPOINT ["/bin/start"]  
CMD []  

