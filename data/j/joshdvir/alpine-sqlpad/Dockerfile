FROM mhart/alpine-node  
  
RUN apk add --update \  
bash  
  
RUN npm install sqlpad -g  
  
ENV NODE_ENV=production \  
SQLPAD_PORT=80 \  
SQLPAD_PASSPHRASE=you_need_something_secured_here  
  
RUN mkdir -p /data  
  
EXPOSE 80  
VOLUME ["/data"]  
  
CMD ["sqlpad", "--dir /data"]

