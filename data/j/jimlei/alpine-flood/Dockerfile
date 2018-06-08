FROM mhart/alpine-node:latest  
MAINTAINER Jim Leirvik  
  
RUN adduser -D flood  
  
RUN apk add --update g++ make openssl python && \  
wget https://github.com/jfurrow/flood/archive/master.zip && \  
unzip -q master.zip && \  
rm master.zip && \  
mv /flood-master/config.template.js /flood-master/config.js && \  
chown -R flood:flood /flood-master  
EXPOSE 3000  
USER flood  
WORKDIR /flood-master  
CMD ["npm", "start"]

