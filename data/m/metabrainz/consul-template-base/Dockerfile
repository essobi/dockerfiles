FROM metabrainz/base-image:v0.9.22-5  
ARG CT_VERSION="0.19.4"  
ARG CT_RELEASE="consul-template_${CT_VERSION}_linux_amd64.zip"  
ARG BUILD_DATE  
ARG VCS_REF  
  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.vcs-url="https://github.com/metabrainz/docker-consul-
template-base.git" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.schema-version="1.0.0-rc1" \  
org.label-schema.vendor="MetaBrainz Foundation" \  
org.metabrainz.based-on-image="metabrainz/base-image:v0.9.22-5" \  
org.metabrainz.consul-template.version="0.19.4"  
  
RUN curl -O https://releases.hashicorp.com/consul-
template/$CT_VERSION/$CT_RELEASE && \  
unzip -d /usr/local/bin $CT_RELEASE && \  
chmod 755 /usr/local/bin/consul-template && \  
rm -rf $CT_RELEASE /var/lib/apt/lists/*  
  
COPY run-consul-template /usr/local/bin/  
  
RUN chmod 755 /usr/local/bin/run-consul-template  

