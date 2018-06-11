FROM ubuntu  
MAINTAINER George Lewis <schvin@schvin.net>  
RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" >
/etc/apt/sources.list  
RUN apt-get update -yqV  
RUN apt-get upgrade -yqV  
  
RUN apt-get install -y unbound  
  
# minimal recursive unbound configuration  
RUN echo "port: 5353" >> /etc/unbound/unbound.conf  
RUN echo "interface: 0.0.0.0" >> /etc/unbound/unbound.conf  
RUN echo "interface: ::0" >> /etc/unbound/unbound.conf  
RUN echo "access-control: 172.16.0.0/12 allow" >> /etc/unbound/unbound.conf  
RUN echo "use-syslog: no" >> /etc/unbound/unbound.conf  
RUN echo "logfile: /dev/stdout" >> /etc/unbound/unbound.conf  
RUN echo "log-queries: yes" >> /etc/unbound/unbound.conf  
  
# create pidfile  
RUN touch /var/run/unbound.pid  
RUN chown unbound:unbound /var/run/unbound.pid  
  
USER unbound  
ENTRYPOINT ["/usr/sbin/unbound"]  
  
CMD ["-h"]  
  
EXPOSE 5353/udp  
EXPOSE 5353  

