FROM debian:jessie-slim  
MAINTAINER Earvin Kayonga <earvin@earvinkayonga.com>  
  
  
ENV RETHINKDB_VERSION 2.3.5  
ENV BRANCH v2.4.x  
  
#  
# DEPENDENCIES  
#  
RUN apt-get clean && apt-get update -qq && apt-get upgrade -y && \  
apt-get install -y apt-utils \  
curl \  
build-essential \  
protobuf-compiler \  
python \  
git \  
libprotobuf-dev \  
libboost-all-dev \  
libncurses5-dev \  
libjemalloc-dev wget m4 libicu-dev  
  
#  
# BUILDING FROM SOURCES  
#  
RUN git clone https://github.com/rethinkdb/rethinkdb.git  
  
VOLUME /data  
WORKDIR /rethinkdb  
  
RUN git checkout $BRANCH  
  
# cd rethinkdb  
RUN ./configure --with-system-malloc --allow-fetch --fetch node --fetch
openssl --fetch npm --dynamic jemalloc  
RUN make clean  
RUN make build-openssl  
RUN make -j 4 ALLOW_WARNINGS=1  
RUN make install  
  
#  
# RUN THE SERVER  
#  
CMD ["rethinkdb", "--bind", "all"]  
  
# process cluster webui  
EXPOSE 28015 29015 8080  

