FROM ubuntu:trusty  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get install -y postgresql  
RUN apt-get install -y postgresql-client  
RUN apt-get install -y postgresql-contrib  
RUN apt-get install -y supervisor  
  
RUN echo "host all all 0.0.0.0/0 md5" >> /etc/postgresql/9.3/main/pg_hba.conf  
RUN echo "listen_addresses='*'" >> /etc/postgresql/9.3/main/postgresql.conf  
  
# supervisord  
RUN mkdir -p /var/log/supervisor  
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
# utility scripts  
ADD ./scripts /scripts  
RUN chmod a+x /scripts/*  
  
USER root  
EXPOSE 5432  
CMD ["/usr/bin/supervisord"]

