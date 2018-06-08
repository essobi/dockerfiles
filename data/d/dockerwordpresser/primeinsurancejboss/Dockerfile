FROM ubuntu:14.04  
RUN sudo apt-get update  
RUN sudo apt-get install python-software-properties -y  
RUN sudo apt-get install software-properties-common -y  
RUN /usr/bin/yes | sudo add-apt-repository ppa:webupd8team/java  
RUN sudo apt-get update  
RUN /usr/bin/yes | sudo apt-get install oracle-java7-installer -y  
RUN java -version  
RUN dpkg --get-selections | grep java  
# enabling sudo group  
# enabling sudo over ssh  
RUN echo '%wheel ALL=(ALL) NOPASSWD: ALL' >> /etc/sudoers && \  
sed -i 's/.*requiretty$/Defaults !requiretty/' /etc/sudoers  
  
# add a user for the application, with sudo permissions  
#RUN useradd -m jboss ; echo jboss: | chpasswd ; usermod -a -G wheel jboss  
#RUN useradd -m jboss && /usr/bin/passwd jboss < "jboss"$'\n'"jboss"  
RUN useradd -m jboss  
#RUN echo jboss | passwd jboss --stdin  
RUN echo jboss:jboss | chpasswd  
RUN usermod -aG sudo jboss  
RUN wget http://download.jboss.org/jbossas/7.1/jboss-as-7.1.1.Final/jboss-
as-7.1.1.Final.zip && sudo apt-get install unzip && sudo unzip jboss-
as-7.1.1.Final.zip  
RUN mv jboss-as-7.1.1.Final /opt/jboss && cd /opt/jboss/bin  
# set environment  
ENV JBOSS_HOME /opt/jboss  
  
# create JBoss console user  
#RUN $JBOSS_HOME/bin/add-user.sh admin admin@2016 --silent  
RUN $JBOSS_HOME/bin/add-user.sh --silent=true admin admin@2016  
# configure JBoss  
RUN echo "JAVA_OPTS=\"\$JAVA_OPTS -Djboss.bind.address=0.0.0.0
-Djboss.bind.address.management=0.0.0.0\"" >> $JBOSS_HOME/bin/standalone.conf  
  
# set permission folder  
RUN chown -R jboss:jboss /opt/jboss  
  
# JBoss ports  
EXPOSE 8080 9990 9999  
# start JBoss  
ENTRYPOINT $JBOSS_HOME/bin/standalone.sh -c standalone-full-ha.xml  
  
# deploy app  
#ADD sample.war "$JBOSS_HOME/standalone/deployments/"  
USER jboss  
CMD /bin/bash  

