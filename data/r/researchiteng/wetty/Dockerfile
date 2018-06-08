FROM node:alpine  
LABEL maintainer ReSearchITEng  
  
ENV USR="term"  
RUN apk add --update git make g++ python bash procps \  
&& git clone https://github.com/krishnasrinivas/wetty \  
&& cd wetty \  
&& npm install \  
&& apk del git python make g++  
  
RUN adduser -D -h /home/$USR -s /bin/bash $USR  
RUN echo "$USR:${PASS:-$USR}" | chpasswd  
  
EXPOSE 3000  
ENTRYPOINT ["node"]  
CMD ["app.js", "-p", "3000"]  

