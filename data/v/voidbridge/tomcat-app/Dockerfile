FROM voidbridge/base-centos7  
MAINTAINER Voidbridge <developers@voidbridge.com>  
ENV JDK_VERSION=1.8.0_11  
  
LABEL io.k8s.description="Builder image for Apache Tomcat" \  
io.k8s.display-name="Tomcat App"  
  
# Install some extra tools  
RUN yum install -y bind-utils telnet hostname && \  
yum clean all -y  
  
# Install Java  
COPY ./files/jdk-8u11-linux-x64.rpm /tmp  
RUN rpm -ivh /tmp/jdk-8u11-linux-x64.rpm  
  
# Install Tomcat  
COPY ./files/apache-tomcat-8.0.35.tar.gz /tmp  
RUN tar zxvf /tmp/apache-tomcat-8.0.35.tar.gz -C /usr/local  
RUN ln -s /usr/local/apache-tomcat-8.0.35 /usr/local/tomcat  
  
RUN rm -rf /usr/local/tomcat/webapps/*  
  
# Mount volume  
VOLUME /mnt/data  
  
# Copy S2I scripts  
LABEL io.openshift.s2i.scripts-url=image:///usr/libexec/s2i  
COPY ./.s2i/bin/ /usr/libexec/s2i  
  
# Drop the root user and make the content of /opt/app-root owned by user 1001  
RUN chown -R 1001:1001 /opt/app-root  
  
ENV HEAP_FRACTION=0.5  
# Set the default user for the image, the user itself was created in the base
image  
USER 1001  
# Expose the ports the final image will expose  
EXPOSE 8080 8443 8082 8090  
# Set the default CMD to print the usage of the image, if somebody does docker
run  
CMD ["usage"]  

