FROM ubuntu:14.04.3  
RUN apt-get install -y apt-transport-https curl  
RUN curl https://repo.varnish-cache.org/ubuntu/GPG-key.txt | sudo apt-key add
-  
RUN sudo sh -c 'echo "deb https://repo.varnish-cache.org/ubuntu/ trusty
varnish-4.1" > /etc/apt/sources.list.d/varnish-cache.list'  
RUN apt-get update && apt-get install -y varnish  
  
ADD start.sh /start.sh  
RUN chmod +x /start.sh  
  
CMD /start.sh  
EXPOSE 80

