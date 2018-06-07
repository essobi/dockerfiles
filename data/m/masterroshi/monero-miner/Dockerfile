FROM masterroshi/xmrig-alpine  
  
# Configuration variables.  
ENV POOL_URL POOL_URL  
ENV POOL_USER WALLET_ID  
ENV POOL_PW x  
ENV MAX_CPU 100  
ENV USE_SCHEDULER false  
ENV START_TIME 2100  
ENV STOP_TIME 0600  
ENV DAYS Monday,Tuesday,Wednesday,Thursday,Friday,Saturday,Sunday  
  
# Set entrypoint  
ENTRYPOINT ./script.sh cryptonight $POOL_URL $POOL_USER $POOL_PW $MAX_CPU
$USE_SCHEDULER $START_TIME $STOP_TIME $DAYS  

