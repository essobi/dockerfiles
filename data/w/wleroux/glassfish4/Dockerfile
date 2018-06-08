FROM ubuntu:latest  
MAINTAINER Wayne Leroux <WayneLeroux@gmail.com>  
  
# Update System  
RUN DEBIAN_FRONTEND=noninteractive dpkg-divert --local \--rename
/usr/bin/ischroot && ln -sf /bin/true /usr/bin/ischroot  
RUN apt-get install -y -q python-software-properties  
RUN add-apt-repository ppa:webupd8team/java -y  
RUN apt-get -y update  
RUN apt-get -y upgrade  
RUN apt-get -y dist-upgrade  
  
# Install utility libraries  
RUN apt-get install -y wget unzip supervisor openssh-server vim  
RUN mkdir -p /var/log/supervisor && mkdir /var/run/sshd  
RUN echo '[supervisord]' >> /etc/supervisor/conf.d/nodaemon.conf  
RUN echo 'nodaemon=true' >> /etc/supervisor/conf.d/nodaemon.conf  
RUN echo '[program:sshd]' >> /etc/supervisor/conf.d/sshd.conf  
RUN echo 'command=/usr/sbin/sshd -D' >> /etc/supervisor/conf.d/sshd.conf  
VOLUME /root/.ssh  
EXPOSE 22  
# Install Java 7  
RUN echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select
true | /usr/bin/debconf-set-selections  
RUN apt-get install -y oracle-java7-installer  
RUN update-java-alternatives -s java-7-oracle  
ENV JAVA_HOME /usr/lib/jvm/java-7-oracle  
RUN echo 'export JAVA_HOME="/usr/lib/jvm/java-7-oracle"' >> /etc/bashrc  
  
# Install Glassfish 4 (to /usr/local/glassfish4)  
RUN wget --quiet
http://download.java.net/glassfish/4.0/release/glassfish-4.0.zip  
RUN unzip -q glassfish-4.0.zip -d /usr/local/  
RUN rm glassfish-4.0.zip  
ENV GLASSFISH_HOME /usr/local/glassfish4  
RUN echo 'export GLASSFISH_HOME="/usr/local/glassfish4"' >> /etc/bashrc  
  
RUN echo '[program:glassfish4]' >> /etc/supervisor/conf.d/glassfish4.conf  
RUN echo 'command=asadmin start-domain' >>
/etc/supervisor/conf.d/glassfish4.conf  
RUN echo 'autostart=true' >> /etc/supervisor/conf.d/glassfish4.conf  
RUN echo 'autorestart=unexpected' >> /etc/supervisor/conf.d/glassfish4.conf  
RUN echo 'exitcodes=0,1,2' >> /etc/supervisor/conf.d/glassfish4.conf  
RUN echo 'startsecs=0' >> /etc/supervisor/conf.d/glassfish4.conf  
  
# ADMIN, HTTP, HTTPS  
EXPOSE 4848 8080 8181  
# DEBUGGER  
EXPOSE 9009  
# IIOP, IIOP/SSL, IIOP/SSL WITH MUTUAL AUTHENTICATION  
EXPOSE 3700 3820 3920  
# JMS, JMX, OSGI_SHELL  
EXPOSE 7676 8686 3700 6666  
# Set up PATH variable  
ENV PATH $PATH:$JAVA_HOME/bin:$GLASSFISH_HOME/bin  
RUN export PATH=$PATH  
RUN echo 'export PATH="$PATH:$JAVA_HOME/bin:$GLASSFISH_HOME/bin"' >>
/etc/bashrc  
  
# Clean Up  
RUN apt-get clean  
  
ENTRYPOINT "/usr/bin/supervisord"  
  

