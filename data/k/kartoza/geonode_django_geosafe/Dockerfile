ARG GEONODE_DJANGO_QGIS_SERVER_TAG=latest  
FROM kartoza/geonode_django_qgis-server:${GEONODE_DJANGO_QGIS_SERVER_TAG}  
  
# Clone source code  
WORKDIR /usr/src  
ARG GEOSAFE_TAG=2.6.x  
RUN git clone \--branch ${GEOSAFE_TAG} \--depth 1
https://github.com/kartoza/geosafe.git  
  
WORKDIR /usr/src/app  
  
# Upgrade dependencies  
ADD geosafe-tasks-headless-celeryconfig.py
/usr/src/geosafe/tasks/headless/celeryconfig.py  

