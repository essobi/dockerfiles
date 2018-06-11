FROM ubuntu:16.04  
WORKDIR /root  
  
USER root  
  
RUN apt-get update && apt-get install -y wget unzip openssh-server  
  
RUN apt-get install -y openjdk-8-jdk nano  
  
RUN wget https://archive.apache.org/dist/spark/spark-2.1.1/spark-2.1.1-bin-
hadoop2.7.tgz && tar xvf spark-2.1.1-bin-hadoop2.7.tgz && mkdir /opt/spark &&
mv spark-2.1.1-bin-hadoop2.7/* /opt/spark && rm -rf spark-2.1.1-bin*  
  
RUN mkdir /var/run/sshd  
  
RUN echo 'root:root' | chpasswd  
  
RUN sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin yes/'
/etc/ssh/sshd_config  
  
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config  
  
ENV JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64  
  
ENV PATH="$PATH:/opt/spark/bin:/opt/spark/sbin:/opt/livy/bin"
SPARK_HOME="/opt/spark"  
EXPOSE 22  
EXPOSE 8080  
EXPOSE 7077  
EXPOSE 8998  
EXPOSE 2222  
EXPOSE 4040  
EXPOSE 8081  
EXPOSE 6066  
#CMD ["/usr/sbin/sshd","-D"]  

