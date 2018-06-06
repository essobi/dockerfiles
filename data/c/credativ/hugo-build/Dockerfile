FROM debian:stretch  
  
# Install pygments (for syntax highlighting)  
RUN apt-get -qq update \  
&& DEBIAN_FRONTEND=noninteractive apt-get -qq install -y --no-install-
recommends python-pygments git ca-certificates asciidoc curl  
  
# Install tools to build docs  
RUN DEBIAN_FRONTEND=noninteractive apt-get -qq install -y pandoc make sphinx-
common python3-sphinx python-recommonmark python-sphinx-rtd-theme \  
&& rm -rf /var/lib/apt/lists/*  
  
# Download and install hugo  
ENV HUGO_VERSION 0.30.2  
ENV HUGO_BINARY hugo_${HUGO_VERSION}_Linux-64bit.deb  
  
#ADD
https://github.com/spf13/hugo/releases/download/v${HUGO_VERSION}/${HUGO_BINARY}
/tmp/hugo.deb  
RUN curl -sL -o /tmp/hugo.deb \  
https://github.com/spf13/hugo/releases/download/v${HUGO_VERSION}/${HUGO_BINARY}
&& \  
dpkg -i /tmp/hugo.deb && \  
rm /tmp/hugo.deb && \  
mkdir /usr/share/blog  
  
# Download and install minify  
ENV MINIFY_VERSION 2.3.1  
ENV MINIFY_BINARY minify_${MINIFY_VERSION}_linux_amd64.tar.gz  
  
RUN curl -sL -o /tmp/minify.tar.gz \  
https://github.com/tdewolff/minify/releases/download/v${MINIFY_VERSION}/${MINIFY_BINARY}
&& \  
tar xf /tmp/minify.tar.gz -C /usr/local/bin && \  
rm /tmp/minify.tar.gz  
  
WORKDIR /usr/share/blog  
  
# Expose default hugo port  
EXPOSE 1313  
# Automatically build site  
ONBUILD ADD site/ /usr/share/blog  
ONBUILD RUN hugo -d /usr/share/nginx/html/  
  
# By default, serve site  
ENV HUGO_BASE_URL http://localhost:1313  
CMD hugo server -b ${HUGO_BASE_URL} \--bind=0.0.0.0  

