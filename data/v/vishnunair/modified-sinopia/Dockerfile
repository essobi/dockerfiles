FROM dockerfile/nodejs  
MAINTAINER Vishnu Nair <vishnu.nair66@gmail.com>  
RUN mkdir -p /opt/sinopia/storage  
WORKDIR /opt/sinopia  
RUN npm install js-yaml sinopia@0.13.0  
ADD /config_gen.js /opt/sinopia/config_gen.js  
ADD /start.sh /opt/sinopia/start.sh  
CMD ["/opt/sinopia/start.sh"]  
EXPOSE 4873  
VOLUME /opt/sinopia  

