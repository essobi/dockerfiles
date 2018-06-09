FROM postgres:9.4  
MAINTAINER Florian Sachs "florian.sachs@gmx.at"  
RUN apt-get update && apt-get install -y vim && rm -rf /var/lib/apt/lists/*  
RUN echo '[[ -f /etc/profile ]] && . /etc/profile' >> /root/.profile  
COPY set_bash_environment.sh /etc/profile.d/  
  
COPY logstash.conf /etc/logstash.conf  
  
COPY update-logging-config.sh /docker-entrypoint-initdb.d/update-logging-
config.sh  
COPY copy-logstash.conf.sh /docker-entrypoint-initdb.d/copy-logstash.conf.sh  
COPY chown-logs.sh /docker-entrypoint.d/chown-logs.sh  
  
COPY set-postgres-password.sh /docker-entrypoint.d/set-postgres-password.sh  
  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
RUN chmod 0755 /docker-entrypoint.sh  
  
RUN mkdir -p /logs /docker-entrypoint-initdb.d  
RUN chown postgres:postgres /logs  
  

