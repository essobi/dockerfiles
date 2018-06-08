FROM openjdk:8-jdk  
  
MAINTAINER Luis David Barrios Alfonso (luisdavid.barrios@agsnasoft.com /
cyberluisda@gmail.com)  
  
ENV SNAPPY_VERSION 0.5  
ADD
https://github.com/SnappyDataInc/snappydata/releases/download/v${SNAPPY_VERSION}/snappydata-${SNAPPY_VERSION}-bin.tar.gz
/usr/lib  
RUN cd /usr/lib && tar -zxvf snappydata-${SNAPPY_VERSION}-bin.tar.gz >
/dev/null && rm -f snappydata-${SNAPPY_VERSION}-bin.tar.gz && cd \- >
/dev/null  
RUN mv /usr/lib/snappydata-${SNAPPY_VERSION}-bin /usr/lib/snappydata && rm -fr
/usr/lib/snappydata/examples /usr/lib/snappydata/quickstart && mv
/usr/lib/snappydata/conf /usr/lib/snappydata/conf-orig  
  
RUN apt-get update && apt-get --no-install-recommends -y install openssh-
server less telnet && rm -rf /var/lib/apt/lists/*  
RUN /etc/init.d/ssh start && ssh-keygen -t rsa -N '' -f ~/.ssh/id_rsa && cat
~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys  
RUN ssh-keyscan -t rsa,dsa localhost >> ~/.ssh/known_hosts && ssh-keyscan -t
rsa,dsa $(hostname) >> ~/.ssh/known_hosts  
  
ENV SNAPPY_HOME /usr/lib/snappydata  
ENV PATH $PATH:/usr/lib/snappydata/bin:/usr/lib/snappydata/sbin  
  
EXPOSE 1527  
EXPOSE 10334  
EXPOSE 4040  
EXPOSE 8090  
EXPOSE 4041  
VOLUME /var/lib/snappy-extra /var/data/spark /usr/lib/snappydata/conf  
  
WORKDIR /var/data/spark  
  
COPY files/snappy-ctl.sh /usr/lib/snappydata/bin/  
RUN chmod a+x /usr/lib/snappydata/bin/snappy-ctl.sh  
  
ENTRYPOINT ["snappy-ctl.sh"]  
CMD ["--help"]  

