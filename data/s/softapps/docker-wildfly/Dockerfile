#Inspiration 1: https://github.com/jboss-dockerfiles/wildfly  
FROM fedora:23  
MAINTAINER Arun T K <arun.kalikeri@xxxxxxxx.com>  
  
# Execute system update  
RUN dnf -y update && dnf clean all  
  
# Set the Language  
RUN dnf -y reinstall glibc-common  
RUN sed -i -- 's/en_US.UTF-8/en_IN.utf8/g' /etc/locale.conf  
RUN source /etc/locale.conf # apply new setting  
ENV LANG en_IN.utf8  
  
# Install Microsoft fonts & necessary packages in Fedora 21  
RUN curl -L -k
"https://downloads.sourceforge.net/project/mscorefonts2/rpms/msttcore-fonts-
installer-2.6-1.noarch.rpm" > /tmp/msttcore-fonts-installer-2.6-1.noarch.rpm  
RUN dnf install -y /tmp/msttcore-fonts-installer-2.6-1.noarch.rpm xmlstarlet
saxon augeas bsdtar unzip tar lohit-devanagari-fonts  
RUN rm /tmp/msttcore-fonts-installer-2.6-1.noarch.rpm  
  
# Create a user and group used to launch processes  
# The user ID 1000 is the default for the first "regular" user on Fedora/RHEL,  
# so there is a high chance that this ID will be equal to the current user  
# making it easier to use volumes (no permission issues)  
RUN groupadd -r jboss -g 1000 && useradd -u 1000 -r -g jboss -m -d /opt/jboss
-s /sbin/nologin -c "JBoss user" jboss  
# Set the working directory to jboss' user home directory  
WORKDIR /opt/jboss  
# Specify the user which should be used to execute all commands below  
USER jboss  
  
# User root user to install software  
USER root  
# Install necessary packages  
#RUN dnf -y install java-1.8.0-openjdk-devel && dnf clean all  
RUN curl -L -k "http://softappsit.com/repo/jdk-7u80-linux-x64.rpm" >
/tmp/jdk-7-linux-x64.rpm && \  
dnf -y install /tmp/jdk-7-linux-x64.rpm && \  
dnf clean all && rm -rf /tmp/jdk-7-linux-x64.rpm  
  
# Switch back to jboss user  
USER jboss  
# Set the JAVA_HOME variable to make it clear where Java is located  
ENV JAVA_HOME /usr/java/latest  
  
# Set the WILDFLY_VERSION env variable  
ENV WILDFLY_VERSION 8.2.1.Final  
  
# Add the WildFly distribution to /opt, and make wildfly the owner of the
extracted tar content  
# Make sure the distribution is available from a well-known place  
RUN cd $HOME && curl
http://download.jboss.org/wildfly/$WILDFLY_VERSION/wildfly-$WILDFLY_VERSION.tar.gz
| tar zx && mv $HOME/wildfly-$WILDFLY_VERSION $HOME/wildfly  
  
# Set the JBOSS_HOME env variable  
ENV JBOSS_HOME /opt/jboss/wildfly  
  
# Uncomment below line to set the admin user & password  
#RUN /opt/jboss/wildfly/bin/add-user.sh admin Pass#3556 --silent  
# Increasing Initial heap size & Maximum heap size  
RUN sed -i -- 's/JAVA_OPTS="-Xms64m -Xmx512m
-XX:MaxPermSize=256m/JAVA_OPTS="-Xms2048m -Xmx6144m -XX:MaxPermSize=256m/g'
/opt/jboss/wildfly/bin/standalone.conf  
RUN echo "JAVA_OPTS=\"\${JAVA_OPTS} -Dsun.rmi.dgc.client.gcInterval=3600000
-Dsun.rmi.dgc.server.gcInterval=3600000 \"" >>
/opt/jboss/wildfly/bin/standalone.conf  
  
#RUN echo "JAVA_OPTS=\"\${JAVA_OPTS} -Dfile.encoding=UTF8
-Djavax.servlet.request.encoding=UTF-8 -Djavax.servlet.response.encoding=UTF-8
\"" >> /opt/jboss/wildfly/bin/standalone.conf  
#RUN echo "JAVA_OPTS=\"\${JAVA_OPTS} -server -Djava.awt.headless=true
-XX:+UseParNewGC -XX:ParallelGCThreads=2 -XX:SoftRefLRUPolicyMSPerMB=36000
-XX:NewRatio=2 -XX:+AggressiveOpts \"" >>
/opt/jboss/wildfly/bin/standalone.conf  
#RUN echo "JAVA_OPTS=\"\$JAVA_OPTS -Xss2m -XX:+UseConcMarkSweepGC
-XX:+CMSClassUnloadingEnabled\"" >> /opt/jboss/wildfly/bin/standalone.conf  
# Enable binding to all network interfaces and debugging inside the EAP  
RUN echo "JAVA_OPTS=\"\$JAVA_OPTS -Djboss.bind.address=0.0.0.0
-Djboss.bind.address.management=0.0.0.0\"" >>
/opt/jboss/wildfly/bin/standalone.conf  
  
# Add Odoo Pentaho module  
#ADD https://googledrive.com/host/0Bz-
lYS0FYZbIfklDSm90US16S0VjWmpDQUhVOW1GZlVOMUdXb1hENFFBc01BTGpNVE1vZGM/pentaho-
fedora23.war /opt/jboss/wildfly/standalone/deployments/  
#ADD http://cloud1.willowit.com.au/dist/pentaho-reports-for-openerp.war
/opt/jboss/wildfly/standalone/deployments/pentaho-fedora23.war  
ADD https://github.com/softapps/pentaho-reports-war/raw/master/pentaho-
fedora23.war /opt/jboss/wildfly/standalone/deployments/pentaho-fedora23.war  
#ADD https://github.com/softapps/pentaho-reports-war/raw/master/pentaho-
fedora21.war /opt/jboss/wildfly/standalone/deployments/pentaho-fedora21.war  
# User root user to cahnge permission  
USER root  
RUN chown jboss:jboss /opt/jboss/wildfly/standalone/deployments/pentaho-
fedora23.war  
RUN chmod 644 /opt/jboss/wildfly/standalone/deployments/pentaho-fedora23.war  
#RUN chown jboss:jboss /opt/jboss/wildfly/standalone/deployments/pentaho-
fedora21.war  
#RUN chmod 644 /opt/jboss/wildfly/standalone/deployments/pentaho-fedora21.war  
# Switch back to jboss user  
USER jboss  
  
# Expose the ports we're interested in  
EXPOSE 8080 9990  
# Set the default command to run on boot  
# This will boot WildFly in the standalone mode and bind to all interface  
CMD ["/opt/jboss/wildfly/bin/standalone.sh", "-b", "0.0.0.0"]  

