FROM ubuntu  
  
ENV maven_url
http://mirror.hosting90.cz/apache/maven/maven-3/3.2.5/binaries/apache-
maven-3.2.5-bin.tar.gz  
  
MAINTAINER Tadeas 'donarus' Palusga  
  
RUN echo '#### ORACLE JAVA' >> /etc/apt/sources.list ;\  
echo 'deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main' >>
/etc/apt/sources.list ;\  
echo 'deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main' >>
/etc/apt/sources.list ;\  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EEA14886 ;\  
apt-get update ;\  
echo "oracle-java7-installer shared/accepted-oracle-license-v1-1 boolean true"
| debconf-set-selections ;\  
DEBIAN_FRONTEND=noninteractive apt-get install oracle-java7-installer -y  
  
RUN apt-get install curl ssh rsync -y  
  
RUN mkdir -p /tmp/maven ;\  
cd /tmp/maven/ ;\  
curl http://mirror.hosting90.cz/apache/maven/maven-3/3.2.5/binaries/apache-
maven-3.2.5-bin.tar.gz | tar xzv ;\  
mavendir=`ls` ;\  
mv $mavendir /opt ;\  
cd /opt ;\  
ln $mavendir maven -s ;\  
update-alternatives --install /usr/bin/mvn mvn /opt/maven/bin/mvn 1  
  
RUN ssh-keygen -f /root/.ssh/id_rsa -N ""  
RUN echo "StrictHostKeyChecking no" >> ~/.ssh/config  
  
COPY mvnrunner.sh /root/mvnrunner.sh  
RUN chmod +x /root/mvnrunner.sh  
RUN mkdir ~/develop  
  
ENTRYPOINT ["/root/mvnrunner.sh"]  

