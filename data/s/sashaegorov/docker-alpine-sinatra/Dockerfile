FROM gliderlabs/alpine:latest  
MAINTAINER Alexander Egorov <a.a.egoroff@gmail.com>  
  
EXPOSE 5678  
ENV RACK_USER sinatra  
ENV RACK_ENV development  
  
COPY . /tmp  
RUN /tmp/prepare.sh  
CMD su ${RACK_USER} -c "rackup -o 0.0.0.0 -p 5678 -E ${RACK_ENV}
/home/${RACK_USER}/config.ru"  

