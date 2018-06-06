FROM tiangolo/uwsgi-nginx:python2.7  
MAINTAINER Jennifer Liao <cutejaneii@hotmail.com>  
  
WORKDIR /  
  
RUN mkdir /download  
  
WORKDIR /download  
  
# Get and install software  
RUN \  
pip install flask && \  
pip install wget && \  
wget https://downloads.lightbend.com/scala/2.12.0/scala-2.12.0.tgz && \  
wget http://d3kbcqa49mib13.cloudfront.net/spark-2.0.2-bin-hadoop2.6.tgz && \  
wget --header "Cookie: oraclelicense=accept-securebackup-cookie"
http://download.oracle.com/otn-
pub/java/jdk/8u131-b11/d54c1d3a095b4ff2b6607d096fa80163/jre-8u131-linux-x64.tar.gz  
  
# unzip tgz files and move to /usr/local/  
RUN \  
tar xvf scala-2.12.0.tgz && \  
mv scala-2.12.0 /usr/local/scala && \  
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
ENV SPARK_HOME=/usr/local/spark \  
JAVA_HOME=/usr/local/jdk \  
PATH=$PATH:$SPARK_HOME:$SPARK_HOME/bin:$SPARK_HOME/python:/usr/local/spark:/usr/local/spark/bin:$JAVA_HOME/bin:$JAVA_HOME/jre/bin
\  
JRE_HOME=/usr/local/jdk/jre \  
CLASSPATH=$CLASSPATH:.:$JAVA_HOME/lib:$JAVA_HOME/jre/lib  
  
# copy nginx setting  
COPY nginx.conf /etc/nginx/conf.d/  
  
# Remove files from /app  
RUN rm -rf /app/*  
  
# Set workDir  
WORKDIR /app  

