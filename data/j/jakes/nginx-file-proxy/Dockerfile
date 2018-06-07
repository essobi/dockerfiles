FROM nginx  
MAINTAINER Jakes Lee <jakeslee66@gmail.com>  
  
ENV SOURCE_URL=""  
ENV HOSTNAME=""  
COPY . /app/  
WORKDIR /app/  
  
EXPOSE 80 443  
ENTRYPOINT ["./docker-entrypoint.sh"]  
CMD ["./run.sh"]  

