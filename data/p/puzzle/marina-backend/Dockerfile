FROM centos/s2i-base-centos7 as builder  
  
# Install Java  
RUN INSTALL_PKGS="tar unzip bc which lsof java-1.8.0-openjdk
java-1.8.0-openjdk-devel" && \  
yum install -y $INSTALL_PKGS && \  
rpm -V $INSTALL_PKGS && \  
yum clean all -y && \  
mkdir -p /opt/s2i/destination  
  
USER 1001  
  
ADD ./gradlew /opt/app-root/src/  
ADD gradle /opt/app-root/src/gradle  
ADD build.gradle /opt/app-root/src/  
ADD src /opt/app-root/src/src  
  
# build the application from source  
RUN sh /opt/app-root/src/gradlew build  
  
FROM centos/s2i-base-centos7  
# Install Java  
RUN INSTALL_PKGS="tar unzip bc which lsof java-1.8.0-openjdk
java-1.8.0-openjdk-devel" && \  
yum install -y $INSTALL_PKGS && \  
rpm -V $INSTALL_PKGS && \  
yum clean all -y && \  
mkdir -p /opt/s2i/destination  
  
  
EXPOSE 8080  
USER 1001  
# copy the artifact to the correct location  
COPY \--from=builder /opt/app-root/src/build/libs /opt/app-root/  
  
RUN mv /opt/app-root/src*.jar /opt/app-root/marina-backend.jar  
RUN ls -la /opt/app-root/  
  
CMD java -jar /opt/app-root/marina-backend.jar  
  

