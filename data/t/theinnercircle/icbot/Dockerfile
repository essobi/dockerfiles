FROM phlak/hangoutsbot:2.8.0  
MAINTAINER The Inner Circle <https://github.com/TheInnerCircleO>  
  
USER root  
  
# Add our custom plugins  
COPY plugins/* /opt/hangoutsbot/hangupsbot/plugins/  
RUN chown -R hangoutsbot:hangoutsbot /opt/hangoutsbot/hangupsbot/plugins/  
  
USER hangoutsbot  

