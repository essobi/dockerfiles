FROM mhart/alpine-node:6.0.0  
VOLUME /root/.npm  
ADD package.json /tmp/package.json  
RUN cd /tmp && npm install --production  
RUN mkdir -p /app/lib && ln -s /tmp/node_modules /app/node_modules  
  
WORKDIR "/app"  
COPY start.sh /app/  
COPY index.js /app/  
COPY libs /app/libs  
  
EXPOSE 8080  
CMD ["/app/start.sh"]  

