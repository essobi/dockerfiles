FROM maven:3-jdk-8  
MAINTAINER Go About <tech@goabout.com>  
  
ENV BRANCH=master \  
JAVA_MX=1G  
  
RUN mkdir /tmp/build && \  
cd /tmp/build && \  
wget -O src.zip --progress dot:mega
https://github.com/opentripplanner/OpenTripPlanner/archive/$BRANCH.zip && \  
unzip src.zip && \  
cd OpenTripPlanner-$BRANCH && \  
mvn package -DskipTests && \  
mkdir -p /usr/local/share/java && \  
mv target/otp-*shaded.jar /usr/local/share/java/otp.jar && \  
rm -r /tmp/build ~/.m2/repository  
  
COPY otp /usr/local/bin/  
RUN chmod 755 /usr/local/bin/*  
  
EXPOSE 8080  

