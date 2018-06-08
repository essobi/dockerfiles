# s3rver Local Docker!  
# https://github.com/jamhall/s3rver  
FROM node:alpine  
RUN npm install -g s3rver  
VOLUME /data  
EXPOSE 8001  
CMD [ "s3rver", "--hostname", "0.0.0.0", "--port", "8001", "--directory",
"/data" ]  

