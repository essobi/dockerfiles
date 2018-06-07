FROM tenforce/tomcat  
  
MAINTAINER Bert Van Nuffelen <bert.van.nuffelen@tenforce.com>  
  
# per example expose an extra port.  
EXPOSE 8081  
ADD contexts /contexts  
  
RUN wget http://repository.epimorphics.com/com/epimorphics/lda/elda-
common/1.3.18/elda-common-1.3.18.war  
RUN cp elda-common-1.3.18.war /webapps/elda-common-1.3.18.war  
RUN wget http://repository.epimorphics.com/com/epimorphics/lda/elda-
assets/1.3.18/elda-assets-1.3.18.war  
RUN cp elda-assets-1.3.18.war /webapps/elda-assets-1.3.18.war  
  
# overwrite defaults  
ADD myconfig /myconfig  
RUN cp /myconfig/* config  
  
# overwrite the default entrypoint  
# this is needed because RUN cp seem not to be executed as expected.  
ENTRYPOINT ["/myconfig/run.sh"]  
  

