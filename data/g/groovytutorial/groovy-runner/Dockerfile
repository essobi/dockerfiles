FROM java:openjdk-8-jdk  
  
MAINTAINER duncan@dickinson.name  
  
RUN apt-get update && \  
apt-get -y install sudo wget unzip && \  
apt-get clean  
  
ENV GROOVY_VERSION=2.4.5  
ENV JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64 \  
GROOVY_HOME=/opt/groovy-${GROOVY_VERSION}  
  
# Install groovy  
ADD http://dl.bintray.com/groovy/maven/apache-groovy-
binary-${GROOVY_VERSION}.zip /tmp/  
  
#ADD dist-tmp/apache-groovy-binary-${GROOVY_VERSION}.zip /tmp/  
RUN unzip -d /opt/ /tmp/apache-groovy-binary-${GROOVY_VERSION}.zip \  
&& rm /tmp/apache-groovy-binary-${GROOVY_VERSION}.zip  
  
#Setup the local user  
RUN echo "%sudo ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers  
  
RUN useradd -u 5001 -c "Local user" -p user -m user --shell /bin/bash -G
users,sudo && \  
echo "secret\nsecret" | passwd user && \  
usermod -u 1000 user  
  
USER user  
EXPOSE 4200  
ENV CODENVY_WEB_SHELL_PORT 4200  
ADD entrypoint.sh /entrypoint.sh  
  
#Install shellinabox  
ADD shellinabox.zip /opt/shellinabox.zip  
  
RUN sudo chown user:user -R /opt && \  
cd /opt && unzip shellinabox.zip && \  
rm -rf /opt/shellinabox.zip && \  
sudo chmod 755 /entrypoint.sh  
  
RUN echo "export JAVA_HOME=$JAVA_HOME" >> /home/user/.bashrc  
RUN echo "export GROOVY_HOME=$GROOVY_HOME" >> /home/user/.bashrc  
RUN echo "export PATH=$GROOVY_HOME/bin:$JAVA_HOME/bin:$PATH" >>
/home/user/.bashrc  
  
ENTRYPOINT ["/entrypoint.sh"]  

