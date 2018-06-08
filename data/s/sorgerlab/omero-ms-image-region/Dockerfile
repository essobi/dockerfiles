FROM dpwrussell/omero-web-extended  
  
USER root  
  
WORKDIR /opt/omero/ms  
  
RUN yum install -y which \  
&& curl -OL
https://ci.appveyor.com/api/buildjobs/l2g74s7rgrx6u41d/artifacts/build%2Fdistributions%2Fomero-
ms-image-region-0.2.0-SNAPSHOT.zip \  
&& unzip *.zip \  
&& rm *.zip \  
&& ln -s omero-ms-image-region-*-SNAPSHOT omero-ms-image-region  
  
ADD conf.json /opt/omero/ms/omero-ms-image-region  
ADD entrypoint.sh /usr/local/bin/entrypoint.sh  
  
# TODO Figure this out  
# RUN chown -R omero-web:omero-web /opt/omero/ms/omero-ms-thumbnail \  
# && chmod -R a+w /opt/omero/ms/omero-ms-thumbnail  
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]  
  
# USER omero-web  
# ls /opt/omero/ms/omero-ms-thumbnail/  

