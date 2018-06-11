FROM ubuntu:14.04  
MAINTAINER Carlos Killpack <carlos@zulumarketing.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN locale-gen en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US.UTF-8  
  
VOLUME ["/var/lib/postgresql"]  
  
COPY ./postgresql-wrapper.sh /usr/bin/postgresql-wrapper  
  
RUN apt-get update > /dev/null \  
&& apt-get upgrade -y > /dev/null \  
&& apt-get install -y postgresql > /dev/null \  
&& apt-get clean > /dev/null  
  
COPY postgresql.conf /etc/postgresql/9.3/main/postgresql.conf  
COPY pg_hba.conf /etc/postgresql/9.3/main/pg_hba.conf  
  
USER postgres  
EXPOSE 5432  
CMD ["/usr/bin/postgresql-wrapper", \  
"-D /var/lib/postgresql/9.3/main", \  
"--config-file=/etc/postgresql/9.3/main/postgresql.conf"]  

