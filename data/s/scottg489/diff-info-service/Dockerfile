#FROM ubuntu:latest  
FROM java:8  
RUN mkdir /opt/diff-info-service/  
ADD https://oss.jfrog.org/artifactory/repo/com/github/scottg489/diff-info-
service/\\[RELEASE\\]/diff-info-service-\\[RELEASE\\]-capsule.jar /opt/diff-
info-service/  
CMD ["java", "-jar", "/opt/diff-info-service/diff-info-
service-[RELEASE]-capsule.jar", "server"]

