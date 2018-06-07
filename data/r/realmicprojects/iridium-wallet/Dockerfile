FROM realmicprojects/iridium:latest  
  
EXPOSE 8082  
ENV WALLETFILE pool.wallet  
ENV DAEMON_ADDR 127.0.0.1  
CMD /opt/iridium_bin/simplewallet --wallet-file
"/opt/iridium_data/$WALLETFILE" \--daemon-address "$DAEMON_ADDR" \--password
"$PASSWORD" \--rpc-bind-ip 0.0.0.0 --rpc-bind-port 8082  

