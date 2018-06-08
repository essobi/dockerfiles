FROM alpine as builder  
  
ARG GITHUB=https://github.com  
  
# Network Plugin  
ADD $GITHUB/mrkm4ntr/gitbucket-network-plugin/releases/download/1.5/gitbucket-
network-plugin_2.12-1.5.jar /  
  
# ipynb Plugin  
ADD $GITHUB/kounoike/gitbucket-ipynb-plugin/releases/download/0.3.0/gitbucket-
ipynb-plugin-assembly-0.3.0.jar /  
  
FROM sdyip/gitbucket:4.21.2-resilient  
  
# All official plugins  
RUN set -e;\  
mkdir /tmp/gitbucket;\  
unzip /opt/gitbucket.war -d /tmp/gitbucket;\  
mkdir plugins;\  
mv /tmp/gitbucket/WEB-INF/classes/plugins/*.jar plugins;\  
rm -r /tmp/gitbucket/*  
  
COPY \--from=builder *.jar plugins/  

