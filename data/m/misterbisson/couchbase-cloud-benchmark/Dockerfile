FROM node:0.12.4  
RUN npm install -g cb-cloud-benchmark json  
  
ADD ./bin/start.bash /bin/start.bash  
  
ADD ./data /data  
  
CMD [ "/bin/bash /bin/start.bash" ]

