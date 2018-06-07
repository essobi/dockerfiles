FROM alpine:3.3  
MAINTAINER gustavonalle  
  
ENV HADOOP_VERSION 2.7.2  
RUN echo "http://dl-4.alpinelinux.org/alpine/edge/community" >>
/etc/apk/repositories \  
&& apk add --update \  
curl openjdk8 openssh ruby bash cracklib-words supervisor procps \  
&& rm /var/cache/apk/*  
  
RUN curl
"http://mirrors.ukfast.co.uk/sites/ftp.apache.org/hadoop/common/hadoop-$HADOOP_VERSION/hadoop-$HADOOP_VERSION.tar.gz"
| tar -C /usr/local/ -xz | ln -s /usr/local/hadoop-$HADOOP_VERSION/
/usr/local/hadoop && rm -Rf /usr/local/hadoop/share/doc/  
  
ADD hadoop_home.sh /etc/profile.d/hadoop_home.sh  
  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
ADD core-site.xml /usr/local/hadoop/etc/hadoop/core-site.xml  
ADD hdfs-site.xml /usr/local/hadoop/etc/hadoop/hdfs-site.xml  
ADD mapred-site.xml /usr/local/hadoop/etc/hadoop/mapred-site.xml  
ADD yarn-site.xml /usr/local/hadoop/etc/hadoop/yarn-site.xml  
ADD start-wrapper.sh /usr/local/hadoop/sbin/start-wrapper.sh  
  
USER root  
RUN ssh-keygen -q -N "" -t dsa -f /etc/ssh/ssh_host_dsa_key  
RUN ssh-keygen -q -N "" -t rsa -f /etc/ssh/ssh_host_rsa_key  
RUN ssh-keygen -q -N "" -t rsa -f /root/.ssh/id_rsa  
RUN cp /root/.ssh/id_rsa.pub /root/.ssh/authorized_keys  
  
ADD ssh_config /root/.ssh/config  
RUN chmod 600 /root/.ssh/config  
RUN chown root:root /root/.ssh/config  
  
ENV JAVA_HOME /usr/lib/jvm/default-jvm  
ENV PATH ${JAVA_HOME}/bin:${PATH}  
  
RUN sed -i -e 's/JAVA=\$JAVA_HOME\/bin\/java/JAVA=\/usr\/lib\/jvm\/default-
jvm\/bin\/java/' /usr/local/hadoop/etc/hadoop/yarn-env.sh  
RUN sed -i -e 's/export JAVA_HOME=${JAVA_HOME}/export
JAVA_HOME=\/usr\/lib\/jvm\/default-jvm\//'
/usr/local/hadoop/etc/hadoop/hadoop-env.sh  
  
RUN /bin/bash -l -c "hdfs namenode -format"  
  
CMD ["/usr/bin/supervisord","-c","/etc/supervisor/conf.d/supervisord.conf"]  
  
EXPOSE 22 80 8020 8030 8031 8032 8033 8042 8080 8088 9000 9001 50010 50020
50030 50065 50060 50070 50075 50090 50470 50475  

