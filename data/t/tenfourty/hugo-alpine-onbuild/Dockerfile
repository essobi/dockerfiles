FROM alpine:3.5  
MAINTAINER Jeremy Brown <jeremy@tenfourty.com>  
  
################################################################################  
#  
# Hugo  
#  
################################################################################  
  
ENV HUGO_VERSION 0.20.7  
ENV HUGO_TAR hugo_${HUGO_VERSION}_Linux-64bit  
  
# Install packages  
# - curl (for install)  
# - pygments (for syntax highlighting)  
# - ca-certificates (needs to be updated)  
# then download and install Hugo  
RUN apk add --no-cache --update curl py-pygments ca-certificates && \  
cd /usr/local/bin && \  
curl -L
https://github.com/spf13/hugo/releases/download/v${HUGO_VERSION}/${HUGO_TAR}.tar.gz
| tar zxvf - && \  
apk del curl && \  
ln -s /usr/local/bin/hugo /usr/local/bin/hugo_${HUGO_VERSION}  
  
# create our /site directory where we will be running this from  
RUN mkdir /site  
WORKDIR /site  
  
# expose port 1313 for hugo  
EXPOSE 1313  
  
# by default serve up the local site mounted at /site, ideally from the
ONBUILD below  
CMD ["hugo", "server", "--bind", "0.0.0.0", "--cleanDestinationDir", "--
forceSyncStatic", "--buildDrafts", "--meminterval=1h", "--
memstats=/dev/stdout"]  
  
# add our files from the local folder into this docker image  
ONBUILD COPY site /site  

