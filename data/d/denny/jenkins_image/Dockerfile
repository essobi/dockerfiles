########## How To Use Docker Image ###############  
##  
## Image Name: denny/jenkins_image:latest  
## Git link:
https://github.com/DennyZhang/jenkins_image/blob/master/Dockerfile  
##################################################  
# Base Docker image: https://hub.docker.com/r/denny/jenkins_image/  
  
FROM denny/jenkins_image:1.1  
  
LABEL maintainer "Denny<https://www.dennyzhang.com/contact>"  
  
HEALTHCHECK --interval=5m --timeout=3s \  
CMD curl -I http://localhost:8080 | grep "HTTP/1.1 200 OK" || exit 1  

