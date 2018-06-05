FROM ubuntu:14.04  
MAINTAINER Barry Pederson <bp@barryp.org>  
  
ENV TERM linux  
  
RUN apt-get -qq update; apt-get -qqy install openjdk-7-jre-headless unzip  
  
ADD
https://github.com/validator/validator.github.io/releases/download/20140222/vnu-20140222.zip
/opt/  
RUN unzip -d /opt /opt/vnu-20140222.zip  
  
USER nobody  
WORKDIR /opt/vnu  
CMD ["java", "-cp", "vnu.jar", "nu.validator.servlet.Main", "8888"]  
  
EXPOSE 8888  

