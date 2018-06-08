FROM tomcat:alpine  
  
RUN apk add --no-cache curl graphviz ttf-dejavu \  
&& rm -rf webapps/* \  
&& curl -L https://downloads.sourceforge.net/project/plantuml/plantuml.war >
./webapps/plantuml.war \  
&& apk del curl  

