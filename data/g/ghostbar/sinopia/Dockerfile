FROM dockerfile/nodejs  
MAINTAINER Jose-Luis Rivas <me@ghostbar.co>  
RUN adduser --disabled-password --gecos "Sinopia" sinopia  
RUN mkdir -p /opt/sinopia/storage  
WORKDIR /opt/sinopia  
RUN npm install js-yaml sinopia@0.13.0  
ADD /start.sh /opt/sinopia/start.sh  
RUN chown -R sinopia:sinopia /opt/sinopia  
USER sinopia  
EXPOSE 4873  
VOLUME /opt/sinopia  
  
CMD ["bash", "/opt/sinopia/start.sh"]  

