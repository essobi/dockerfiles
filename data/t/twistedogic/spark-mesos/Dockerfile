FROM twistedogic/mesos-serf  
MAINTAINER Jordan Li  
  
ENV MESOS_NATIVE_LIBRARY /usr/local/lib/libmesos.so  
  
ENV SPARK_VERSION 1.4.1-bin-hadoop2.6  
ENV SPARK_EXECUTOR_URI http://d3kbcqa49mib13.cloudfront.net/spark-1.4.1-bin-
hadoop2.6.tgz  
  
RUN apt-get update && \  
apt-get -y upgrade && \  
apt-get install -y curl python && \  
curl -s "${SPARK_EXECUTOR_URI}" | tar zx -C /opt && \  
mv "/opt/spark-${SPARK_VERSION}" /opt/spark && \  
rm /opt/spark/lib/spark-examples-*.jar  
  
RUN \  
echo "# Install OpenSSH Server" ;\  
apt-get -q -y install openssh-server ;\  
mkdir -p /var/run/sshd ;\  
echo 'root:passw0rd' | chpasswd ;\  
\  
true  
ADD sshd_config /etc/ssh/sshd_config  
ADD supervisord.conf /etc/supervisord.conf  
ADD start-shell.sh /start-shell.sh  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]  

