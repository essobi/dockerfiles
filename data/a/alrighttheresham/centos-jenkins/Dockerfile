from alrighttheresham/centos-base  
  
RUN yum -y groupinstall 'X Window System'; yum -y install liberation-mono-
fonts pyvnc2swf tigervnc-server twm xterm  
  
RUN wget -O /etc/yum.repos.d/jenkins.repo http://pkg.jenkins-
ci.org/redhat/jenkins.repo; rpm --import http://pkg.jenkins-
ci.org/redhat/jenkins-ci.org.key; yum -y install jenkins; echo
"jenkins:jenkins" | chpasswd  
  
ENV JENKINS_HOME /var/lib/jenkins  
  
RUN usermod -s /bin/bash jenkins; su -c 'mkdir -p $HOME/.vnc' jenkins; su -c
'echo jenkins | vncpasswd -f > $HOME/.vnc/passwd' jenkins; su -c 'chmod 600
$HOME/.vnc/passwd' jenkins  
ADD ./xstartup $JENKINS_HOME/.vnc/  
RUN chmod -v +x $JENKINS_HOME/.vnc/xstartup  
  
ADD http://updates.jenkins-ci.org/latest/xvnc.hpi
$JENKINS_HOME/plugins/xvnc.hpi  
ADD http://updates.jenkins-ci.org/latest/sonar.hpi
$JENKINS_HOME/plugins/sonar.hpi  
ADD http://updates.jenkins-ci.org/latest/subversion.hpi
$JENKINS_HOME/plugins/subversion.hpi  
ADD http://updates.jenkins-ci.org/latest/vncrecorder.hpi
$JENKINS_HOME/plugins/vncrecorder.hpi  
  
RUN chown -R jenkins:jenkins $JENKINS_HOME  
  
ENV NETBEANS_VER 8.0.1  
ADD ./state.xml /tmp/state.xml  
RUN wget
http://download.netbeans.org/netbeans/$NETBEANS_VER/final/bundles/netbeans-$NETBEANS_VER-
javase-linux.sh -O /tmp/netbeans.sh -q; chmod +x /tmp/netbeans.sh;
/tmp/netbeans.sh --silent --state /tmp/state.xml; rm -rf /tmp/*; ln -s
/usr/local/netbeans-$NETBEANS_VER /usr/local/netbeans  
  
ENV nbplatform.default.netbeans.dest.dir /usr/local/netbeans  
ENV nbplatform.default.harness.dir /usr/local/netbeans/harness  
  
EXPOSE 8080  
ENTRYPOINT service jenkins start; sleep 5; tail -f
/var/log/jenkins/jenkins.log  

