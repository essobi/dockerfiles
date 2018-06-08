FROM jetty:alpine  
  
RUN apk add --no-cache graphviz fontconfig ttf-dejavu  
  
# http://plantuml.com/download  
ADD ./plantuml.war /var/lib/jetty/webapps/plantuml.war  
  
EXPOSE 8080  

