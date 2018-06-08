#lordius/alpine-ngrok  
FROM alpine:3.4  
LABEL maintainer=andriy.khomych@gmail.com  
RUN apk --no-cache update  
#Create /temp_dir for using  
RUN mkdir /temp_docker && chmod -R +x /temp_docker && cd /temp_docker  
# Add config script.  
RUN mkdir /root/.ngrok2 && chmod -R +x /root/.ngrok2  
COPY ngrok.yml /root/.ngrok2/  
#Add our ngrok version  
ADD ngrok-stable-linux-386.zip /temp_docker/ngrok-stable-linux-386.zip  
RUN cd /temp_docker && unzip /temp_docker/ngrok-stable-linux-386.zip  
RUN cp /temp_docker/ngrok /usr/local/bin/  
RUN chmod +x /usr/local/bin/ngrok  
  
COPY docker-entrypoint.sh /usr/local/bin/  
RUN chmod +x /usr/local/bin/docker-entrypoint.sh  
RUN rm -rf /temp_docker  
ENTRYPOINT ["docker-entrypoint.sh"]  
EXPOSE 4040  

