# -*- sh -*-  
FROM ubuntu:12.04  
MAINTAINER elsdoerfer  
  
# Enable this during development.  
#RUN echo 'Acquire::http { Proxy "http://192.168.59.103:3142"; };' >>
/etc/apt/apt.conf.d/01proxy  
ENV DISCOURSE_VERSION 0.9.9.12  
ENV RAILS_ENV production  
  
ENV LANGUAGE en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
ADD install /  
RUN bash -xe /install  
  
ADD enter /  
RUN chmod +x /enter  
  
WORKDIR /discourse  
ENTRYPOINT ["/enter"]  

