FROM flowdocker/postgresql:0.0.87  
ADD . /opt/schema  
WORKDIR /opt/schema  
  
RUN echo "set -x #echo on" >> /opt/run.sh  
RUN echo "service postgresql start" >> /opt/run.sh  
RUN echo "sh /opt/schema/install.sh" >> /opt/run.sh  
RUN echo "service postgresql stop" >> /opt/run.sh  
  
RUN sh /opt/run.sh  
  
USER "postgres"  
CMD ["/usr/lib/postgresql/10/bin/postgres", "-i", "-D",
"/var/lib/postgresql/10/main"]  

