FROM library/node  
  
RUN apt-get install git && \  
rm -rf /tmp/* /var/cache/apk/*  
  
COPY . src  
  
WORKDIR src  
  
RUN npm install  
  
CMD npm start

