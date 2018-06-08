FROM idio/java-7  
MAINTAINER David Przybilla <david.przybilla@idioplatform.com>  
  
ENV SPARK_VERSION "1.3.1"  
ENV SPARK_PATH "/spark-${SPARK_VERSION}-bin-hadoop2.4"  
ENV SPARK_FILE "spark-${SPARK_VERSION}-bin-hadoop2.4.tgz"  
ENV SPARK_URL
"http://www.mirrorservice.org/sites/ftp.apache.org/spark/spark-1.3.1/${SPARK_FILE}"  
ADD $SPARK_URL /  
RUN tar -xvf $SPARK_FILE  
RUN ln -s $SPARK_PATH /var/lib/spark

