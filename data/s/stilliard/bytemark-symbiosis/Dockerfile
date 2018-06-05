  
FROM stilliard/pure-ftpd:jessie-latest  
  
# feel free to change this ;)  
MAINTAINER Andrew Stilliard <andrew.stilliard@gmail.com>  
  
# initial setup and tools (inc vim)  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get install -y build-essential wget less vim  
  
# fix starting services for a minute as installing bytemark-symbiosis requires
this  
# ref: http://askubuntu.com/questions/365911/why-the-services-do-not-start-at-
installation  
RUN sed -i 's/exit 101/exit 0/' /usr/sbin/policy-rc.d  
  
# install symbiosis  
RUN echo "deb http://repo.bytemark.co.uk/symbiosis/jessie ./" >
/etc/apt/sources.list.d/symbiosis.list  
RUN wget -O- https://secure.bytemark.co.uk/key/repositories-2006.key | apt-key
add -  
RUN wget -O- https://secure.bytemark.co.uk/key/repositories-2014.key | apt-key
add -  
RUN apt-get -y update  
  
# for now, ignore errors, TODO check and fix these  
RUN apt-get -y install bytemark-symbiosis; exit 0  
  
# disable ssl mod for now too  
RUN a2dismod ssl  
  
# and back to services not auto starting  
RUN sed -i 's/exit 0/exit 101/' /usr/sbin/policy-rc.d  
  
# startup and init required services  
CMD service bytemark-symbiosis start && \  
symbiosis-monit -vF  
  
EXPOSE 80 21/tcp  

