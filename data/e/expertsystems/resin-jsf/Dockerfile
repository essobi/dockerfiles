# Base image with Resin and bundled JSF version replaced with newer  
  
FROM expertsystems/resin:4.0.40  
# Remove bundled JSF version  
RUN cd ${RESIN_HOME}/lib && \  
rm javax.faces-2.1.24.jar  
  
# Add new JSF version  
RUN cd ${RESIN_HOME}/lib && \  
curl -O http://repo1.maven.org/maven2/com/sun/faces/jsf-api/2.2.7/jsf-
api-2.2.7.jar && \  
curl -O http://repo1.maven.org/maven2/com/sun/faces/jsf-impl/2.2.7/jsf-
impl-2.2.7.jar

