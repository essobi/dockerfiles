FROM dpwrussell/omero-web-extended  
  
USER root  
  
WORKDIR /opt/omero/ms  
  
RUN yum install -y which \  
&& curl -OL
https://ci.appveyor.com/api/buildjobs/k9iup704jm2b75mb/artifacts/build%2Fdistributions%2Fomero-
ms-pixel-buffer-0.2.0-SNAPSHOT.zip \  
&& unzip *.zip \  
&& rm *.zip \  
&& ln -s omero-ms-pixel-buffer-*-SNAPSHOT omero-ms-pixel-buffer  
  
ADD conf.json /opt/omero/ms/omero-ms-pixel-buffer/  
ADD entrypoint.sh /usr/local/bin/entrypoint.sh  
  
# TODO Figure this out  
# RUN chown -R omero-web:omero-web /opt/omero/ms/omero-ms-pixel-buffer \  
# && chmod -R a+w /opt/omero/ms/omero-ms-pixel-buffer  
VOLUME ["/OMERO"]  
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]  
  
# USER omero-web  
# ls /opt/omero/ms/omero-ms-pixel-buffer/  

