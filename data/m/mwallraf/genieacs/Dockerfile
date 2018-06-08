FROM node  
MAINTAINER Sergio Tejón <sergio.tejon@gmail.com>  
  
WORKDIR /usr/src  
  
RUN git clone https://github.com/zaidka/genieacs.git  
RUN ln -s /usr/src/genieacs /app  
  
WORKDIR /app  
  
RUN npm install && npm run configure && npm run compile && \  
curl https://bootstrap.pypa.io/ez_setup.py -o - | python && \  
easy_install supervisor  
  
ADD ./etc/supervisord.conf /etc/supervisord.conf  
ADD ./config.json /app/config/config.json  
ADD ./start.sh /app  
  
CMD ["/bin/sh", "/app/start.sh"]  

