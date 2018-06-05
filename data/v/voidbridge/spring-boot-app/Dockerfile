FROM voidbridge/base-centos7  
MAINTAINER Voidbridge <developers@voidbridge.com>  
ENV JDK_VERSION=1.8.0_11  
  
LABEL io.k8s.description="Builder image for a Spring Boot Java application" \  
io.k8s.display-name="Spring Boot App"  
  
# Install some extra tools  
RUN yum install -y bind-utils telnet hostname && \  
yum clean all -y  
  
# Install Java  
COPY ./files/jdk-8u11-linux-x64.rpm /tmp  
RUN rpm -ivh /tmp/jdk-8u11-linux-x64.rpm  
  
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

