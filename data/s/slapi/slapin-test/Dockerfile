FROM slapi/ruby:latest  
  
MAINTAINER SLAPI Devs  
  
# Use labels to create help commands  
# arg="description"  
LABEL "description"="Uses entire data package from chat"  
LABEL "parse"="parse all data from slack"  
  
RUN mkdir -p /parse && chmod 777 /parse && \  
apk update && apk add \  
supervisor && \  
rm -rf /var/cache/apk/* && \  
rm -rf /tmp/*  
  
WORKDIR /parse  
  
# Copy app to container  
COPY . ./  
  
COPY supervisord.conf /etc/supervisor.d/supervisord.conf  
  
ENTRYPOINT ["supervisord", "-c", "/etc/supervisor.d/supervisord.conf", "-n"]  

