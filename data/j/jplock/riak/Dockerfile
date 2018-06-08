# DOCKER-VERSION 0.6.1  
# VERSION 0.3  
FROM ubuntu  
MAINTAINER Justin Plock <jplock@gmail.com>  
  
RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" >
/etc/apt/sources.list  
RUN apt-get update  
RUN apt-get upgrade -y  
  
RUN apt-get -y -q install curl  
  
# Hack for initctl not being available in Ubuntu  
RUN dpkg-divert --local \--rename --add /sbin/initctl  
RUN ln -s /bin/true /sbin/initctl  
  
RUN curl http://apt.basho.com/gpg/basho.apt.key | apt-key add -  
RUN echo "deb http://apt.basho.com precise main" >
/etc/apt/sources.list.d/basho.list  
RUN apt-get update  
RUN apt-get -y -q install riak || true  
RUN sed 's/127.0.0.1/0.0.0.0/' -i /etc/riak/app.config  
  
EXPOSE 8098 8087  
CMD /usr/sbin/riak start && tail -f /var/log/riak/console.log  

