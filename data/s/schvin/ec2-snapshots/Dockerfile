FROM java:8  
MAINTAINER George Lewis <schvin@schvin.net>  
  
ENV REFRESHED_AT 2016-09-07  
ENV EC2_HOME /s/ec2/ec2-api-tools  
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64/jre/  
  
RUN apt-get update -y && \  
apt-get install -y csh curl libdate-manip-perl libtime-format-perl perl unzip  
  
# preload app  
RUN mkdir -p /s/ec2  
ADD bin /s/ec2/bin/  
ADD lib /s/ec2/lib/  
  
# setup user  
RUN groupadd s-ec2  
RUN useradd s-ec2 -g s-ec2 -d /s/ec2  
RUN chown -R s-ec2:s-ec2 /s/ec2  
ENV HOME /s/ec2  
USER s-ec2  
  
# prep ec2  
WORKDIR /s/ec2  
RUN curl -O http://s3.amazonaws.com/ec2-downloads/ec2-api-tools.zip  
RUN unzip ec2-api-tools.zip  
RUN rm ec2-api-tools.zip  
RUN ln -s ec2* ec2-api-tools  
  
# run app  
ENTRYPOINT /s/ec2/bin/snap-all-volumes.csh  

