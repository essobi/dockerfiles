FROM blacklabelops/gcloud  
  
MAINTAINER Lucas Amorim <lucasamorim@protonmail.com>  
EXPOSE 8042  
LABEL version="1.0.0"  
LABEL app="pubsub-emulator"  
  
ENV CLOUDSDK_CORE_DISABLE_PROMPTS 1  
ENV DATA_DIR "/data"  
ENV HOST_PORT 8042  
ENV APP_HOME /pubsub  
WORKDIR $APP_HOME  
  
RUN yum install -y java-1.7.0-openjdk  
  
COPY . $APP_HOME  
  
RUN mkdir ${DATA_DIR}  
RUN gcloud components install -q pubsub-emulator beta  
  
ADD start-pubsub $APP_HOME/start-pubsub  
  
RUN chmod +x $APP_HOME/start-pubsub  
  
CMD ["/pubsub/start-pubsub"]  
  

