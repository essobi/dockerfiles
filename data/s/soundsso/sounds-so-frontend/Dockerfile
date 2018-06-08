FROM jorgenfb/nginx-nodejs-bower-gulp  
MAINTAINER dev@sounds.so  
  
WORKDIR /app  
  
ADD package.json /app/  
RUN npm install  
  
RUN git config \--global url."https://".insteadOf git://  
ADD bower.json /app/  
RUN bower install --allow-root  
  
ADD index.html /app/index.html  
ADD gulpfile.js /app/gulpfile.js  
ADD gulpTasks /app/gulpTasks  
ADD src /app/src  
RUN gulp scripts && gulp styles && rm -rf gulpTasks  
  
ADD conf/nginx.conf /etc/nginx/sites-enabled/default  
EXPOSE 80  
  
ADD conf/start.sh /start.sh  
CMD ["/bin/sh", "/start.sh"]  

