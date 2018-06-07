FROM node:8  
RUN apt update && apt install --yes shellcheck  
RUN npm i -g reveal-md@1.1.3 http-server@0.11.1  
  
WORKDIR /usr/local/web/  
  
COPY docker.sh /usr/local/web/scripts/docker.sh  
COPY shellter.sh /usr/local/web/scripts/shellter.sh  
COPY winscp.sh /usr/local/web/scripts/winscp.sh  
COPY entrypoint.sh /usr/local/web/entrypoint.sh  
RUN shellcheck *.sh  
  
ENTRYPOINT ["./entrypoint.sh"]  

