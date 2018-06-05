FROM alpine  
RUN apk update; apk add dialog;  
RUN echo "ls" > /var/dialog.sh; chmod 777 /var/dialog.sh  
ENTRYPOINT sh /var/dialog.sh  

