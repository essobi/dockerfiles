FROM blacklabelops/gcloud  
  
MAINTAINER Lucas Amorim <lucasamorim@protonmail.com>  
EXPOSE 8461  
ENV CLOUDSDK_CORE_DISABLE_PROMPTS 1  
ENV HOST_PORT 8461  
ENV APP_HOME /bigtable  
WORKDIR $APP_HOME  
  
COPY . $APP_HOME  
  
RUN gcloud components update  
RUN gcloud components update beta  
RUN gcloud components install -q bigtable beta  
  
ADD start-bigtable $APP_HOME/start-bigtable  
  
RUN chmod +x $APP_HOME/start-bigtable  
  
CMD ["/bigtable/start-bigtable"]  
  

