FROM emanueleperuffo/oracle-java-8:latest  
MAINTAINER Emanuele Peruffo <info@emanueleperuffo.com>  
  
ENV HOME /root  
ADD . /build  
  
ENV PGHOST postgres.example.com  
ENV PGUSER nominatim  
ENV PHOTON_LANGUAGES it,en  
  
RUN /build/prepare.sh && \  
/build/services.sh && \  
/build/cleanup.sh  
  
VOLUME ["/var/db/photon"]  
  
EXPOSE 2322  
CMD ["/sbin/my_init"]

