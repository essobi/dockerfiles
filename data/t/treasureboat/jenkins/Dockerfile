#  
# TreasureBoat.org  
# by ishimoto  
#  
# Jenkins 1.596 on CentOS 6.6  
#  
# service jenkins start/stop/restart  
#  
# build : docker build -t treasureboat/jenkins:0.7 .  
# run : docker run -d -P -p 8080:8080 --name tbJenkins -it
treasureboat/jenkins:0.7  
  
FROM treasureboat/java:latest  
MAINTAINER treasureboat <office@treasureboat.org>  
  
##### download jenkins get latest and greatest  
#RUN wget -O /etc/yum.repos.d/jenkins.repo http://pkg.jenkins-
ci.org/redhat/jenkins.repo  
#RUN rpm --import http://pkg.jenkins-ci.org/redhat/jenkins-ci.org.key  
#RUN yum install -y jenkins  
  
##### download version 1.597-1.1  
##### see 'http://pkg.jenkins-ci.org/redhat/'  
RUN wget -q -O /tmp/jenkins.rpm 'http://pkg.jenkins-
ci.org/redhat/jenkins-1.597-1.1.noarch.rpm'  
RUN rpm -ivh /tmp/jenkins.rpm  
  
##### install git  
RUN yum install -y git  
RUN yum clean all  
  
# add boot script  
RUN printf 'service jenkins start\n' >> /opt/boot.sh  
RUN printf 'sleep 5\n' >> /opt/boot.sh  
RUN chmod u+rwx /opt/boot.sh  
  
#### Jenkins Home is : /var/lib/jenkins  
#### about the Jenkins folder structure  
## config.xml -> (jenkins root configuration)  
## userContent -> (files in this directory will be served under yout
http://serve/userContent/)  
## plugins -> (stores plugins)  
## jobs -> (here are the jobs)  
  
#### Back up and restore  
## All the settings, build logs, artifact archives are stored under the
JENKINS_HOME directory.  
## Simply archive this directory to make a back up. Similarly, restoring the
data is just replacing  
## the contents of the JENKINS_HOME directory from a back up.  
## Back ups can be taken without stopping the server, but when you restore,
please do stop the server.  
  
#### Create the Job : TreasureBoat  
RUN mkdir -p /var/lib/jenkins/jobs/TreasureBoat  
RUN mkdir -p /var/lib/jenkins/.ssh  
RUN wget -q -O /var/lib/jenkins/jobs/TreasureBoat/config.xml
'https://dl.dropboxusercontent.com/u/1548210/TB/Docker/Jenkins/config.xml'  
RUN chown -R jenkins:jenkins /var/lib/jenkins/jobs  
  
EXPOSE 22 8080  
  
VOLUME ["/var/lib/jenkins", "/var/log/jenkins"]  
  
#####first time running the docker, you have to create a ssh key  
## so do following commands.  
##  
## $ cd /var/lib/jenkins  
## $ ssh-keygen -t rsa -C "your.address@domain.com"  
## it will ask you : Enter file in which to save the key (/root/.ssh/id_rsa):  
## Enter : /var/lib/jenkins/.ssh/id_rsa  
##  
## add the key to the ssh-agent  
## $ eval "$(ssh-agent -s)"  
## $ ssh-add /var/lib/jenkins/.ssh/id_rsa  
##  
## get the public key  
## $ cat id_rsa.pub  
## $ chown -R jenkins:jenkins /var/lib/jenkins/.ssh  
##  
## you have to send this key to <office@treasureboat.org> so we can set your
key on our Github deploy page  
## after that step is done  
## $ ssh -T git@github.com  
##  
## The authenticity of host 'github.com (XXX.XXX.XXX.XXX)' can't be
established.  
## RSA key fingerprint is XX:XX:XX:XX:XX:XX:XX:XX:XX:XX:XX:XX:XX:XX:XX:XX.  
## Are you sure you want to continue connecting (yes/no)? yes  
## Warning: Permanently added 'github.com,XXX.XXX.XXX.XXX' (RSA) to the list
of known hosts.  
## Hi ishimoto/TreasureBoat! You've successfully authenticated, but GitHub
does not provide shell access.  
##  
## Last :  
## docker ps -l  
## docker commit -m "Added ssh key" -a "Your Name" tbJenkins yourname/jenkins  

