FROM httpd:2.4.29  
# vim for debug  
# git is widly used for this app  
# jq is used to read JSON config file  
# curl is used to query github API  
RUN apt-get update && apt-get install -yq --no-install-recommends vim git ca-
certificates jq curl  
  
# nodejs installation used for index.html resources  
# jquery and material-components-web  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -  
RUN apt-get install -y build-essential nodejs  
  
COPY index.html /usr/local/apache2/htdocs/  
COPY index2.html /usr/local/apache2/htdocs/  
COPY index.css /usr/local/apache2/htdocs/  
COPY package.json /usr/local/apache2/htdocs/  
RUN cd /usr/local/apache2/htdocs/ && npm install  
  
COPY entrypoint.sh /  
COPY dump-github.periodically.sh /  
COPY config.json /  
  
# ezmasterization of ezmaster-globs  
# see https://github.com/Inist-CNRS/ezmaster  
RUN echo '{ \  
"httpPort": 80, \  
"configPath": "/config.json", \  
"configType": "json", \  
"dataPath": "/usr/local/apache2/htdocs" \  
}' > /etc/ezmaster.json  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD [ "httpd-foreground" ]  
EXPOSE 80

