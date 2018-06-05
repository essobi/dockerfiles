FROM openjdk:8u151-jre-alpine  
LABEL org.label-schema.schema-version = "1.0"  
LABEL org.label-schema.description = "A simple containerization of giter8.
https://github.com/moredip/giter8"  
LABEL org.label-schema.vcs-url = "https://github.com/avast/giter8-docker-
image"  
  
RUN apk --update add curl ca-certificates openssl bash  
ENV CONSCRIPT_HOME /root/  
# install conscript  
RUN curl -s curl
https://raw.githubusercontent.com/foundweekends/conscript/master/setup.sh | sh  
  
# install giter8 using conscript  
RUN ~/bin/cs n8han/giter8  
  
# trigger g8 to install dependencies, including half the internet apparently  
RUN ~/bin/g8 || true  
  
VOLUME /g8out  
WORKDIR /g8out  
  
ENTRYPOINT ["/root/bin/g8","--force"]  

