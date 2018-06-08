FROM alpine:3.5  
LABEL maintainer "prajnamort@gmail.com"  
  
# openjdk  
RUN apk add \--no-cache openjdk8-jre  
  
# python3, pip3  
RUN apk add \--no-cache python3  
  
# psycopg2 (pip3)  
RUN apk add \--no-cache postgresql-dev \  
&& apk add \--no-cache --virtual .psycopg2-deps gcc libc-dev python3-dev \  
&& pip3 install psycopg2==2.7.1 \  
&& apk del --no-cache .psycopg2-deps  
  
# nginx  
RUN apk add \--no-cache nginx \  
&& rm /etc/nginx/conf.d/default.conf \  
&& mkdir /run/nginx  
  
# supervisor  
RUN apk add \--no-cache supervisor \  
&& mkdir -p /var/log/supervisor  
  
# oracle instant client  
RUN apk add \--no-cache --virtual .curl-deps curl \  
&& curl -o /tmp/instantclient_11_2.zip
http://olywm419i.bkt.clouddn.com/instantclient_11_2.zip \  
&& apk del --no-cache .curl-deps \  
&& unzip /tmp/instantclient_11_2.zip -d /usr/lib \  
&& rm /tmp/instantclient_11_2.zip \  
&& ln -s /usr/lib/instantclient_11_2/libclntsh.so.11.1
/usr/lib/instantclient_11_2/libclntsh.so \  
&& ln -s /usr/lib/instantclient_11_2/libocci.so.11.1
/usr/lib/instantclient_11_2/libocci.so \  
&& apk add \--no-cache libaio  
ENV LD_LIBRARY_PATH="/usr/lib/instantclient_11_2" \  
PATH="$PATH:/usr/lib/instantclient_11_2" \  
ORACLE_BASE="/usr/lib/instantclient_11_2" \  
ORACLE_HOME="/usr/lib/instantclient_11_2"  
  
# spark  
RUN apk add \--no-cache bash \  
&& apk add \--no-cache --virtual .curl-deps curl \  
&& curl -o spark-2.1.0-bin-hadoop2.7.tgz
https://d3kbcqa49mib13.cloudfront.net/spark-2.1.0-bin-hadoop2.7.tgz \  
&& apk del --no-cache .curl-deps \  
&& tar xf spark-2.1.0-bin-hadoop2.7.tgz \  
&& rm spark-2.1.0-bin-hadoop2.7.tgz \  
&& mv spark-2.1.0-bin-hadoop2.7 /usr/spark-2.1.0 \  
&& cp /usr/spark-2.1.0/conf/spark-defaults.conf.template
/usr/spark-2.1.0/conf/spark-defaults.conf \  
&& echo "spark.driver.extraClassPath $ORACLE_HOME/ojdbc6.jar" >>
/usr/spark-2.1.0/conf/spark-defaults.conf \  
&& echo "spark.executor.extraClassPath $ORACLE_HOME/ojdbc6.jar" >>
/usr/spark-2.1.0/conf/spark-defaults.conf  
ENV SPARK_HOME="/usr/spark-2.1.0" \  
PYSPARK_PYTHON=python3  

