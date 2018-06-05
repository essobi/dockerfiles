# Creates an Ambari Server based on vanilla CentOS  
#  
#To build the image use:  
#  
#git clone https://github.com/sequenceiq/docker-ambari.git  
#cd docker-ambari  
# git checkout 2.0.0  
# docker build -t sequenceiq/ambari:2.0.0 ./ambari-server/  
#  
#To build the image  
#docker pull sequenceiq/ambari:2.0.0  
FROM sequenceiq/dnsmasq:pam-fix  
MAINTAINER SequenceIQ  
  
ADD ambari.repo /etc/yum.repos.d/  
RUN yum install -y ambari-server ambari-agent  
RUN yum install -y tar git curl  
  
RUN ambari-server setup --silent  
  
ADD serf /usr/local/serf  
  
# instead of starting the docker file FROM sequenceiq/ssh:  
RUN yum install -y curl  
RUN curl -L https://api.github.com/repos/sequenceiq/docker-
ssh/tarball/master|tar -xz -C /usr/local/serf --strip-components=2 --touch
\\*/serf  
RUN curl -L https://raw.githubusercontent.com/sequenceiq/docker-
ssh/master/install-ssh.sh | bash  
  
# fix annoying PAM error 'couldnt open session'  
RUN sed -i "/pam_limits/ s/^/#/" /etc/pam.d/*  
  
# warm up the image  
ADD hdp.repo /etc/yum.repos.d/  
RUN yum install -y ambari-log4j hadoop hadoop-libhdfs hadoop-lzo hadoop-lzo-
native hadoop-mapreduce hadoop-mapreduce-historyserver hadoop-yarn hadoop-
yarn-nodemanager hadoop-yarn-proxyserver hadoop-yarn-resourcemanager lzo net-
snmp net-snmp-utils snappy snappy-devel unzip zookeeper hbase slider storm
hive hive_2_3_*-hcatalog hive_2_3_*-webhcat mysql-connector-java mysql-server
datafu ranger phoenix kafka pig ambari-metrics-* rpcbind && yum clean all  
  
# add ambari shell to the image so new users don't need the 1GB java image  
RUN curl -o /tmp/ambari-shell.jar https://s3-eu-
west-1.amazonaws.com/maven.sequenceiq.com/releases/com/sequenceiq/ambari-
shell/0.1.25/ambari-shell-0.1.25.jar  
ADD blueprints /tmp/blueprints  
ADD install-cluster.sh /tmp/  
ADD wait-for-host-number.sh /tmp/  
ADD ambari-shell.sh /tmp/  
ENV JAVA_HOME /usr/jdk64/jdk1.8.0_40  
ENV PATH $JAVA_HOME/bin:$PATH  
WORKDIR /tmp  
  
# add HIVE view jar - before ambari-server setup  
RUN curl -o /var/lib/ambari-server/resources/views/hive-0.1.0-SNAPSHOT.jar
https://s3-eu-
west-1.amazonaws.com/sequenceiq/hive-0.1.0-20150306.030234-109.jar  
  
# fixing pgsql issue  
RUN rm -rf /tmp/.s.PGSQL.5432.*  
  
ADD public-hostname.sh /etc/ambari-agent/conf/public-hostname.sh  
ADD internal-hostname.sh /etc/ambari-agent/conf/internal-hostname.sh  
RUN sed -i "/\\[agent\\]/ a public_hostname_script=\/etc\/ambari-
agent\/conf\/public-hostname.sh" /etc/ambari-agent/conf/ambari-agent.ini  
RUN sed -i "/\\[agent\\]/ a hostname_script=\/etc\/ambari-
agent\/conf\/internal-hostname.sh" /etc/ambari-agent/conf/ambari-agent.ini  
  
RUN mkdir /var/log/hadoop-metrics && chmod 777 /var/log/hadoop-metrics  
RUN mkdir /var/log/httpd  
ADD hadoop-metrics2.properties.j2 /var/lib/ambari-
server/resources/stacks/HDP/2.0.6/hooks/before-START/templates/hadoop-
metrics2.properties.j2  
  
# Error: database disk image is malformed  
#ADD 00_dbclean.sh /usr/local/init/00_dbclean.sh  
VOLUME /var/log  
  
# increase agent timeout  
RUN sed -i "s/agent.task.timeout=900/agent.task.timeout=2000/" /etc/ambari-
server/conf/ambari.properties  
  
EXPOSE 2181 3773 3772 6627 8000 8020 8032 8080 8088 8744 9933 9999 10000 16010
19888 50060 50070 50075 50470 50475  
ENTRYPOINT ["/usr/local/serf/bin/start-serf-agent.sh"]  
CMD ["--log-level", "debug"]  

