#######################################################################  
# Mocks de hotel - CVC Responsivo  
#######################################################################  
FROM sciensa2/soapui-runner:latest  
MAINTAINER Leonardo Gaona <leonardo.gaona@sciensa.com>  
  
ADD hotel-mocks/cangooroo/src/main/resources/mocks/project.xml
$SOAPUI_PRJ/cangooroo.xml  
ADD hotel-mocks/cvc/src/main/resources/mocks/project.xml $SOAPUI_PRJ/cvc.xml  
ADD hotel-mocks/expedia/src/main/resources/mocks/project.xml
$SOAPUI_PRJ/expedia.xml  
ADD hotel-mocks/hotelbeds/src/main/resources/mocks/project.xml
$SOAPUI_PRJ/hotelbeds.xml  
ADD hotel-mocks/juniper/src/main/resources/mocks/project.xml
$SOAPUI_PRJ/juniper.xml  
ADD hotel-mocks/omnibees/src/main/resources/mocks/project.xml
$SOAPUI_PRJ/omnibees.xml  
ADD hotel-mocks/hotels/src/main/resources/mocks/project.xml
$SOAPUI_PRJ/hotels.xml  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
CMD ["start-soapui"]  

