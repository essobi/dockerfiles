FROM node:0.10.40  
RUN mkdir /var/s3  
RUN npm install -g s3rver  
  
EXPOSE 4521  
CMD [ "s3rver", "-d", "/var/s3", "-p", "4521"]

