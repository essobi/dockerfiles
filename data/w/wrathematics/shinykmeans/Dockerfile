FROM rocker/shiny  
MAINTAINER "Drew Schmidt" wrathematics@gmail.com  
  
  
# get and install the app  
ENV SHINY_PATH /srv/shiny-server  
ENV APP_NAME shinykmeans  
  
RUN apt-get update && apt-get install -y curl  
RUN rm -rf ${SHINY_PATH}/*  
RUN cd /tmp \  
&& curl -sOL https://github.com/wrathematics/${APP_NAME}/archive/master.zip \  
&& unzip master.zip  
  
RUN cp /tmp/${APP_NAME}-master/*.r ${SHINY_PATH}  
  
# cleanup  
RUN rm -rf /tmp/*  
RUN apt-get remove -y --purge curl  
  
# run the app  
# CMD ["bash"] ### for debugging  
CMD ["/usr/bin/shiny-server.sh"]  

