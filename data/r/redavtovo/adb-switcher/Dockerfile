FROM sorccu/adb  
  
RUN apk update && \  
apk add expect &&\  
rm -r /var/cache/apk/APKINDEX.*  
  
ARG scriptLocation=/opt  
  
ENV DEBUG=false \  
SCRIPTS_LOCATION=$scriptLocation  
  
COPY scripts/*.sh $scriptLocation/  
  
RUN chmod +x $scriptLocation/*.sh  
  
ENTRYPOINT /opt/switcher.sh  

