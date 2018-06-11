FROM node:8  
RUN mkdir code && \  
wget https://codeload.github.com/YMFE/yapi/tar.gz/v1.3.10 && \  
tar -xzvf v1.3.10 -C code \--strip-components 1  
  
WORKDIR /code  
RUN npm i  
RUN echo
'{"port":"3000","adminAccount":"admin@admin.com","db":{"servername":"mongodb","DATABASE":"yapi","port":27017,"user":"","pass":""},"mail":{"enable":true,"host":"smtp.163.com","port":465,"from":"***@163.com","auth":{"user":"***@163.com","pass":"*****"}}}'
> /config.json  
  
CMD ["node", "server/app.js"]

