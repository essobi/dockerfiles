FROM debian:wheezy  
MAINTAINER MeteorHacks Pvt Ltd.  
  
ENV METEORD_DIR /opt/meteord  
ENV PHANTOMJS_BIN=/usr/local/bin/phantomjs  
ENV JASMINE_BROWSER=PhantomJS  
  
COPY scripts $METEORD_DIR  
  
RUN bash $METEORD_DIR/init.sh  
  
EXPOSE 80  
ENTRYPOINT bash $METEORD_DIR/run_app.sh  

