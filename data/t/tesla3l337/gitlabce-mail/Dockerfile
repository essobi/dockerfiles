# gitlabce-mail  
#  
# VERSION 0.0.2  
FROM gitlab/gitlab-ce:latest  
MAINTAINER Tesla <tesla@v-ip.fr>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get install -y postfix  
COPY ./main.cf /etc/postfix/  
RUN echo "gitlab" > /etc/mailname  
  
COPY ./docker-entrypoint.sh /  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  

