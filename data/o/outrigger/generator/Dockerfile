FROM outrigger/yeoman  
  
ENV OUTRIGGER_DRUPAL_VERSION 4.0.0  
ENV GADGET_VERSION=1.2.0  
ENV PATTERN_LAB_STARTER_VERSION=3.0.2  
  
# Need root user for installing  
USER root  
  
RUN npm install --global --silent generator-outrigger-
drupal@v$OUTRIGGER_DRUPAL_VERSION  
RUN npm install --global --silent generator-gadget@v$GADGET_VERSION  
RUN npm install --global --silent generator-pattern-lab-
starter@v$PATTERN_LAB_STARTER_VERSION  
# Back to yeoman user for running  
USER yeoman  
  
# Default command argument passed to yo as generator name  
CMD ["outrigger-drupal"]  

