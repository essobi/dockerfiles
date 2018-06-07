FROM maven:3.3.9-jdk-8-alpine  
MAINTAINER Automation Team <devops@decibelinsight.com>  
  
#RUN apt-get update && apt-get install -y make binutils mysql-client && apt-
get clean  
RUN apk --no-cache add \  
make \  
binutils \  
ca-certificates \  
openssl \  
git \  
openssh \  
mysql-client \  
perl \  
&& update-ca-certificates  
COPY create_mysql.sh /bin/  
WORKDIR /data  

