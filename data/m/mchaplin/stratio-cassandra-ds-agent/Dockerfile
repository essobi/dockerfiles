FROM inovatrend/java8  
  
# Add Datastax repository to sources  
RUN echo "deb http://debian.datastax.com/community stable main" | sudo tee -a
/etc/apt/sources.list.d/cassandra.sources.list  
RUN curl -L http://debian.datastax.com/debian/repo_key | sudo apt-key add -  
  
# Install datastax agent, SSH server, supervisor  
RUN apt-get update  
RUN apt-get -y install openssh-server datastax-agent supervisor  
RUN ln -s /var/lib/datastax-agent/conf /etc/datastax-agent  
  
# Setup datastax-agent  
RUN if [ -z "`getent passwd dsagent`" ]; then adduser --quiet --system --home
/home/dsagent --shell /bin/bash --ingroup cassandra --disabled-password
--gecos "Opscenter agent" dsagent 2> /dev/null && usermod -a -G operator
dsagent ; fi  
RUN mkdir -p /home/dsagent/.ssh  
ADD src/authorized_keys /home/dsagent/.ssh/authorized_keys  
  
ADD src/dsagent-sudoers /etc/sudoers.d/dsagent-sudoers  
RUN chmod 440 /etc/sudoers.d/dsagent-sudoers && chmod 440
/home/dsagent/.ssh/authorized_keys  
  
# Install cassandra manually  
WORKDIR /  
RUN if [ -z "`getent passwd cassandra`" ]; then useradd cassandra ; fi  
  
# Use apache public release  
# RUN wget -O /tmp/cassandra.tgz
http://mir2.ovh.net/ftp.apache.org/dist/cassandra/2.1.2/apache-
cassandra-2.1.2-bin.tar.gz && tar zxvf /tmp/cassandra.tgz && mv /apache-
cassandra* /cassandra && rm /tmp/cassandra.tgz && mkdir -p /etc/cassandra &&
ln -s /cassandra/conf /etc/cassandra/conf && chown -R cassandra /cassandra  
# Alternative, use stratio cassandra fork with lucene support  
ADD stratio-cassandra-2.1.2.2.tar.gz /tmp  
RUN mv /tmp/stratio-cassandra* /cassandra && mkdir -p /etc/cassandra && ln -s
/cassandra/conf /etc/cassandra/conf && mkdir -p /cassandra/data && chown -R
cassandra /cassandra  
ENV PATH $PATH:/cassandra/bin  
  
# Configure supervisord  
ADD src/supervisord.conf /etc/supervisor/supervisord.conf  
RUN mkdir -p /var/log/supervisor  
  
# Deploy startup script  
ADD src/start.sh /usr/local/bin/start  
ADD src/start-dsagent.sh /usr/local/bin/start-dsagent  
RUN chmod 755 /usr/local/bin/start && chmod 755 /usr/local/bin/start-dsagent  
  
EXPOSE 7199 7000 7001 9160 9042  
USER root  
CMD start  
#CMD /bin/bash  
# Clean up  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

