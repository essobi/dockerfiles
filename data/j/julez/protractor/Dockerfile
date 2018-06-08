FROM mhart/alpine-node:6.2.2  
RUN npm install -g protractor \  
&& rm -rf /root/.npm /root/.node-gyp \  
&& npm uninstall -g npm  
  
WORKDIR /app  
CMD ["-"]  
ENTRYPOINT ["protractor"]  

