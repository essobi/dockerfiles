FROM java:8-jre-alpine  
  
RUN apk add --no-cache curl jq tmux  
  
RUN mkdir /mc  
ADD launch.sh /mc/  
  
RUN chmod +x /mc/launch.sh  
  
VOLUME /minecraft  
EXPOSE 25565  
CMD "/mc/launch.sh"  

