FROM phusion/baseimage  
MAINTAINER Kaiden Prince  
  
RUN echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main" >>
/etc/apt/sources.list \  
&& echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main"
>> /etc/apt/sources.list \  
&& apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EEA14886
\  
&& echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true
| /usr/bin/debconf-set-selections \  
&& apt-get update && apt-get upgrade -y && apt-get -y dist-upgrade \  
&& apt-get -y install oracle-java8-installer  
ENV JAVA_HOME=/usr/lib/jvm/java-8-oracle  
  
RUN curl -sL https://deb.nodesource.com/setup_7.x | bash - && \  
apt-get install -y nodejs python \  
&& apt-get -y install oracle-java8-installer  
  
RUN echo "deb http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.4
multiverse" >> /etc/apt/sources.list \  
&& apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv
0C49F3730359A14518585931BC711F9BA15703C6 \  
&& apt-get update && apt-get upgrade -y && apt-get -y dist-upgrade \  
&& apt-get install -y mongodb-org  
  
RUN apt-get update && apt-get upgrade -y && apt-get -y dist-upgrade \  
&& apt-get -y install tmux xz-utils sudo \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN rm -f /etc/service/sshd/down  
  
EXPOSE 22  
EXPOSE 25565  
EXPOSE 25565/udp  
  
VOLUME /data  
VOLUME /backup  
VOLUME /etc/ssh  
  
RUN useradd mc -m -s /bin/bash && usermod -p '*' mc && \  
ln -s /data /home/mc/data && \  
ln -s /backup /home/mc/backup && \  
chown mc:mc -R /home/mc  
  
RUN mkdir -p /etc/my_init.d && chown mc:mc -R /data  
ADD dockerFiles/service /etc/service  
ADD dockerFiles/my_init.d /etc/my_init.d  
ADD dockerFiles/scripts /scripts  
ADD dockerFiles/crontab /tmp  
  
RUN chmod +x /etc/my_init.d/*.sh /etc/service/*/run /scripts/* && \  
echo 'PATH=$PATH:/scripts' >> /etc/profile && \  
cat /tmp/crontab >> /etc/crontab && \  
echo >> /etc/crontab && \  
echo "mc ALL=(root) NOPASSWD: /usr/bin/sv, (root) NOPASSWD: /scripts/mc" >>
/etc/sudoers  
  
ADD app /usr/src/app

