FROM wnameless/oracle-xe-11g  
  
MAINTAINER Kris Ramanah - krisrr3@hotmail.com  
  
RUN apt-get update &&\  
apt-get install -y nodejs npm && \  
npm install -g frisby && \  
npm install -g grunt-cli && \  
npm install -g jasmine-node && \  
ln -s /usr/bin/nodejs /usr/local/bin/node  
  
ENV ORACLE_HOME=/u01/app/oracle/product/11.2.0/xe  
ENV ORACLE_SID=XE  
ENV PATH=$ORACLE_HOME/bin:$PATH  
  
  
  
  

