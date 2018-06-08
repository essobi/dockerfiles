FROM postgres:9.4  
RUN apt-get update && apt-get install -y unixodbc unixodbc-dev unixodbc-bin
libodbc1 odbcinst1debian2 tdsodbc freetds-bin freetds-common freetds-dev
libct4 libsybdb5 wget make postgresql-server-dev-9.4 gcc  
  
RUN wget https://github.com/GeoffMontee/tds_fdw/archive/v1.0.7.tar.gz \  
&& tar -xvzf v1.0.7.tar.gz \  
&& cd tds_fdw-1.0.7 \  
&& make USE_PGXS=1 \  
&& make USE_PGXS=1 install  
  
COPY freetds.conf /etc/freetds/  
COPY odbc.ini /etc/  
COPY odbcinst.ini /etc/  

