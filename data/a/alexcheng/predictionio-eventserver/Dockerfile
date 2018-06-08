FROM phusion/baseimage  
MAINTAINER Fu Cheng <alexcheng1982@gmai.com>  
  
ENV PIO_VERSION 0.9.6  
ENV SPARK_VERSION 1.6.2  
ENV PIO_HOME /PredictionIO-${PIO_VERSION}  
ENV PATH=${PIO_HOME}/bin:$PATH  
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64  
  
RUN apt-get update \  
&& apt-get install -y --auto-remove --no-install-recommends curl openjdk-8-jdk
libgfortran3 python-pip \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN curl -O http://download.prediction.io/PredictionIO-${PIO_VERSION}.tar.gz \  
&& tar -xvzf PredictionIO-${PIO_VERSION}.tar.gz -C / && mkdir -p
${PIO_HOME}/vendors \  
&& rm PredictionIO-${PIO_VERSION}.tar.gz  
COPY files/pio-env.sh ${PIO_HOME}/conf/pio-env.sh  
  
RUN curl -O http://d3kbcqa49mib13.cloudfront.net/spark-${SPARK_VERSION}-bin-
hadoop2.6.tgz \  
&& tar -xvzf spark-${SPARK_VERSION}-bin-hadoop2.6.tgz -C ${PIO_HOME}/vendors \  
&& rm spark-${SPARK_VERSION}-bin-hadoop2.6.tgz  
  
RUN ${PIO_HOME}/sbt/sbt -batch  
  
CMD ["/sbin/my_init"]  
  
RUN mkdir /etc/service/eventserver  
ADD eventserver.sh /etc/service/eventserver/run  
RUN chmod +x /etc/service/eventserver/run  

