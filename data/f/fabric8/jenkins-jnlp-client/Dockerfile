FROM fabric8/java-centos-openjdk8-jre  
  
#We need to add the epele-release before we try to install the nss_wrapper  
RUN yum install -y epel-release git gettext  
RUN yum install -y nss_wrapper  
  
ENV HOME /home/jenkins  
ENV JENKINS_HOME /home/jenkins  
  
RUN useradd -c "Jenkins user" -d $HOME -m jenkins  
  
RUN curl --create-dirs -sSLo /usr/share/jenkins/slave.jar http://repo.jenkins-
ci.org/public/org/jenkins-ci/main/remoting/2.52/remoting-2.52.jar \  
&& chmod 755 /usr/share/jenkins \  
&& chmod 644 /usr/share/jenkins/slave.jar  
  
COPY start.sh /usr/local/bin/start.sh  
COPY passwd.template /usr/local/share/passwd.template  
WORKDIR /home/jenkins  
  
ENTRYPOINT ["/usr/local/bin/start.sh"]  

