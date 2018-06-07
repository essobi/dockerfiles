FROM mariadb:10  
  
ARG BUILD_DATE  
ARG VCS_REF  
ARG VERSION  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.name="mariadb-pmm" \  
org.label-schema.description="mariadb-pmm - Mariadb + Client PMM (Percona
Monitoring and Management)" \  
org.label-schema.url="http://andradaprieto.es" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/jandradap/mariadb-pmm" \  
org.label-schema.vendor="Jorge Andrada Prieto" \  
org.label-schema.version=$VERSION \  
org.label-schema.schema-version="1.0" \  
maintainer="Jorge Andrada Prieto <jandradap@gmail.com>" \  
org.label-schema.docker.cmd=""  
  
COPY pmm.cnf /etc/mysql/conf.d/pmm.cnf  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
pmm-client \  
percona-toolkit \  
&& rm -rf /var/lib/apt/lists/* /tmp/* \  
&& chmod 644 /etc/mysql/conf.d/pmm.cnf  

