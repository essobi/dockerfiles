FROM o2rproject/geospatial-ctv:spatiotemporal  
  
LABEL maintainer "daniel.nuest@uni-muenster.de"  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
# for sys  
libapparmor-dev \  
&& apt-get autoremove -y \  
&& apt-get autoclean -y \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN R -e "devtools::install_github('r-hub/sysreqs'); \  
devtools::install_github('wch/harbor'); \  
devtools::install_github('o2r-project/containerit')"  
# Metadata http://label-schema.org/rc1/  
LABEL org.label-schema.vendor="o2r project" \  
org.label-schema.url="https://github.com/o2r-project/dockerfiles/" \  
org.label-schema.name="containerit base image" \  
org.label-schema.description="base image with extensive pre-installed packages
for containerization of R workspaces using the extension package
'containerit'" \  
org.label-schema.vcs-url=$VCS_URL \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.docker.schema-version="rc1"  
# docker build --tag geospatial-containerit .  
# docker run geospatial-ctv R

