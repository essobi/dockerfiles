FROM java:openjdk-8-jdk  
  
MAINTAINER Francois Achache <francois.achache@gmail.com>  
  
ENV PROFILE glassfish  
ENV ARTIFACT ear  
ENV EXT ear  
  
############### BEGIN COMMON PART ###############  
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64  
ENV PATH $PATH:$JAVA_HOME/bin  
ENV MAVEN_VERSION 3.3.3  
ENV BRANCH docker  
  
# Get maven  
RUN curl -fsSL
http://archive.apache.org/dist/maven/maven-3/$MAVEN_VERSION/binaries/apache-
maven-$MAVEN_VERSION-bin.tar.gz | tar xzf - -C /usr/share \  
&& mv /usr/share/apache-maven-$MAVEN_VERSION /usr/share/maven \  
&& ln -s /usr/share/maven/bin/mvn /usr/bin/mvn  
  
# Build ocelotds  
RUN curl --silent --location --retry 3
https://github.com/ocelotds/ocelotds.org/archive/$BRANCH.tar.gz | tar xz -C
/tmp \  
&& cd /tmp/ocelotds.org-$BRANCH && mvn package -P $PROFILE  
  
# Move application  
RUN mv /tmp/ocelotds.org-$BRANCH/ocelotds.$EXT/target/ocelotds*.$ARTIFACT
/tmp/  
  
# Clean  
RUN rm -rf /tmp/ocelot-master && rm -rf /tmp/ocelotds.org-master && rm -f
/usr/bin/mvn && rm -rf /usr/share/maven && rm -rf ~/.m2  
############### END COMMON PART ###############  
# Set the GLASSFISH env variable  
ENV GLASSFIH_VERSION 4.1.1  
ENV GLASSFISH_HOME /usr/local/glassfish4  
ENV PATH $PATH:$GLASSFISH_HOME/bin  
  
# Install glassfish  
RUN apt-get update && apt-get install -y curl unzip zip inotify-tools && rm
-rf /var/lib/apt/lists/* \  
&& curl -L -o /tmp/glassfish-$GLASSFIH_VERSION.zip
http://download.java.net/glassfish/$GLASSFIH_VERSION/release/glassfish-$GLASSFIH_VERSION.zip
\  
&& unzip /tmp/glassfish-$GLASSFIH_VERSION.zip -d /usr/local \  
&& rm -f /tmp/glassfish-$GLASSFIH_VERSION.zip  
  
# Define demo user  
RUN $GLASSFISH_HOME/bin/asadmin start-domain domain1 \  
&& echo "AS_ADMIN_USERPASSWORD=demo" > pwd.txt \  
&& $GLASSFISH_HOME/bin/asadmin create-file-user --passwordfile=pwd.txt
--groups USERGP demo \  
&& $GLASSFISH_HOME/bin/asadmin stop-domain domain1 \  
&& rm pwd.txt  
  
# Deploy ocelotds  
RUN mv /tmp/ocelot*.ear $GLASSFISH_HOME/glassfish/domains/domain1/autodeploy  
  
# Expose the ports we're interested in  
EXPOSE 8080 4848 8181  
WORKDIR $GLASSFISH_HOME  
  
# Expose workspace  
VOLUME $GLASSFISH_HOME/glassfish/domains/domain1/autodeploy  
  
# verbose mode for foreground mode  
CMD asadmin start-domain --verbose domain1  
  

