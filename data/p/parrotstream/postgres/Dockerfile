FROM postgres:9.5  
MAINTAINER Matteo Capitanio <matteo.capitanio@gmail.com>  
  
ENV PG_MAJOR 9.5  
ENV LD_LIBRARY_PATH $LD_LIBRARY_PATH:/usr/local/lib  
  
# Install needed packages  
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-
selections  
RUN apt-get update -y; \  
apt-get install -y apt-utils; \  
apt-get install -y --no-install-recommends --force-yes git g++ pkg-config
software-properties-common cmake postgresql-server-dev-${PG_MAJOR} libpq-dev
make libproj-dev liblwgeom-dev; \  
add-apt-repository "deb http://ftp.debian.org/debian testing main contrib"; \  
apt-get update; \  
apt-get install -y libprotobuf-c-dev=1.2.*  
RUN apt-get clean all  
  
WORKDIR /  
  
# Download Debezium Postgres Decoderbufs  
RUN git clone https://github.com/debezium/postgres-decoderbufs.git  
RUN cd postgres-decoderbufs; \  
make; \  
make install; \  
rm -rf postgres-decoderbufs  
  
COPY docker-entrypoint.sh /  
RUN chmod 765 /docker-entrypoint.sh  
  
COPY pg_hba.conf /  
COPY postgresql.conf /  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
CMD ["postgres"]  

