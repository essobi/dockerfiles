FROM python:2.7  
MAINTAINER Jennifer Liao <cutejaneii@hotmail.com>  
  
# Install uWSGI & flask  
RUN pip install uwsgi  
  
RUN \  
pip install flask && \  
pip install wget && \  
wget https://downloads.lightbend.com/scala/2.11.11/scala-2.11.11.tgz && \  
wget http://d3kbcqa49mib13.cloudfront.net/spark-2.0.2-bin-hadoop2.6.tgz && \  
wget --header "Cookie: oraclelicense=accept-securebackup-cookie"
http://download.oracle.com/otn-
pub/java/jdk/8u131-b11/d54c1d3a095b4ff2b6607d096fa80163/jre-8u131-linux-x64.tar.gz  
  
RUN apt-get update  
RUN apt-get -y install python-pip  
RUN pip install kafka-python  
  
# unzip tgz files and move to /usr/local/  
RUN \  
tar xvf scala-2.11.11.tgz && \  
mv scala-2.11.11 /usr/local/scala && \  
tar xvf spark-2.0.2-bin-hadoop2.6.tgz && \  
mv spark-2.0.2-bin-hadoop2.6 /usr/local/spark && \  
tar xvf jre-8u131-linux-x64.tar.gz && \  
mv jre1.8.0_131 /usr/local/jre  
  
# Install py4j / Cassandra-driver / pandas  
RUN \  
pip install py4j && \  
pip install cassandra-driver && \  
pip install pandas  
  
# Environment variables  
ENV NGINX_VERSION 1.9.11-1~jessie  
  
ENV SPARK_HOME=/usr/local/spark  
ENV JAVA_HOME=/usr/local/jre \  
PATH=$PATH:$SPARK_HOME:$SPARK_HOME/bin:$SPARK_HOME/python:$JAVA_HOME/bin \  
JRE_HOME=/usr/local/jdk/jre \  
CLASSPATH=$CLASSPATH:.:$JAVA_HOME/lib:$JAVA_HOME/jre/lib  
  
RUN apt-key adv --keyserver hkp://pgp.mit.edu:80 --recv-keys
573BFD6B3D8FBC641079A6ABABF5BD827BD9BF62 \  
&& echo "deb http://nginx.org/packages/mainline/debian/ jessie nginx" >>
/etc/apt/sources.list \  
&& apt-get update \  
&& apt-get install -y ca-certificates nginx=${NGINX_VERSION} gettext-base \  
&& rm -rf /var/lib/apt/lists/*  
  
# forward request and error logs to docker log collector  
RUN ln -sf /dev/stdout /var/log/nginx/access.log \  
&& ln -sf /dev/stderr /var/log/nginx/error.log  
  
ENV PYTHONPATH=$PYTHONPATH:$SPARK_HOME:$SPARK_HOME/bin:$SPARK_HOME/python  
  
# Make NGINX run on the foreground  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf  
  
# Download jars  
RUN mkdir /usr/local/spark_jars  
  
WORKDIR /usr/local/spark_jars  
  
COPY /spark_jars/spark-streaming-kafka-0-8-assembly_2.11-2.0.2.jar
/usr/local/spark_jars/spark-streaming-kafka-0-8-assembly_2.11-2.0.2.jar  
  
COPY /spark_jars/spark-cassandra-connector-2.0.0-M2-s_2.11.jar
/usr/local/spark_jars/spark-cassandra-connector_2.0.0-M2-s_2.11.jar  
  
COPY /spark_jars/jsr166e-1.1.0.jar /usr/local/spark_jars/jsr166e-1.1.0.jar  
  
# Copy spark-defaults.conf to add spark.driver.extraClassPath  
COPY spark-defaults.conf /usr/local/spark/conf/spark-defaults.conf  
  
# Remove default configuration from Nginx  
RUN rm /etc/nginx/conf.d/default.conf  
  
# Copy the modified Nginx conf  
COPY nginx.conf /etc/nginx/conf.d/  
  
# Copy uWSGI emperor.ini to monitor /etc/uwsgi/vassals folder  
COPY emperor.ini /etc/uwsgi/  
  
# This dir will be monitored by uwsgi emperor  
RUN mkdir /etc/uwsgi/vassals  
  
# Install Supervisord  
RUN apt-get update && apt-get install -y supervisor \  
&& rm -rf /var/lib/apt/lists/*  
# Custom Supervisord config  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
COPY ./app /app  
COPY ./vassals /etc/uwsgi/vassals  
  
WORKDIR /app  
  
CMD ["/usr/bin/supervisord"]  

