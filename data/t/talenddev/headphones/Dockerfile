FROM talenddev/python  
MAINTAINER talenddev <leo@talenddev.com>  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN git clone https://github.com/rembo10/headphones.git /opt/headphones  
  
# Add headphones to runit  
RUN mkdir /etc/service/headphones  
ADD start.sh /etc/service/headphones/run  
RUN chmod +x /etc/service/headphones/run  
  
EXPOSE 8181  

