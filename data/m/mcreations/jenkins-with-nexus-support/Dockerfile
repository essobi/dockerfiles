## -*- docker-image-name: "mcreations/jenkins-with-nexus-support" -*-  
FROM mcreations/jenkins:2.46.1  
MAINTAINER Kambiz Darabi <darabi@m-creations.net>  
MAINTAINER Reza Rahimi <rahimi@m-creations.net>  
  
USER ${user}  
  
# Requiresd parameters example  
#ENV NEXUS_NAME m-creations  
#ENV NEXUS_SSL_HOST nexus.example.com  
#ENV NEXUS_PASS *******  
ENV NEXUS_SSL_PORT 443  
ENV NEXUS_USER jenkins  
  
  
#ENV SCM_HOST git.example.com  
#ENV SCM_USER_EMAIL jenkins@example.com  
#ENV SCM_PASS  
ENV SCM_USER_ID jenkins  
ENV SCM_USER_NAME "Jenkins CI Administrator"  
RUN opkg update && \  
opkg install libstdcpp  
  
COPY start-jenkins-with-nexus-support /  
  
CMD ["/start-jenkins-with-nexus-support"]  

