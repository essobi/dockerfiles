FROM alpine:edge  
ADD will.jordan@gmail.com-56ba6562.rsa.pub /etc/apk/keys/  
WORKDIR /opt/image-resizer  
COPY ./package.json /opt/image-resizer/  
COPY ./install.sh /tmp/install.sh  
RUN /tmp/install.sh  
ENV NODE_ENV=production  
COPY ./index.js /opt/image-resizer/  
EXPOSE 3001  
CMD ["node", "index.js"]  

