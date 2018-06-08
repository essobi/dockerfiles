FROM debian:stretch-slim  
  
ARG BUILD_DATE  
ARG VCS_REF  
ARG DEBIAN_FRONTEND=noninteractive  
  
ENV PANDOC_VER=2.0.6  
  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.vcs-url="https://github.com/php-earth/docker-pandoc.git" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.schema-version="1.0" \  
org.label-schema.vendor="PHP.earth" \  
org.label-schema.name="docker-pandoc" \  
org.label-schema.description="Pandoc Docker image" \  
org.label-schema.url="https://github.com/php-earth/docker-pandoc"  
  
RUN apt-get update && apt-get -y --no-install-recommends install \  
wget \  
ca-certificates \  
texlive \  
texlive-xetex \  
texlive-fonts-extra \  
texlive-luatex \  
lmodern \  
netbase \  
&& cd /opt && wget
https://github.com/jgm/pandoc/releases/download/$PANDOC_VER/pandoc-$PANDOC_VER-1-amd64.deb
\  
&& dpkg -i pandoc-$PANDOC_VER-1-amd64.deb \  
&& apt-get -y autoremove && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
/opt/*  
  
WORKDIR /opt  
  
CMD ["/usr/bin/pandoc", "--help"]  

