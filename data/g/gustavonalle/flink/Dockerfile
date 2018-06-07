FROM alpine:3.3  
MAINTAINER gustavonalle  
  
ENV FLINK_VERSION 1.0.3  
ENV FLINK_HADOOP hadoop27  
  
RUN echo "http://dl-4.alpinelinux.org/alpine/edge/community" >>
/etc/apk/repositories \  
&& apk add --update \  
curl openjdk8 openssh ruby bash cracklib-words supervisor procps \  
&& rm /var/cache/apk/*  
  
RUN curl
"http://www.mirrorservice.org/sites/ftp.apache.org/flink/flink-$FLINK_VERSION/flink-$FLINK_VERSION-
bin-$FLINK_HADOOP-scala_2.10.tgz" | tar -C /usr/local/ -xz | ln -s
/usr/local/flink-$FLINK_VERSION/ /usr/local/flink  
  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
USER root  
RUN ssh-keygen -q -N "" -t dsa -f /etc/ssh/ssh_host_dsa_key  
RUN ssh-keygen -q -N "" -t rsa -f /etc/ssh/ssh_host_rsa_key  
RUN ssh-keygen -q -N "" -t rsa -f /root/.ssh/id_rsa  
RUN cp /root/.ssh/id_rsa.pub /root/.ssh/authorized_keys  
  
ADD ssh_config /root/.ssh/config  
ADD start-cluster-wrapper.sh /usr/local/flink/bin/start-cluster-wrapper.sh  
RUN chmod 600 /root/.ssh/config  
RUN chown root:root /root/.ssh/config  
  
CMD ["/usr/bin/supervisord","-c","/etc/supervisor/conf.d/supervisord.conf"]  
  
EXPOSE 22 6123 8080 8081  

