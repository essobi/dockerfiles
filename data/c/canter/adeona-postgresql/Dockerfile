  
# The installer  
FROM postgres:10-alpine as installer  
  
ENV PGAMQPVERSION v0.4.1  
RUN pg_config --libdir  
  
RUN apk -U add \  
alpine-sdk \  
perl \  
build-base \  
&& git clone https://github.com/omniti-labs/pg_amqp.git pg_amqp \  
&& cd pg_amqp \  
&& git checkout ${PGAMQPVERSION}  
  
# PATCH pg_amqp to build in alpine  
RUN cd pg_amqp \  
&& echo "#include <sys/time.h>" > patch.txt \  
&& echo "typedef struct timeval timeval;" >> patch.txt \  
&& cat ./src/librabbitmq/amqp.h >> patch.txt \  
&& cat patch.txt > ./src/librabbitmq/amqp.h  
  
RUN cd pg_amqp && cat ./src/librabbitmq/amqp.h  
  
RUN cd pg_amqp \  
&& make \  
&& make install  
  
RUN ls -la /usr/local/share/postgresql/extension/  
  
# The image  
FROM postgres:10-alpine  
  
COPY \--from=installer /usr/local/share/postgresql/extension/amqp*
/usr/local/share/postgresql/extension/  
COPY \--from=installer /usr/local/lib/postgresql/pg_amqp*
/usr/local/lib/postgresql/  
  
COPY ./docker-entrypoint-initdb.d/* /docker-entrypoint-initdb.d/  
  
LABEL maintainer="Tuomas Lehtonen" \  
description="PIM postgres image" \  
version="10-alpine"  
  
EXPOSE 5432

