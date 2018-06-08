FROM node:8.0  
MAINTAINER Mien <mien@dreamxo.net>  
  
# install dependencies  
RUN apt-get update && \  
apt-get install -y --no-install-recommends unzip calibre xsltproc curl && \  
apt-get clean && \  
apt-get autoclean && \  
apt-get autoremove && \  
rm -rf /var/lib/apt/lists/*  
## Install Calibre and noto fonts  
RUN echo "deb http://http.debian.net/debian jessie-backports main" >
/etc/apt/sources.list.d/backports.list && \  
apt-get update && \  
apt-get install -y --no-install-recommends calibre fonts-noto fonts-noto-cjk
locales-all && \  
apt-get clean && \  
apt-get autoclean && \  
apt-get autoremove && \  
rm -rf /var/lib/apt/lists/*  
# install gitbook toolchain and dependencies  
RUN npm install -g gitbook-cli ebook-convert svgexport sqlite3 nodejieba && \  
gitbook fetch  
  
# "EXDEV: cross-device link not permitted",
cef="https://github.com/npm/npm/issues/9863"  
RUN cd $(npm root -g)/npm && \  
npm install fs-extra && \  
sed -i -e s/graceful-fs/fs-extra/ -e s/fs\\.rename/fs.move/
./lib/utils/rename.js  
# clean temp files  
RUN rm -rf /var/lib/apt/lists/* /var/cache/apt/* /root/.npm /tmp/npm*  
# add var  
ENV BOOKROOT /gitbook/www/  
  
# default content and cache node_modules.  
WORKDIR $BOOKROOT  
COPY . $BOOKROOT  
RUN gitbook install  
  
# clean  
RUN rm -f searchindex Dockerfile  
  
EXPOSE 4000  
CMD ["gitbook","serve"]

