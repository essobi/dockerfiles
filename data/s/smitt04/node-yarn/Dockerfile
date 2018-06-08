FROM node:8.9-alpine  
MAINTAINER Kevin Smithson  
  
RUN apk update && \  
apk add yarn && \  
apk add git && \  
apk add bash && \  
apk add openssh-client  
  
ADD ssh-env-config.sh /usr/bin/  
RUN chmod +x /usr/bin/ssh-env-config.sh  
  
ENTRYPOINT ["ssh-env-config.sh"]  

