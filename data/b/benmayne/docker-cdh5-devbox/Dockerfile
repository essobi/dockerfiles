FROM factual/docker-cdh5-dev  
  
# switching spark versions  
ARG SPARK_VERSION=2.3.0  
ARG SPARK_HOME=/opt/spark  
RUN rm -rf $SPARK_HOME  
  
#Spark  
ADD
http://archive.apache.org/dist/spark/spark-$SPARK_VERSION/spark-$SPARK_VERSION-
bin-hadoop2.6.tgz /tmp/  
RUN cd /tmp/ && tar xzf spark-$SPARK_VERSION-bin-hadoop2.6.tgz && mv
spark-$SPARK_VERSION-bin-hadoop2.6 $SPARK_HOME  
RUN echo "export PATH=$SPARK_HOME/bin:\$PATH" >> /etc/profile  
RUN echo "export HADOOP_CONF_DIR=$HADOOP_CONF_DIR" >> /etc/profile  
RUN echo "export SPARK_HOME=$SPARK_HOME" >> /etc/profile  
RUN mkdir -p /etc/spark/ && ln -s $SPARK_HOME/conf /etc/spark/conf  
RUN cp /usr/lib/hadoop/lib/hadoop-lzo.jar $SPARK_HOME/jars/  
  
RUN rm -f /etc/service/sshd/down  
RUN /etc/my_init.d/00_regen_ssh_host_keys.sh  
ADD sshd_config /etc/ssh/  
  
RUN mkdir -p /share  
RUN mkdir -p /local  
  
RUN apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys
58118E89F3A912897C070ADBF76221572C52609D  
RUN echo "deb https://apt.dockerproject.org/repo ubuntu-xenial main" >>
/etc/apt/sources.list.d/docker.list  
  
RUN apt-get update && apt-get install -y byobu docker-engine python3-pip bash-
completion s3cmd awscli  
  
RUN mkdir -p /etc/service/docker  
ADD docker.sh /etc/service/docker/run  
  
#cleanup  
RUN apt-get clean  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
VOLUME ["/home","/share", "/local"]  

