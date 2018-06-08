FROM pascalgrimaud/ubuntu  
MAINTAINER Pascal Grimaud <pascalgrimaud@gmail.com>  
  
# update  
RUN apt-get -y update  
  
# install python-software-properties (so you can do add-apt-repository)  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y -q python-software-
properties software-properties-common  
  
# install utilities  
RUN apt-get -y install wget  
  
# install oracle java from PPA  
RUN add-apt-repository ppa:webupd8team/java -y  
RUN apt-get -y -qq update  
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true | /usr/bin/debconf-set-selections  
RUN apt-get -y install oracle-java8-installer  
RUN update-java-alternatives -s java-8-oracle  
RUN echo "export JAVA_HOME=/usr/lib/jvm/java-8-oracle" >> ~/.bashrc  
  
# install jenkins  
ENV JENKINS_VERSION latest  
RUN wget -O /tmp/jenkins.war http://mirrors.jenkins-
ci.org/war/${JENKINS_VERSION}/jenkins.war  
RUN mkdir -p /opt/jenkins/  
RUN mv /tmp/jenkins.war /opt/jenkins/jenkins.war  
ENV JENKINS_HOME /opt/jenkins/jenkins_home  
  
#----- optional -----  
# install git  
RUN add-apt-repository ppa:git-core/ppa -y  
RUN apt-get -y update  
RUN apt-get -y install git  
  
# install svn  
RUN apt-get -y install subversion  
  
# install ant  
RUN wget -O /tmp/apache-ant-1.9.5-bin.tar.gz
https://archive.apache.org/dist/ant/binaries/apache-ant-1.9.5-bin.tar.gz  
RUN echo "44122814846a6f4f59fcc9ea2b36b42e /tmp/apache-ant-1.9.5-bin.tar.gz" |
md5sum -c  
RUN tar xzf /tmp/apache-ant-1.9.5-bin.tar.gz -C /opt/  
  
# install maven  
RUN wget -O /tmp/apache-maven-3.3.3-bin.tar.gz
http://archive.apache.org/dist/maven/maven-3/3.3.3/binaries/apache-
maven-3.3.3-bin.tar.gz  
RUN echo "794b3b7961200c542a7292682d21ba36 /tmp/apache-maven-3.3.3-bin.tar.gz"
| md5sum -c  
RUN tar xzf /tmp/apache-maven-3.3.3-bin.tar.gz -C /opt/  
  
# install java 7  
# RUN echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select
true | /usr/bin/debconf-set-selections  
# RUN apt-get -y install oracle-java7-installer  
# install java 6  
# RUN echo oracle-java6-installer shared/accepted-oracle-license-v1-1 select
true | /usr/bin/debconf-set-selections  
# RUN apt-get -y install oracle-java6-installer  
# install Sun JDK 1.5.0_22  
# RUN cd /tmp ;\  
# wget --no-check-certificate --no-cookies --header "Cookie:
oraclelicense=accept-securebackup-cookie" \  
# -O jdk-1_5_0_22-linux-amd64.bin http://download.oracle.com/otn-
pub/java/jdk/1.5.0_22/jdk-1_5_0_22-linux-amd64.bin  
# RUN cd /tmp ;\  
# echo yes|sh /tmp/jdk-1_5_0_22-linux-amd64.bin  
# RUN mv /tmp/jdk1.5.0_22 /usr/lib/jvm/  
# install Sun JDK 1.4.2_19  
# RUN cd /tmp ;\  
# wget --no-check-certificate --no-cookies --header "Cookie:
oraclelicense=accept-securebackup-cookie" \  
# -O j2sdk-1_4_2_19-linux-i586.bin http://download.oracle.com/otn-
pub/java/j2sdk/1.4.2_19/j2sdk-1_4_2_19-linux-i586.bin  
# RUN cd /tmp ;\  
# echo yes|sh /tmp/j2sdk-1_4_2_19-linux-i586.bin  
# RUN mv /tmp/j2sdk1.4.2_19 /usr/lib/jvm/  
# install maven 2.2  
# RUN wget -O /tmp/apache-maven-2.2.1-bin.tar.gz
http://archive.apache.org/dist/maven/maven-2/2.2.1/binaries/apache-
maven-2.2.1-bin.tar.gz  
# RUN echo "3f829ed854cbacdaca8f809e4954c916 /tmp/apache-
maven-2.2.1-bin.tar.gz" | md5sum -c  
# RUN tar xzf /tmp/apache-maven-2.2.1-bin.tar.gz -C /opt/  
#--------------------  
# link  
RUN ln -s /usr/lib/jvm/java-8-oracle /opt/java8  
RUN ln -s /opt/apache-ant-1.9.5 /opt/ant  
RUN ln -s /opt/apache-maven-3.3.3 /opt/maven  
# RUN ln -s /usr/lib/jvm/j2sdk1.4.2_19 /opt/java4  
# RUN ln -s /usr/lib/jvm/jdk1.5.0_22 /opt/java5  
# RUN ln -s /usr/lib/jvm/java-6-oracle /opt/java6  
# RUN ln -s /usr/lib/jvm/java-7-oracle /opt/java7  
# RUN ln -s /opt/apache-maven-2.2.1 /opt/maven2  
# env  
ENV ANT_HOME /opt/ant  
ENV MAVEN_HOME /opt/maven  
  
# configuration  
ADD settings.xml /root/.m2/settings.xml  
  
# clean  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# expose ports  
EXPOSE 8080 50000  
# add volumes to allow backup of config  
VOLUME ["/opt/jenkins/jenkins_home"]  
  
# script to start the container  
ADD jenkins_run.sh /jenkins_run.sh  
RUN chmod 755 /*.sh  
CMD ["/jenkins_run.sh"]  

