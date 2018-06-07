FROM camunda/camunda-bpm-platform:tomcat-7.8.0  
RUN rm -r webapps/camunda-invoice  
  
COPY docker/camunda/conf/ conf  
  
COPY docker/camunda/lib/* lib  
  
COPY docker/camunda/webapps/camunda/commons/assets/
webapps/camunda/app/welcome/assets  
  
COPY docker/camunda/webapps/camunda/commons/styles/
webapps/camunda/app/welcome/styles  
  
COPY docker/camunda/webapps/camunda/welcome/index.html
webapps/camunda/app/welcome  
  
COPY docker/camunda/webapps/camunda/welcome/scripts/config.js
webapps/camunda/app/welcome/scripts  
  
COPY docker/camunda/webapps/camunda/commons/assets/
webapps/camunda/app/admin/assets  
  
COPY docker/camunda/webapps/camunda/commons/styles/
webapps/camunda/app/admin/styles  
  
COPY docker/camunda/webapps/camunda/admin/index.html webapps/camunda/app/admin  
  
COPY docker/camunda/webapps/camunda/commons/assets/
webapps/camunda/app/cockpit/assets  
  
COPY docker/camunda/webapps/camunda/commons/styles/
webapps/camunda/app/cockpit/styles  
  
COPY docker/camunda/webapps/camunda/cockpit/index.html
webapps/camunda/app/cockpit  
  
COPY docker/camunda/webapps/camunda/commons/assets/
webapps/camunda/app/tasklist/assets  
  
COPY docker/camunda/webapps/camunda/commons/styles/
webapps/camunda/app/tasklist/styles  
  
COPY docker/camunda/webapps/camunda/tasklist/index.html
webapps/camunda/app/tasklist  
  
COPY docker/camunda/webapps/camunda/tasklist/scripts/config.js
webapps/camunda/app/tasklist/scripts  

