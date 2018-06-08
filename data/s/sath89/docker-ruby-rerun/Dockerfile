FROM ruby:latest  
  
RUN curl -o /usr/bin/docker "https://get.docker.com/builds/Linux/i386/docker-
latest" && chmod +x /usr/bin/docker  
RUN curl -o /usr/bin/kubectl "https://storage.googleapis.com/kubernetes-
release/release/v1.6.1/bin/linux/amd64/kubectl" && chmod +x /usr/bin/kubectl  
RUN apt-get update && apt-get install shellinabox -y && apt-get clean && rm
-rf /tmp/* /var/lib/apt/lists/* /var/tmp/*  
  
ENV APP_HOME /opt/app  
ENV APP_MAIN lib/main.rb  
ENV RERUN_OPTS ''  
ADD entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
CMD [""]  

