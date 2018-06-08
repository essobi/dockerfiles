from ubuntu  
RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" >
/etc/apt/sources.list  
RUN apt-get -y update  
RUN apt-get -y install wget git redis-server supervisor  
run wget -O - http://nodejs.org/dist/v0.8.23/node-v0.8.23-linux-x64.tar.gz |
tar -C /usr/local/ --strip-components=1 -zxv  
RUN npm install hipache -g  
RUN mkdir -p /var/log/supervisor  
ADD ./supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
ADD ./config.json /usr/local/lib/node_modules/hipache/config/config.json  
EXPOSE 80  
EXPOSE 6379  
CMD ["supervisord", "-n"]

