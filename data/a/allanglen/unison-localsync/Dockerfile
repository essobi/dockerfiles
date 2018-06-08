FROM ubuntu  
  
RUN apt-get install software-properties-common -y  
  
# ppa provides latest unison version (currently 2.84.3) which is required for
-repeat watch  
RUN add-apt-repository ppa:eugenesan/ppa  
  
RUN apt-get update -y  
RUN apt-get install unison -y  
  
COPY unison.sh unison.sh  
  
VOLUME /root/.unison  
  
ENTRYPOINT ["./unison.sh"]

