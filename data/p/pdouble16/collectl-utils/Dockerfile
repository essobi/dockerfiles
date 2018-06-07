FROM debian:stretch-slim  
  
ARG DOCKERFILE_PATH  
ARG BUILD_DATE  
ARG SOURCE_REF  
ARG SOURCE_TYPE  
  
USER root  
RUN export DEBIAN_FRONTEND=noninteractive \  
&& apt-get update \  
&& apt-get install -yq curl apache2 colplot collectl ghostscript \  
&& rm -rf /var/lib/apt/lists/* \  
&& apt-get clean \  
&& mkdir -p /input \  
&& ln -sf /usr/share/colplot/conf_templates/colplot.apache.conf
/etc/apache2/conf-available/colplot.apache.conf \  
&& ln -sf /etc/apache2/conf-available/colplot.apache.conf /etc/apache2/conf-
enabled/colplot.apache.conf \  
&& ln -sf /etc/apache2/mods-available/cgi.load /etc/apache2/mods-
enabled/cgi.load  
  
COPY entrypoint.sh /  
  
VOLUME ["/input"]  
ENTRYPOINT ["/entrypoint.sh"]  
EXPOSE 80  
HEALTHCHECK \--interval=30s --timeout=30s --start-period=30s --retries=3 CMD [
"/usr/bin/curl", "-sf", "-o", "/dev/null", "http://localhost:80/colplot/" ]  
  
LABEL maintainer="Patrick Double <pat@patdouble.com>" \  
org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.license="MPL-2.0" \  
org.label-schema.vendor="https://github.com/double16" \  
org.label-schema.name="collectl-utils" \  
org.label-schema.url="https://github.com/double16/collectl-utils" \  
org.label-schema.docker.dockerfile="${DOCKERFILE_PATH}/Dockerfile" \  
org.label-schema.vcs-ref=$SOURCE_REF \  
org.label-schema.vcs-type=$SOURCE_TYPE \  
org.label-schema.vcs-url="https://github.com/double16/collectl-utils.git"  

