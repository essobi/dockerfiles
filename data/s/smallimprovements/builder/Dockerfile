FROM openjdk:8-alpine  
  
RUN apk add --update \  
git \  
su-exec  
  
RUN adduser -h /home/build-user -D -g "" build-user  
  
COPY prepare-build.sh /home/build-user/prepare-build.sh  
COPY npmrc /home/build-user/.npmrc  
ENV GRADLE_USER_HOME=/cache  
  
WORKDIR /project  
  
# please DO NOT remove the braces from the entrypoint statement  
# (without the braces the command line arguments are not processed)  
ENTRYPOINT ["/home/build-user/prepare-build.sh"]

