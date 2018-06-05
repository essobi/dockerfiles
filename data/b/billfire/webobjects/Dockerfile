FROM openjdk:8-jdk  
  
ARG AWS_ACCESS_KEY_ID  
ARG AWS_SECRET_ACCESS_KEY  
  
ARG ANT_VERSION=1.9.10  
ARG USER_HOME_DIR="/root"  
ARG ANT_URL=http://mirror.ibcp.fr/pub/apache/ant/binaries/apache-
ant-${ANT_VERSION}-bin.tar.gz  
  
ARG
WONDER_FRAMEWORKS_URL=https://jenkins.wocommunity.org/job/Wonder6/lastSuccessfulBuild/artifact/Root/Roots/Wonder-
Frameworks.tar.gz  
ARG
WOPROJECT_ZIP=https://jenkins.wocommunity.org/job/WOLips47/lastBuild/artifact/temp/dist/plugins/org.objectstyle.wolips.woproject.ant_4.7.20170831.4.jar  
  
RUN mkdir -p /usr/share/ant /usr/share/ant/ref \  
&& curl -fsSL -o /tmp/apache-ant.tar.gz ${ANT_URL} \  
&& tar -xzf /tmp/apache-ant.tar.gz -C /usr/share/ant --strip-components=1 \  
&& rm -f /tmp/apache-ant.tar.gz \  
&& ln -s /usr/share/ant/bin/ant /usr/bin/ant  
  
RUN curl -C - -O https://wocommunity.org/documents/tools/WOInstaller.jar  
  
RUN java -jar WOInstaller.jar 5.4.3 /opt  
  
RUN curl -o /tmp/wonder-frameworks.tar.gz ${WONDER_FRAMEWORKS_URL} \  
&& tar -xzf /tmp/wonder-frameworks.tar.gz -C /opt/Library/Frameworks \  
&& rm -f /tmp/wonder-frameworks.tar.gz  
  
RUN curl -o /tmp/woproject.zip ${WOPROJECT_ZIP} \  
&& unzip /tmp/woproject.zip -d /tmp/woproject \  
&& cp /tmp/woproject/lib/woproject.jar /usr/share/ant/lib/ \  
&& rm -rf /tmp/woproject  
  
# ant -Dwo.system.frameworks=/opt/Library/Frameworks
-Dwo.local.frameworks=/opt/Local/Library/Frameworks build  

