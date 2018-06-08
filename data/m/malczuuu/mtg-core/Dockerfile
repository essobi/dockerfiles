# Stage 1: build application  
FROM gradle:4.8-jdk8-alpine as builder  
  
RUN mkdir app  
ADD . app  
  
RUN cd app/ && gradle clean build  
  
# Stage 2: setup docker url  
FROM openjdk:8-jre-alpine  
  
WORKDIR /  
  
ENV DB_HOST=localhost  
ENV DB_PORT=3306  
ENV DB_USER=mtg  
ENV DB_PASS=mtg  
ENV DB_NAME=mtg  
  
ENV MAIL_SMTP_HOST=localhost  
ENV MAIL_SMTP_PORT=1025  
ENV MAIL_SMTP_AUTH=false  
ENV MAIL_SMTP_STARTTLS_ENABLE=false  
ENV MAIL_FROM=john.doe@example.com  
ENV MAIL_USERNAME=john.doe@example.com  
ENV MAIL_PASSWORD=password  
  
ENV SPRING_LOG_LEVEL=info  
ENV LOG_LEVEL=info  
  
  
COPY \--from=builder /home/gradle/app/docker-entrypoint docker-entrypoint  
COPY \--from=builder /home/gradle/app/build/libs/*.jar app.jar  
  
VOLUME /data  
  
EXPOSE 8080  
CMD /docker-entrypoint  

