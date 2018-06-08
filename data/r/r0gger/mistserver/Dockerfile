FROM phusion/baseimage:latest  
MAINTAINER R0GGER  
  
ENV PATH /app/mistserver:$PATH  
ENV MISTSERVER=https://r.mistserver.org/dl/mistserver_64V2.12.tar.gz  
  
CMD ["/sbin/my_init"]  
  
# install basics  
RUN apt-get update  
RUN apt-get install wget nano -yq  
RUN mkdir -p /app/mistserver /config /media  
ADD start.sh /etc/my_init.d/start.sh  
RUN chmod +x /etc/my_init.d/*.sh  
  
# install mistserver  
RUN wget -qO- ${MISTSERVER} | tar xvz -C /app/mistserver  
  
# clean up  
RUN apt-get clean  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
VOLUME /config /media  
EXPOSE 4242 8080 1935 554  

