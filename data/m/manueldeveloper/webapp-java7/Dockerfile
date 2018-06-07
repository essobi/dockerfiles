# Dockerfile which defines the technological stack for webapp based on Java 7.  
# The stack is built with the following tools:  
# - Java 1.7 (OpenJDK)  
# - Maven 3.1.1  
# - Tomcat 7.0.78  
#  
# Contributors:  
# manueldeveloper@gmail.com  
  
FROM ubuntu:16.04  
  
ENV JAVA_HOME=/usr/lib/jvm/java-7-openjdk-amd64  
  
ENV MAVEN_VERSION=3.1.1  
ENV M2_HOME=/home/user/apache-maven-$MAVEN_VERSION  
  
ENV TOMCAT_HOME=/home/user/tomcat7  
  
ENV PATH=$JAVA_HOME/bin:$M2_HOME/bin:$PATH  
  
RUN apt-get update && \  
apt-get -y install \  
openssh-server \  
sudo \  
procps \  
wget \  
unzip \  
mc \  
ca-certificates \  
curl \  
locales \  
software-properties-common \  
python-software-properties \  
bash-completion && \  
mkdir /var/run/sshd && \  
sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd && \  
echo "%sudo ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers && \  
useradd -u 1000 -G users,sudo -d /home/user --shell /bin/bash -m user && \  
usermod -p "*" user && \  
add-apt-repository -y ppa:git-core/ppa && \  
add-apt-repository -y ppa:openjdk-r/ppa && \  
apt-get update && \  
sudo apt-get install git subversion -y && \  
apt-get clean && \  
apt-get -y autoremove && \  
apt-get install -y openjdk-7-jdk && \  
apt-get -y clean && \  
rm -rf /var/lib/apt/lists/* && \  
echo "#! /bin/bash\n set -e\n sudo /usr/sbin/sshd -D &\n exec \"\$@\"" >
/home/user/entrypoint.sh && chmod a+x /home/user/entrypoint.sh  
  
ENV LANG en_GB.UTF-8  
ENV LANG en_US.UTF-8  
  
USER user  
RUN sudo locale-gen en_US.UTF-8 && \  
svn --version && \  
cd /home/user && ls -la && \  
sed -i 's/# store-passwords = no/store-passwords = yes/g'
/home/user/.subversion/servers && \  
sed -i 's/# store-plaintext-passwords = no/store-plaintext-passwords = yes/g'
/home/user/.subversion/servers  
  
EXPOSE 22 4403 8000 8080 9876  
  
LABEL che:server:8080:ref=tomcat7 che:server:8080:protocol=http
che:server:8000:ref=tomcat7-debug che:server:8000:protocol=http
che:server:9876:ref=codeserver che:server:9876:protocol=http  
  
RUN mkdir /home/user/tomcat7 && \  
mkdir /home/user/apache-maven-$MAVEN_VERSION && \  
wget -qO- "http://apache.ip-
connect.vn.ua/maven/maven-3/$MAVEN_VERSION/binaries/apache-
maven-$MAVEN_VERSION-bin.tar.gz" | tar -zx --strip-components=1 -C
/home/user/apache-maven-$MAVEN_VERSION/ && \  
wget -qO-
"http://apache.mirrors.ovh.net/ftp.apache.org/dist/tomcat/tomcat-7/v7.0.78/bin/apache-
tomcat-7.0.78.tar.gz" | tar -zx --strip-components=1 -C /home/user/tomcat7 &&
\  
rm -rf /home/user/tomcat8/webapps/* && \  
echo "export MAVEN_OPTS=\$JAVA_OPTS" >> /home/user/.bashrc  
  
WORKDIR /projects  
  
ENTRYPOINT ["/home/user/entrypoint.sh"]  
  
CMD tail -f /dev/null  

