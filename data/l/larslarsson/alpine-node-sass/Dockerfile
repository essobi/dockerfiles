FROM mhart/alpine-node:6.7.0  
ENV LIBSASS_VERSION=3.3.1 SASSC_VERSION=3.3.1  
RUN apk --update add git build-base libstdc++ make g++ python curl && \  
git clone https://github.com/sass/sassc && \  
cd sassc && git checkout $SASSC_VERSION && \  
git clone https://github.com/sass/libsass && \  
cd libsass && \  
git checkout $LIBSASS_VERSION && \  
cd .. && SASS_LIBSASS_PATH=/sassc/libsass make && \  
mv bin/sassc /usr/bin/sassc && \  
npm install -g node-sass@3.8.0  
  
RUN curl -L -o /usr/local/bin/dumb-init https://github.com/Yelp/dumb-
init/releases/download/v1.0.0/dumb-init_1.0.0_amd64 && \  
chmod +x /usr/local/bin/dumb-init && \  
apk del git build-base curl && \  
rm -rf /var/cache/apk/* /sassc  
  
ENTRYPOINT ["dumb-init"]  
CMD ["node"]  
  

