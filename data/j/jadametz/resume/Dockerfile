FROM node:alpine  
LABEL maintainer="jesseadametz@gmail.com"  
  
RUN apk update && apk add --no-cache git && \  
npm install -g --unsafe-perm resume-cli yamljs  
  
WORKDIR /resume  
COPY resume.yml .  
  
COPY entrypoint.sh /usr/local/bin  
ENTRYPOINT ["entrypoint.sh"]  
CMD ["yml"]  

