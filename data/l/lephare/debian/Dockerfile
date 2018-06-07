FROM debian:jessie  
  
RUN echo 'Europe/Paris' | tee /etc/timezone  
RUN dpkg-reconfigure -f noninteractive tzdata  
  
ENV DOCKER_USER_ID 1000  

