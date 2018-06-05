FROM ubuntu  
  
MAINTAINER Baev Dmitry  
  
RUN apt-get update  
  
# Install a basic SSH server  
RUN apt-get install -y openssh-server  
RUN sed -i 's|session required pam_loginuid.so|session optional
pam_loginuid.so|g' /etc/pam.d/sshd  
RUN mkdir -p /var/run/sshd  
  
RUN adduser --quiet jenkins  
RUN echo "jenkins:jenkins" | chpasswd  
RUN chown -R jenkins:jenkins /home/jenkins/.*  
  
# Standard SSH port  
EXPOSE 22  
CMD ["/usr/sbin/sshd", "-D"]  
  
RUN apt-get install -y -q --force-yes git maven  
  
# Add .gitconfig  
ADD build/.gitconfig /home/jenkins/.gitconfig  
  
RUN apt-get purge -y --force-yes -f openjdk-7-jre openjdk-6-jre-headless  
  
# Install JDK7  
RUN \  
apt-get install software-properties-common python-software-properties -y && \  
echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select true |
debconf-set-selections && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update && \  
apt-get install -y oracle-java7-installer && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/cache/oracle-jdk7-installer  
ENV JAVA_HOME /usr/lib/jvm/java-7-oracle  
  
# Install PhantomJS  
ENV PHANTOMJS_VERSION 1.9.8  
RUN \  
apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y vim git wget libfreetype6 libfontconfig bzip2 && \  
mkdir -p /srv/var && \  
wget -q --no-check-certificate -O /tmp/phantomjs-$PHANTOMJS_VERSION-
linux-x86_64.tar.bz2
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-$PHANTOMJS_VERSION-
linux-x86_64.tar.bz2 && \  
tar -xjf /tmp/phantomjs-$PHANTOMJS_VERSION-linux-x86_64.tar.bz2 -C /tmp && \  
rm -f /tmp/phantomjs-$PHANTOMJS_VERSION-linux-x86_64.tar.bz2 && \  
mv /tmp/phantomjs-$PHANTOMJS_VERSION-linux-x86_64/ /srv/var/phantomjs && \  
ln -s /srv/var/phantomjs/bin/phantomjs /usr/bin/phantomjs && \  
apt-get autoremove -y && \  
apt-get clean all  
  
# Prepare dependencies cache  
ADD build/resolve-deps.sh /home/jenkins/resolve-deps.sh  
RUN \  
su -l jenkins -c "bash /home/jenkins/resolve-deps.sh" && \  
rm -rf /home/jenkins/resolve-deps.sh  
  
# Add MAVEN_OPTS and JAVA_OPTS to .bash_rc  
RUN \  
echo 'MAVEN_OPTS="-Xmx2048m -XX:MaxPermSize=512m"' >>
/home/jenkins/.bash_profile && \  
echo 'JAVA_OPTS="-Xmx2048m -XX:MaxPermSize=512m"' >>
/home/jenkins/.bash_profile  

