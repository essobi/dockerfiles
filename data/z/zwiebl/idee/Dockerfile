FROM alpine:3.7  
MAINTAINER zwiebl <patrick@zwiebl.xyz>  
  
ADD https://raw.githubusercontent.com/zwieblauch/docker-idea-license-
server/master/idea_license_server /idea_license_server  
ADD https://github.com/zwieblauch/docker-idea-license-
server/raw/master/IntelliJIDEALicenseServer.html
/IntelliJIDEALicenseServer.html  
RUN chmod +x /idea_license_server  
WORKDIR /  
EXPOSE 1027  
ENTRYPOINT ["/idea_license_server"]  

