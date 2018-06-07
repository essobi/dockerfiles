FROM postgres:9.5  
RUN apt-get -y update  
RUN apt-get -y install git postgresql-server-dev-9.5 make gcc  
WORKDIR /tmp  
RUN git clone https://github.com/omniti-labs/pg_amqp.git  
WORKDIR /tmp/pg_amqp  
RUN make  
RUN make install  

