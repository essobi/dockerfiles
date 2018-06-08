FROM java:jdk  
  
ENV DEBIAN_FRONTEND noninteractive  
  
ADD https://repo1.maven.org/maven2/com/facebook/presto/presto-
server/0.185/presto-server-0.185.tar.gz \  
/tmp/presto.tar.gz  
  
RUN mkdir -p /opt/presto &&\  
tar -zxvf /tmp/presto.tar.gz -C /opt/presto &&\  
rm /tmp/presto.tar.gz  
  
RUN mv /opt/presto/presto-server-0.185 /opt/presto/presto-server  
  
ENV HOME /opt/presto  
  
WORKDIR $HOME  
  
# copy default set of config  
COPY config/ $HOME/presto-server/etc/  
  
# Copy additional plugins  
COPY plugin/ $HOME/presto-server/plugin/  
  
# adding the config mounting point  
VOLUME $HOME/presto-server/etc/  
  
# adding the data mounting point  
VOLUME $HOME/presto-data/  
  
EXPOSE 8080  
CMD ["presto-server/bin/launcher", "run"]

