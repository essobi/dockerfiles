FROM ubuntu:trusty  
  
#For Linode only  
#COPY sources.list /etc/apt/  
RUN locale-gen en_US en_US.UTF-8  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys
B97B0AFCAA1A47F044F244A07FCC7D46ACCC4CF8  
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ trusty-pgdg main" >
/etc/apt/sources.list.d/pgdg.list  
RUN apt-get update && apt-get install -y python-software-properties software-
properties-common postgresql-9.3 postgresql-9.3-plproxy postgresql-9.3-pgq3
postgresql-contrib-9.3 postgresql-plpython3-9.3 postgresql-server-dev-9.3 git
make protobuf-c-compiler libprotobuf-c0-dev  
RUN git clone https://github.com/citusdata/cstore_fdw.git  
RUN cd /cstore_fdw && make && make install && cd /  
#RUN git clone https://github.com/keithf4/pg_partman.git  
#RUN cd /pg_partman && make && make install  
USER postgres  
RUN /etc/init.d/postgresql start &&\  
psql --command "CREATE USER s2k WITH SUPERUSER PASSWORD '2447532';"  
RUN echo "host all all 10.0.0.0/8 trust" >>
/etc/postgresql/9.3/main/pg_hba.conf && \  
echo "host all all 192.168.0.0/16 trust" >>
/etc/postgresql/9.3/main/pg_hba.conf  
  
EXPOSE 5432  

