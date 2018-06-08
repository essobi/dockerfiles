FROM webhippie/python:2  
MAINTAINER Thomas Boerger <thomas@webhippie.de>  
  
WORKDIR /srv/app  
ENTRYPOINT ["/usr/bin/entrypoint"]  
CMD ["bash"]  
  
RUN apk update && \  
apk add \  
texlive-full@testing \  
xz \  
zlib-dev \  
jpeg-dev && \  
curl -sLo - \  
ftp://ftp.tug.org/historic/systems/texlive/2016/texlive-20160523b-texmf.tar.xz
| tar -Jxvf - --strip 1 -C /tmp && \  
cp -rf \  
/tmp/texmf-dist/* \  
/usr/share/texmf-dist/ && \  
rm -rf \  
/tmp/texmf-dist && \  
apk fix \  
texlive \  
texlive-full && \  
pip install \  
reportlab \  
rst2pdf \  
sphinxcontrib-phpdomain \  
sphinxcontrib-golangdomain \  
sphinxcontrib-disqus \  
sphinxcontrib-email \  
sphinxcontrib-fancybox \  
sphinxcontrib-gravatar \  
sphinxcontrib-httpdomain \  
sphinxcontrib-imagehelper \  
sphinxcontrib-images \  
sphinx==1.2.2 && \  
rm -rf /var/cache/apk/*  
  
ADD rootfs /  
  
ARG VERSION  
ARG BUILD_DATE  
ARG VCS_REF  
  
LABEL org.label-schema.version=$VERSION  
LABEL org.label-schema.build-date=$BUILD_DATE  
LABEL org.label-schema.vcs-ref=$VCS_REF  
LABEL org.label-schema.vcs-url="https://github.com/dockhippie/sphinx.git"  
LABEL org.label-schema.name="Sphinx"  
LABEL org.label-schema.vendor="Thomas Boerger"  
LABEL org.label-schema.schema-version="1.0"  

