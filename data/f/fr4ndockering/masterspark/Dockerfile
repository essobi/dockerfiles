FROM ubuntu:16.04  
WORKDIR /root  
  
USER root  
  
RUN apt-get update && apt-get install -y openssh-client sshpass nano  
  
RUN apt-get install -y wget unzip openjdk-8-jdk  
  
RUN ssh-keygen -t rsa -f ~/.ssh/id_rsa -P '' && cat ~/.ssh/id_rsa.pub >>
~/.ssh/authorized_keys  
  
RUN wget https://archive.apache.org/dist/spark/spark-2.1.1/spark-2.1.1-bin-
hadoop2.7.tgz && tar xvf spark-2.1.1-bin-hadoop2.7.tgz && mkdir /opt/spark &&
mv spark-2.1.1-bin-hadoop2.7/* /opt/spark && rm -rf spark-2.1.1-bin*  
  
RUN wget
http://apache.rediris.es/incubator/livy/0.4.0-incubating/livy-0.4.0-incubating-
bin.zip && unzip livy-0.4.0-incubating-bin.zip && mkdir /opt/livy && mv
livy-0.4.0-incubating-bin/* /opt/livy && rm -rf livy*  
  
ENV JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64  
  
ENV PATH="$PATH:/opt/spark/bin:/opt/spark/sbin:/opt/livy/bin"
SPARK_HOME="/opt/spark"  
EXPOSE 8998  
EXPOSE 7077  
EXPOSE 8080  
EXPOSE 2222  
EXPOSE 22  
EXPOSE 4040  
EXPOSE 8081  
EXPOSE 6066  
COPY ej.sh .  
  
RUN chmod 700 ej.sh  
  
#ENTRYPOINT ["sh","-c","./ej.sh"]  
#ENTRYPOINT ["sh","-c","ssh-keyscan nodo >> ~/.ssh/known_hosts && sshpass -p
'root' ssh-copy-id -i ~/.ssh/id_rsa.pub root@nodo"]  

