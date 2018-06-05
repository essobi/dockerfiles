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
#FROM httpd:2.4  
# use a variant of the official HTTPD container build on Debian Stretch  
# this is temporary until the official moves to it  
FROM solsson/httpd-stretch  
  
# install additional software  
# especially deploy the ruby linkeddata gem  
RUN apt-get update \  
&& apt-get install -y curl vim \  
&& apt-get install -y ruby ruby-dev build-essential zlib1g-dev  
  
RUN gem install linkeddata  
RUN apt-get remove -y build-essential \  
&& apt-get autoremove -y \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# make logs persistent in /logs  
RUN mkdir -p /logs && chmod -R 666 /logs  
  
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
ADD scripts /scripts  
RUN chmod -R 555 /scripts && mkdir -p /scripts/tmp && chmod 666 /scripts/tmp  
  
# www directory holds the document root  
ADD www /www  
RUN rm -rf /usr/local/apache2/htdocs && ln -s /www /usr/local/apache2/htdocs  
RUN mkdir -p /www/tmp && chmod 777 /www/tmp  
  
# Default Environment Variable assignments  
# these values can be overwritten at runtime  
ENV ENV_SERVERNAME ldsb-data.vlaanderen.be  
ENV ENV_URI_DOMAIN data.vlaanderen.be  
ENV ENV_SPARQL_ENDPOINT_SERVICE_URL http://sparql-endpoint-service:8890/sparql  
ENV ENV_CONTEXTMAP=file:///config/context.map  
  
# redefine the start of the service to be incorporate the runtime
configuration  
# of environment variables  
ENTRYPOINT ["/config/bin/start.sh"]  

