FROM maven:3.3.3-jdk-7  
MAINTAINER Michael Sevilla <mikesevilla3@gmail.com>  
  
# install deps  
RUN apt-get update && apt-get install -y git openjdk-7-jdk curl && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /debian  
  
# download the tachyon packages  
RUN mkdir -p /src/ && \  
cd /src && \  
git clone https://github.com/amplab/tachyon.git && \  
cd tachyon && \  
git checkout -b branch-0.8 remotes/origin/branch-0.8 && \  
mvn install -DskipTests  
  
ADD build /  
RUN chmod 755 /build  
ENTRYPOINT ["/build"]  

