########## How To Use Docker Image ###############  
##  
## Image Name: denny/challenges-aws-ecs:latest  
## Git link: https://github.com/DennyZhang/challenges-aws-
ecs/blob/master/Dockerfile/nginx/Dockerfile  
## Build docker image:  
## time docker build --no-cache -f Dockerfile -t denny/challenges-aws-
ecs:nginx --rm=true .  
## Test image:  
## docker run -p 8081:8081 \--name nginx-test -d denny/challenges-aws-
ecs:nginx  
## # bind /etc/hosts for jenkins.dennyzhang.com and slack.dennyzhang.com  
## curl -I -L http://jenkins.dennyzhang.com:8081  
## curl -I -L http://slack.dennyzhang.com:8081  
##################################################  
# Base Docker image: https://hub.docker.com/_/nginx/  
  
FROM nginx  
ENV HTTP_PORT 8081  
ENV HTTPS_PORT 8441  
  
LABEL maintainer "Denny<https://www.dennyzhang.com/contact>"  
  
ADD default.conf /etc/nginx/conf.d/default.conf  
  
RUN apt-get -y update && apt-get install -y curl  
  
COPY ./docker-entrypoint.sh /docker-entrypoint.sh  
COPY ./docker-healthcheck.sh /docker-healthcheck.sh  
  
ENTRYPOINT /docker-entrypoint.sh  
  
HEALTHCHECK --interval=5m --timeout=3s \  
CMD /docker-healthcheck.sh || exit 1  

