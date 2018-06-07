FROM inclusivedesign/nodejs  
  
RUN yum -y install git && \  
yum -y clean all  
  
COPY package.json /opt/rbmm-nodejs/  
  
RUN cd /opt/rbmm-nodejs/ && \  
npm install  
  
COPY . /opt/rbmm-nodejs/  
  
WORKDIR /opt/rbmm-nodejs  
  
RUN mv /opt/rbmm-nodejs/start.sh /usr/local/bin/start.sh && \  
chmod +x /usr/local/bin/start.sh && \  
yum -y install nodejs-grunt-cli && \  
cd /opt/rbmm-nodejs && \  
grunt dedupe-infusion && \  
yum -y autoremove nodejs-grunt-cli  
  
EXPOSE 8078  
CMD ["/usr/local/bin/start.sh"]  

