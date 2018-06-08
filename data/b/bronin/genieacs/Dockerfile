FROM node:8  
RUN mkdir -p /opt/app && cd /opt/app &&\  
curl -L https://github.com/genieacs/genieacs/archive/master.tar.gz | tar xzf -
-C /opt/app --strip-components=1 && \  
npm install && npm run configure && npm run compile && \  
rm -rf /root/.npm /tmp/npm-*  
  
WORKDIR /opt/app  
COPY config.json config/config.json  
  
EXPOSE 7547  
ENTRYPOINT ["/opt/app/bin/genieacs-cwmp"]  
  
CMD ["/bin/bash"]  

