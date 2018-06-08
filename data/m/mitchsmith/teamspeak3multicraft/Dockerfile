FROM ubuntu:latest  
  
ARG
TEAMSPEAK_URL=http://dl.4players.de/ts/releases/3.2.0/teamspeak3-server_linux_amd64-3.2.0.tar.bz2  
ARG TS_DIRECTORY=/opt/ts3  
  
RUN apt-get -y update && apt-get -y install wget && apt-get -y install nodejs  
  
RUN mkdir /opt/shockbyte-wrapper && cd /opt/shockbyte-wrapper && wget -q -O
wrapper.js http://switchbladed.com/wrapper/shockbyte.php && chmod 555
wrapper.js && chmod 111 /opt/shockbyte-wrapper  
  
RUN wget ${TEAMSPEAK_URL} -O "/tmp/teamspeak.tar.bz2" &&\  
tar jxf /tmp/teamspeak.tar.bz2 -C /opt &&\  
mv /opt/teamspeak3-server_* ${TS_DIRECTORY} &&\  
rm /tmp/teamspeak.tar.bz2  
  
# set the locale  
RUN apt-get -y install locales  
RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen  
RUN locale-gen  
  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
  
RUN mkdir /data &&\  
mkdir /data/files &&\  
mkdir /data/logs &&\  
#ln -s /data/ts3server.sqlitedb /opt/ts3/ts3server.sqlitedb &&\  
#ln -s /data/files /opt/ts3/files &&\  
#ln -s /data/logs /opt/ts3/logs &&\  
useradd -r docker &&\  
chown -R docker:docker ${TS_DIRECTORY} /data  
  
#COPY entrypoint.sh /opt/entrypoint.sh  
#RUN chown docker:docker /opt/entrypoint.sh && chmod 555 /opt/entrypoint.sh  
  
#RUN ln -s /data/ts3server.sqlitedb /opt/ts3/ts3server.sqlitedb &&\  
# ln -s /data/files /opt/ts3/files &&\  
# ln -s /data/logs /opt/ts3/logs  
  
USER docker:docker  
# external install script  
#ENTRYPOINT ["/opt/entrypoint.sh"]  

