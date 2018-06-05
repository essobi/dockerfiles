FROM node:4-alpine  
  
WORKDIR /app  
  
RUN apk update && apk upgrade && apk add bash && apk add git && apk add \  
ca-certificates && update-ca-certificates && apk add openssl && apk add make\  
&& apk add gcc && apk add python && apk add wget && apk add tmux && apk add
g++  
  
RUN git clone https://github.com/c9/core.git  
RUN wget https://raw.githubusercontent.com/c9/install/master/link.sh  
RUN bash link.sh  
RUN bash core/scripts/install-sdk.sh  
RUN mkdir core/code  
  
WORKDIR /app/core  
  
CMD ["node", "server.js", "-p", "8080", "-a", ":", "--listen", "0.0.0.0",
"-w", "code"]  

