FROM mhart/alpine-node  
  
LABEL date=05-feb-2018  
LABEL version=1.0  
  
RUN npm install -g reveal-md && \  
npm install phantomjs-prebuilt && \  
npm cache clean --force && \  
apk add --no-cache --update tini && \  
rm -Rf /var/cache/apk && \  
ln -s /node_modules/phantomjs-prebuilt/bin/phantomjs /bin  
  
ADD *.md /usr/src/app/  
  
EXPOSE 1948  
WORKDIR /usr/src/app  
  
ENTRYPOINT ["/sbin/tini", "-g", "--"]  
  
CMD reveal-md index.md  

