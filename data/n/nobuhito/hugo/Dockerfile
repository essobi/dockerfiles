FROM debian:jessie  
# MAINTAINER yigal@publysher.nl  
MAINTAINER nobuhito.sato@gmail.com  
  
RUN apt-get -qq update \  
&& DEBIAN_FRONTEND=noninteractive apt-get -qq install -y --no-install-
recommends apt-utils ca-certificates curl zip  
  
# Install git (for git submodule)  
RUN apt-get -qq update \  
&& DEBIAN_FRONTEND=noninteractive apt-get -qq install -y --no-install-
recommends git-core  
  
# Install pngquanti, jpegtran (for image resize)  
RUN apt-get -qq update \  
&& DEBIAN_FRONTEND=noninteractive apt-get -qq install -y --no-install-
recommends pngquant libjpeg-turbo-progs  
  
RUN rm -fr /var/lib/apt/lists/*  
  
# Download and install hugo  
ENV HUGO_VERSION 0.25.1  
ENV HUGO_TARBALL hugo_${HUGO_VERSION}_Linux-64bit.tar.gz  
ENV HUGO_BINARY hugo_${HUGO_VERSION}  
  
ADD
https://github.com/spf13/hugo/releases/download/v${HUGO_VERSION}/${HUGO_TARBALL}
/usr/local/  
RUN tar xzf /usr/local/${HUGO_TARBALL} -C /usr/local/ \  
&& ln -s /usr/local/hugo /usr/local/bin/hugo \  
&& rm /usr/local/${HUGO_TARBALL}  
  
# Create working directory  
RUN mkdir /usr/share/blog  
WORKDIR /usr/share/blog  
  
# Expose default hugo port  
EXPOSE 1313  
# Automatically build site  
ONBUILD ADD site/ /usr/share/blog  
ONBUILD RUN hugo -d /usr/share/nginx/html/  
  
# By default, serve site  
ENV HUGO_BASE_URL http://localhost:1313  
CMD hugo server -b ${HUGO_BASE_URL}  

