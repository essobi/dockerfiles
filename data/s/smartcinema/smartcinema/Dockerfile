FROM ubuntu:16.04  
# copy source code into container  
COPY . /tmp/kino-build/  
  
# run build script  
# we do this to reduce the number of layers and trim our image  
RUN chmod u+x /tmp/kino-build/docker/build.sh && /tmp/kino-
build/docker/build.sh  
  
USER smartcinema  
WORKDIR /home/smartcinema  
EXPOSE 9090  
EXPOSE 8080  
ENV LANG=en_US.UTF-8 LC_ALL=en_US.UTF-8  
CMD ["supervisord", "-n", "-c", "/etc/supervisord.cfg"]  

