FROM patdreis/docker-zcash  
  
#RUN mkdir /home/zcash/.zcash/ && touch /home/zcash/.zcash/zcash.conf \  
# && echo "rpcuser=zcash" > /home/zcash/.zcash/zcash.conf \  
# && echo "rpcpassword=`pwgen 20 1`" >> /home/zcash/.zcash/zcash.conf \  
# && echo "addnode=mainnet.z.cash" >> /home/zcash/.zcash/zcash.conf  
  
USER root  
  
COPY start.sh /usr/bin/zec  
  
RUN chmod -R 777 /usr/bin/zec  
  
ENTRYPOINT ["zec"]  
  

