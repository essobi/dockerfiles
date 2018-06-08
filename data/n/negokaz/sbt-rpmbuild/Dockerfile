FROM centos:7  
MAINTAINER negokaz <negokaz@gmail.com>  
  
ENV OPENJDK_VERSION 1.8.0  
RUN curl https://bintray.com/sbt/rpm/rpm | tee /etc/yum.repos.d/bintray-sbt-
rpm.repo \  
&& yum install -y \  
rpmdevtools \  
yum-utils \  
java-${OPENJDK_VERSION}-openjdk \  
java-${OPENJDK_VERSION}-openjdk-devel \  
sbt \  
&& yum clean all \  
&& rm -rf /var/cache/*  
  
VOLUME /project  
WORKDIR /project  
  
ENTRYPOINT ["/usr/bin/sbt"]  
CMD [""]  

