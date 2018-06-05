FROM openshift/base-centos7  
  
MAINTAINER Thomas Philipona <philipona@puzzle.ch>  
  
EXPOSE 8080  
  
  
LABEL io.k8s.description="Example Spring Boot App" \  
io.k8s.display-name="APPUiO Spring Boot App" \  
io.openshift.expose-services="8080:http" \  
io.openshift.tags="builder,springboot" \  
io.openshift.s2i.destination="/opt/s2i/destination"  
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
  
RUN sh /opt/app-root/src/gradlew build  
  
RUN cp -a /opt/app-root/src/build/libs/springboots2idemo*.jar /opt/app-
root/springboots2idemo.jar  
  
CMD java -Xmx64m -Xss1024k -jar /opt/app-root/springboots2idemo.jar  

