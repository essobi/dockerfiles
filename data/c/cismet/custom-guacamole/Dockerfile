FROM glyptodon/guacamole  
RUN apt-get update -y  
RUN apt-get install -y zip  
RUN mkdir /opt/guacamole/customization/  
WORKDIR /opt/guacamole/customization/  
COPY logo60.png /opt/guacamole/customization/images/guac-tricolor.png  
COPY en.json /opt/guacamole/customization/translations/en.json  
RUN zip -ur ../guacamole.war images/guac-tricolor.png  
RUN zip -ur ../guacamole.war translations/en.json  
RUN rm -rf /usr/local/tomcat/webapps/ROOT  
RUN sed -i 's/ln -sf \/opt\/guacamole\/guacamole.war
\/usr\/local\/tomcat\/webapps\//ln -sf \/opt\/guacamole\/guacamole.war
\/usr\/local\/tomcat\/webapps\/ROOT.war/' /opt/guacamole/bin/start.sh  

