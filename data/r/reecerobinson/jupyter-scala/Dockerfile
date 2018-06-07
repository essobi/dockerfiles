FROM reecerobinson/jupyter:1.6.0  
MAINTAINER docker@reecerobinson.co.nz  
  
ENV APACHE_SPARK_VERSION=1.6.0  
ENV SPARK_HOME /usr/local/spark  
ENV PATH $PATH:$SPARK_HOME/bin  
ENV USE_VAGRANT=false  
ENV IS_SNAPSHOT=false  
  
RUN git clone https://github.com/ibm-et/spark-kernel.git  
RUN echo "deb http://dl.bintray.com/sbt/debian /" | tee -a
/etc/apt/sources.list.d/sbt.list && \  
apt-get update && \  
apt-get install --force-yes -y sbt && \  
apt-get clean  
  
WORKDIR /root/spark-kernel  
RUN sed -i s/'USE_VAGRANT?='/''/g /root/spark-kernel/Makefile \  
&& sed -i s/'IS_SNAPSHOT?=true'/''/g /root/spark-kernel/Makefile \  
&& sed -i s/'RUN_PREFIX=$(if $(USE_VAGRANT),vagrant ssh -c "cd $(VM_WORKDIR)
&& )'/''/g /root/spark-kernel/Makefile \  
&& sed -i s/'RUN_SUFFIX=$(if $(USE_VAGRANT),")'/''/g /root/spark-
kernel/Makefile  
  
RUN sbt exit  
  
RUN make dist && rm -rf /root/.ivy2  
RUN mkdir /root/local && cd /root/local && tar -xzvf /root/spark-
kernel/dist/spark-kernel-0.1.5.tar.gz  
  
COPY kernels /root/.ipython/kernels  
  
RUN cp $SPARK_HOME/lib/elasticsearch-spark_2.10-2.2.0-rc1.jar
/root/local/spark-kernel/lib && \  
cp $SPARK_HOME/lib/cassandra-clientutil-2.2.2.jar /root/local/spark-kernel/lib
&& \  
cp $SPARK_HOME/lib/cassandra-driver-core-3.0.0-rc1.jar /root/local/spark-
kernel/lib && \  
cp $SPARK_HOME/lib/guava-16.0.1.jar /root/local/spark-kernel/lib  
  

