FROM java:8  
MAINTAINER blizarazu  
  
RUN wget https://github.com/burst-
team/burstcoin/releases/download/1.2.9/burstcoin-1.2.9.zip  
RUN unzip -a burstcoin-1.2.9.zip -d /usr/src/burstcoin  
WORKDIR /usr/src/burstcoin  
  
VOLUME /usr/src/burstcoin/conf /usr/src/burstcoin/burst_db  
  
EXPOSE 8125 8123  
RUN chmod +x /usr/src/burstcoin/run.sh  
CMD ./run.sh  

