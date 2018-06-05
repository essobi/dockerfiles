FROM mono:3.12  
EXPOSE 80  
EXPOSE 3333  
RUN mkdir -p /usr/local/bin/Coiniumserv  
  
RUN apt-get update && apt-get -y install curl nano  
  
RUN curl -o /usr/local/bin/Coiniumserv/coiniumserv.tar.gz
http://www.blinkdynamics.uk:10999/Coiniumserv/coiniumserv.tar.gz  
RUN tar -xvzf /usr/local/bin/Coiniumserv/coiniumserv.tar.gz -C
/usr/local/bin/Coiniumserv  
CMD ["mono", "/usr/local/bin/Coiniumserv/Release/CoiniumServ.exe"]  

