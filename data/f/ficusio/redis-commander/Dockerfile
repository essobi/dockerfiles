FROM ficusio/node-alpine:5  
RUN npm install -g redis-commander \  
&& npm cache clean \  
&& rm -rf ~/.node-gyp /tmp/* \  
&& mkdir /root  
  
COPY wrap /usr/local/bin/  
RUN chmod +x /usr/local/bin/wrap  
  
EXPOSE 8081  
ENTRYPOINT ["wrap", "redis-commander", "--address", "0.0.0.0", "--port",
"8081"]  

