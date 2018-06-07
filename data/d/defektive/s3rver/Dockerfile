FROM node:6-alpine  
  
EXPOSE 3000  
RUN npm install -g s3rver \  
&& mkdir -p /var/lib/s3  
  
ENTRYPOINT [ "/usr/local/bin/s3rver", "-p", "3000", "-h", "0.0.0.0", "-d",
"/var/lib/s3" ]  

