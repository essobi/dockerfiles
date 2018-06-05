FROM alpine:3.7  
MAINTAINER bingo <bingov5@icloud.com>  
  
ADD https://raw.githubusercontent.com/bingozb/docker-idea-license-
server/master/idea_license_server /idea_license_server  
ADD https://raw.githubusercontent.com/bingozb/docker-idea-license-
server/master/IntelliJIDEALicenseServer.html /IntelliJIDEALicenseServer.html  
RUN chmod +x /idea_license_server  
WORKDIR /  
EXPOSE 1027  
ENTRYPOINT ["/idea_license_server"]

