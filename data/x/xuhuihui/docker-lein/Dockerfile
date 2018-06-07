FROM flurdy/oracle-java8  
  
MAINTAINER xhh  
  
RUN apt-get update && apt-get upgrade -y -o Dpkg::Options::="--force-confold"  
  
ENV LEIN_ROOT true  
  
RUN wget -q -O /usr/bin/lein \  
https://raw.githubusercontent.com/technomancy/leiningen/stable/bin/lein \  
&& chmod +x /usr/bin/lein  
  
RUN lein  
  
#RUN mkdir /app  
#WORKDIR /app  
#ENTRYPOINT lein  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  
  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

