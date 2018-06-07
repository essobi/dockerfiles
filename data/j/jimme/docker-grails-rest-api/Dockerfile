FROM mozart/grails:3  
MAINTAINER Manuel Ortiz Bey <ortiz.manuel@mozartanalytics.com>  
  
WORKDIR /app  
  
RUN grails create-app --inplace --profile rest-api  
  
# Run Grails dependency-report command to pre-download dependencies but not  
# create unnecessary build files or artifacts.  
RUN grails dependency-report  
  
# Set Default Behavior  
ENTRYPOINT ["/bin/bash"]  

