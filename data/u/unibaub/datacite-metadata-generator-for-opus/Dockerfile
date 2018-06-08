FROM php:7.1.7-apache  
  
COPY datacite_metadata_generator.html /var/www/html/index.html  
COPY src /var/www/html/src  
  
# Add Versioning Labels  
ARG BUILD_DATE  
ARG VCS_REF  
ARG VERSION  
LABEL org.label-schema.version="1.0" \  
org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.name="DataCite Metadata Generator for OPUS" \  
org.label-schema.vendor="University Library of Bamberg" \  
org.label-schema.version=$VERSION \  
org.label-schema.vcs-ref=$VCS_REF  

