FROM ubuntu:14.04  
  
ENV CHEF_VERSION=12.7.2 \  
CHEF_SHA1=9bc701d90ba12c71fbe51a8bdcdf25e864375f4e \  
CHEF_SERVER_CORE_VERSION=12.4.1 \  
CHEF_SERVER_CORE_SHA1=a75e8dbcce749adf61a60ca0ccf25fc041e4774a \  
CHEF_ORGANISATION=example \  
CHEF_USER=admin \  
CHEF_FIRST_NAME=admin \  
CHEF_LAST_NAME=admin \  
CHEF_EMAIL=admin@example.com \  
CHEF_PASSWORD=pleasechangethis \  
PUBLIC_URL=http://chef.example.com  
  
ARG BUILD_DATE  
ARG VCS_REF  
ARG VERSION  
  
EXPOSE 80 443  
  
VOLUME /var/opt/opscode  
  
ADD ./resources /resources  
  
RUN /resources/build && rm -rf /resources  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
LABEL "maintainer"="cloudsquad@fxinnovation.com" \  
"org.label-schema.name"="chefserver" \  
"org.label-schema.base-image.name"="docker.io/library/ubuntu" \  
"org.label-schema.base-image.version"="14.04" \  
"org.label-schema.description"="Chef-Server in a container" \  
"org.label-schema.url"="https://www.chef.io" \  
"org.label-schema.vcs-url"="https://bitbucket.org/fxadmin/public-common-
docker-chefserver" \  
"org.label-schema.vendor"="FXinnovation" \  
"org.label-schema.schema-version"="1.0.0-rc.1" \  
"org.label-schema.applications.chef.version"=$CHEF_VERSION \  
"org.label-schema.applications.chef-server-
core.version"=$CHEF_SERVER_CORE_VERSION \  
"org.label-schema.vcs-ref"=$VCS_REF \  
"org.label-schema.version"=$VERSION \  
"org.label-schema.build-date"=$BUILD_DATE \  
"org.label-schema.usage"="Please read readme in vsc-ref"  

