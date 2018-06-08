FROM meteorhacks/meteord:base  
  
MAINTAINER Noam Okman <noamokman@gmail.com>  
  
RUN git clone -b no-cdn https://github.com/noamokman/spyfall.git /repo  
RUN cp -R /repo/spyfall /app  
RUN chmod 777 -R $METEORD_DIR  
  
ENV METEOR_ALLOW_SUPERUSER true  
  
RUN $METEORD_DIR/lib/install_meteor.sh  
RUN $METEORD_DIR/lib/build_app.sh  
  
ENV ROOT_URL http://loaclhost  
  
EXPOSE 80

