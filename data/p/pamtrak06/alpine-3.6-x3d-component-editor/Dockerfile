FROM httpd:2.4-alpine  
RUN apk add --update \  
git  
RUN git clone https://github.com/x3dom/component-editor.git /component-editor  
RUN mv /component-editor/* /usr/local/apache2/htdocs  
#/var/www/localhost/htdocs

