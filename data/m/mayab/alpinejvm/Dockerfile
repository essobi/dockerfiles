# import Alpine linux as base  
FROM alpine:3.4  
# install java  
RUN apk --update add openjdk8-jre  
  
# clean the apk cache  
RUN rm -rf /var/cache/apk/*  
  
CMD ["/usr/bin/java", "-version"]  

