FROM centos:centos6  
  
MAINTAINER Stephen Butcher stephen.butcher@redhound.net  
  
ADD ./files /vtemp  
RUN yum -y install dos2unix gzip tar wget openssh-server openssh-clients &&
yum -y update  
RUN cd /vtemp && \  
wget --no-check-certificate --no-cookies --header "Cookie:
oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-
pub/java/jdk/8u65-b17/jdk-8u65-linux-x64.rpm -q && \  
rpm -i /vtemp/jdk-8u65-linux-x64.rpm  
  
RUN mkdir -p /usr/share && cd /vtemp && \  
wget http://archive.apache.org/dist/tomcat/tomcat-8/v8.0.29/bin/apache-
tomcat-8.0.29.tar.gz -q && \  
cd /usr/share && tar xf /vtemp/apache-tomcat-8.0.29.tar.gz  
RUN cp /vtemp/setenv.sh /usr/share/apache-tomcat-8.0.29/bin/setenv.sh  
RUN cp /vtemp/tomcat-users.xml /usr/share/apache-tomcat-8.0.29/conf/tomcat-
users.xml  
RUN echo "export CATALINA_HOME=\"/usr/share/apache-tomcat-8.0.29\"" >>
/etc/profile  
RUN echo "export JAVA_HOME=\"/usr/java/jdk1.8.0_65\"" >> /etc/profile  
RUN echo "export JRE_HOME=\"/usr/java/jdk1.8.0_65\"" >> /etc/profile  
RUN echo "export JENKINS_HOME =\"/jenkins\"" >> /etc/profile  
RUN cp /vtemp/tomcat8 /etc/init.d/tomcat8  
RUN cd /etc/init.d && dos2unix /etc/init.d/tomcat8 && chkconfig --add tomcat8  
  
RUN cp /vtemp/sshd_config /etc/ssh/sshd_config  
RUN /usr/sbin/useradd jenkins -u 500 -U -G wheel  
RUN mkdir /jenkins && chown jenkins:jenkins /jenkins && chmod 775 /jenkins  
RUN cp /vtemp/jenkins.war /usr/share/apache-tomcat-8.0.29/webapps/jenkins.war  
RUN echo 'jenkins:Q$1Mnj&f' | chpasswd  
RUN rm -r /vtemp  
  
EXPOSE 8009 8080 22  
CMD /etc/init.d/sshd start && /etc/init.d/tomcat8 start && tail -F
/usr/share/apache-tomcat-8.0.29/logs/catalina.out  

