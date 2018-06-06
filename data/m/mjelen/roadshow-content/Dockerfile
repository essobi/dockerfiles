FROM docker.io/osevg/workshopper  
  
ENV CONTENT_URL_PREFIX="file:///opt/data/workshopper-content"  
ENV WORKSHOPS_URLS="file:///opt/data/workshopper-
content/_workshops/roadshow.yml"  
ENV DEFAULT_LAB="roadshow"  
USER root  
  
RUN yum -y install git && mkdir /opt/data && cd /opt/data && \  
git clone https://github.com/osevg/workshopper-content.git && \  
rm -rf workshopper-content/.git && \  
chown jboss:root -R /opt/data && chmod 777 -R /opt/data  
  
USER jboss  

