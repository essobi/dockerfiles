FROM ubuntu:14.04  
ENV MEMSQL_VERSION 4.0.28  
RUN apt-get update && apt-get install -yq wget  
RUN wget http://download.memsql.com/memsql-ops-$MEMSQL_VERSION/memsql-
ops-$MEMSQL_VERSION.tar.gz  
RUN wget http://download.memsql.com/releases/latest/memsqlbin_amd64.tar.gz  
RUN tar xvf memsql-ops-$MEMSQL_VERSION.tar.gz  
WORKDIR memsql-ops-$MEMSQL_VERSION  
RUN ./install.sh --no-cluster  
ADD entrypoint.sh /opt/entrypoint.sh  
RUN chmod +x /opt/entrypoint.sh  
EXPOSE 9000  
EXPOSE 3306  
CMD ["/opt/entrypoint.sh"]  

