FROM phusion/baseimage:0.10.0  
ENV NodeJS_VERSION 8.10.0  
ENV tiddlywiki_VERSION 5.1.15  
# baseimage init scripts  
RUN mkdir -p /etc/my_init.d  
ADD init /etc/my_init.d  
RUN chmod +x /etc/my_init.d/*  
  
# baseimage daemons  
COPY daemons/tiddlywiki.sh /etc/service/tiddlywiki/run  
RUN chmod +x /etc/service/tiddlywiki/run  
  
# install tiddlywiki binaries  
RUN apt-get update && apt-get upgrade -y  
RUN apt-get install wget  
COPY build/install_nodejs.sh /tmp/build/install_nodejs.sh  
COPY build/install_tiddlywiki.sh /tmp/build/install_tiddlywiki.sh  
RUN chmod +x /tmp/build/*  
RUN /tmp/build/install_nodejs.sh  
RUN /tmp/build/install_tiddlywiki.sh  
  
# clean up  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# ports  
EXPOSE 8080  
CMD ["/sbin/my_init"]  

