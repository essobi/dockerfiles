FROM dpwrussell/omero-web-extended  
  
USER root  
  
WORKDIR /opt/omero/ms  
  
RUN yum install -y which \  
&& curl -OL
https://ci.appveyor.com/api/buildjobs/xlcng2hcpnie5alg/artifacts/build%2Fdistributions%2Fomero-
ms-thumbnail-0.2.0-SNAPSHOT.zip \  
&& unzip *.zip \  
&& rm *.zip \  
&& ln -s omero-ms-thumbnail-*-SNAPSHOT omero-ms-thumbnail  
  
ADD conf.json /opt/omero/ms/omero-ms-thumbnail/  
ADD entrypoint.sh /usr/local/bin/entrypoint.sh  
  
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]  

