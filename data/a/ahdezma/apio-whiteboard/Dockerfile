FROM anapsix/alpine-java  
MAINTAINER Alejandro Hernández  
ENV JAVA_OPTS ""  
ADD apio.jar /apio.jar  
ADD logback.xml /logback.xml  
ADD run.sh /run.sh  
RUN chmod +x run.sh  
RUN apk update && apk add busybox-extras  
EXPOSE 8080 5000 6666  
RUN mkdir /deploy  
RUN mkdir /modules  
COPY modules/*.jar /modules/  
COPY com.liferay.apio.architect.cors.jar /modules/  
COPY com.liferay.apio.architect.application.internal.ApioApplication.cfg
/modules/  
CMD ["./run.sh"]

