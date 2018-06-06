FROM centos:latest  
  
MAINTAINER ciela <zektbach@gmail.com>  
  
# yum  
RUN yum -y update && \  
yum -y install initscripts wget tar ntp git docker zip unzip mercurial bzr &&
\  
yum -y clean all  
  
# Time Zone  
RUN echo 'ZONE="Asia/Tokyo"' > /etc/sysconfig/clock && \  
rm -f /etc/localtime && \  
ln -fs /usr/share/zoneinfo/Asia/Tokyo /etc/localtime && \  
ntpdate ntp.nict.jp  
  
# java  
RUN wget --no-check-certificate --no-cookies --header "Cookie:
oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-
pub/java/jdk/8u20-b26/jdk-8u20-linux-x64.rpm && \  
rpm -ihv jdk-8u20-linux-x64.rpm  
  
# Go  
RUN wget https://storage.googleapis.com/golang/go1.3.3.linux-amd64.tar.gz && \  
tar -C /usr/local -xzf go1.3.3.linux-amd64.tar.gz  
ENV GOROOT /usr/local/go  
RUN mkdir /gopath  
ENV GOPATH /gopath  
ENV PATH $PATH:/usr/local/go/bin  
RUN go get github.com/mattn/gom  
  
# jenkins  
RUN wget -O /etc/yum.repos.d/jenkins.repo http://pkg.jenkins-
ci.org/redhat/jenkins.repo && \  
rpm --import http://pkg.jenkins-ci.org/redhat/jenkins-ci.org.key && \  
yum -y install jenkins  
RUN unzip /usr/lib/jenkins/jenkins.war WEB-INF/jenkins-cli.jar  
RUN service jenkins start && sleep 60 && \  
curl -L http://updates.jenkins-ci.org/update-center.json | sed '1d;$d' | curl
-X POST -H 'Accept: application/json' -d @-
http://localhost:8080/updateCenter/byId/default/postBack && \  
java -jar WEB-INF/jenkins-cli.jar -s http://localhost:8080 install-plugin \  
github docker-plugin golang awseb-deployment-plugin thinBackup -restart  
RUN ls -lF /var/lib/jenkins/plugins  
  
EXPOSE 8080  
CMD ["java", "-DJENKINS_HOME=/var/lib/jenkins", "-jar",
"/usr/lib/jenkins/jenkins.war", "--logfile=/var/log/jenkins/jenkins.log"]  

