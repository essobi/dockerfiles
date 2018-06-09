FROM openjdk:8-jre-alpine  
LABEL Description="A simple containerization of giter8.
https://github.com/moredip/giter8"  
  
RUN apk --update add curl ca-certificates openssl bash  
ENV CONSCRIPT_HOME /root  
  
# install conscript  
RUN curl
https://raw.githubusercontent.com/foundweekends/conscript/master/setup.sh | sh  
  
# install giter8 using conscript  
RUN ~/bin/cs foundweekends/giter8  
  
# trigger g8 to install dependencies, including half the internet apparently  
RUN ~/bin/g8 || true

