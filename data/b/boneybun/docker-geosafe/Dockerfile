FROM kartoza/qgis-server:LTR  
  
# Clone plugin source code  
WORKDIR /opt/qgis-server/plugins  
ARG OTF_PROJECT_TAG=master  
RUN git clone \--branch ${OTF_PROJECT_TAG} \--depth 1
https://github.com/kartoza/otf-project.git  
  
WORKDIR /  

