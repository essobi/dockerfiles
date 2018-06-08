FROM mhart/alpine-node  
  
LABEL maintainer="Sherpany DevOps Team <devops@sherpany.com>"  
  
ENV PATH=/usr/lib/node_modules/.bin:$PATH  
  
RUN mkdir -p /app/reports /app/xunit  
  
WORKDIR /app/reports  
  
RUN npm install -g xunit-viewer && \  
rm -rf /usr/share/man /tmp/* \  
/root/.npm /root/.node-gyp \  
/usr/lib/node_modules/npm/man \  
/usr/lib/node_modules/npm/doc \  
/usr/lib/node_modules/npm/html && \  
find /usr/lib/node_modules/npm -name test -o -name .bin -type d | xargs rm -rf  
  
ENTRYPOINT ["xunit-viewer"]  
CMD ["--output=/app/xunit/"]  

