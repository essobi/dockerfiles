FROM devildominator/tacobelljenkins_slave  
  
MAINTAINER TacobellJenkinSlave version 1.0  
  
USER root  
  
ARG JENKINS_REMOTING_VERSION=3.12  
  
ENV ANDROID_HOME /usr/lib/android-sdk-linux/  
ENV GRADLE_HOME /usr/local/gradle  
ENV PATH ${GRADLE_HOME}/bin:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-
tools:${PATH}  
RUN chmod a+rwx /home/jenkins  
WORKDIR /home/jenkins  
USER jenkins  
  
ENTRYPOINT ["/opt/bin/entry_point.sh", "/usr/local/bin/jenkins-slave"]  

