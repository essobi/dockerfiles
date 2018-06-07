FROM debian:jessie  
  
MAINTAINER Arthur <arthur@corenzan.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update  
  
COPY locale.txt /tmp/  
RUN debconf-set-selections /tmp/locale.txt  
  
RUN apt-get install -y locales  
  
ENV LC_ALL en_US.UTF-8  
RUN apt-get install -y --no-install-recommends postgresql-9.4 postgresql-
contrib-9.4  
  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN echo "host all all 0.0.0.0/0 md5" >> /etc/postgresql/9.4/main/pg_hba.conf  
RUN echo "listen_addresses='*'" >> /etc/postgresql/9.4/main/postgresql.conf  
  
ENV PATH /usr/lib/postgresql/9.4/bin:$PATH  
  
RUN mkdir /var/run/postgresql/9.4-main.pg_stat_tmp/ && chown -R
postgres:postgres /var/run/postgresql  
  
EXPOSE 5432  
VOLUME ["/etc/postgresql/9.4/main", "/var/lib/postgresql/9.4/main"]  
  
COPY postgresql.sh /  
CMD ["/postgresql.sh"]  

