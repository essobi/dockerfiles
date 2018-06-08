#-----------------------------------------------------------------------------------------------------#  
# use the official Docker container  
#  
# official container  
# * deploys the build from the apache.org downloads page  
# * does not come with the supporting tools to configure the webservice as in
a Debian distribution  
# * make logs only accessible via the docker logs streams, so no persistence  
#  
# This Docker configuration is a minor adaptation to the Official container
setup.  
# Extra steps are in the layers for documenentation purpose  
#-----------------------------------------------------------------------------------------------------#  
FROM httpd:2.4  
# install additional software  
RUN apt-get update && apt-get install -y wget raptor2-utils curl emacs24
python-seqdiag  
  
# deploy emacs  
ENV DEBIAN_FRONTEND noninteractive  
ADD emacs /emacs  
#ADD emacs/export.el /emacs/export.el  
#ADD emacs/ob-blockdiag.el /emacs/ob-blockdiag.el  
#ADD emacs/.blockdiagrc /emacs/.blockdiagrc  
#ADD emacs/LiberationSans-Regular.ttf /emacs/LiberationSans-Regular.ttf  
ENV LANG en_US.UTF-8  
RUN emacs --batch --load /emacs/install.el  
  
# added the script in /scripts  
#RUN chmod a+rwX /emacs/org-export  
# make logs persistent in /logs  
RUN mkdir -p /logs && chmod -R 666 /logs  
RUN touch /logs/webservice.log && chmod 666 /logs/webservice.log  
  
# config directory holds the configuration  
ADD config /config  
ENV PATH /config/bin:$PATH  
# activates the necessary modules  
COPY config/httpd.conf /usr/local/apache2/conf/httpd.conf  
# vhosts configuration:  
# aliases /scripts with cgi-bin  
# sets logs to point to /logs  
COPY config/httpd-vhosts.conf /usr/local/apache2/conf/extra/httpd-vhosts.conf  
  
# scripts directory is the cgi-bin for the config  
ADD rules /rules  
ADD scripts /scripts  
RUN chmod -R 555 /scripts  
  
# www directory holds the document root  
ADD www /www  
RUN mkdir -p /www/results && chmod -R 777 /www/results  
RUN rm -rf /usr/local/apache2/htdocs && ln -s /www /usr/local/apache2/htdocs  
RUN rm -rf /vodap_validator/ && mkdir -p /vodap_validator && ln -s /scripts
/vodap_validator/bin  
RUN rm -rf /www/vodap_validator/ && mkdir -p /www/vodap_validator && ln -s
/scripts /www/vodap_validator/bin  
  
# Default Environment Variable assignments  
# these values can be overwritten at runtime  
ENV ENV_VALIDATOR_DOMAIN opendata.vlaanderen.be  
ENV ENV_VALIDATOR_LOCATION opendata.vlaanderen.be/validator  
ENV ENV_VALIDATOR_LOCATION_PATH validator  
ENV ENV_SPARQL_ENDPOINT_SERVICE_URL http://sparql-endpoint-service:8890/sparql  
  
# redefine the start of the service to be incorporate the runtime
configuration  
# of environment variables  
CMD ["/config/bin/start.sh"]  

