FROM alpine:3.7  
  
RUN apk add \--no-cache \--virtual build-deps build-base git boost-dev zlib-
dev && \  
git clone \--depth 1 \--branch master \--single-branch \  
git://github.com/JohnLangford/vowpal_wabbit.git /opt/vowpal_wabbit/ && \  
cd /opt/vowpal_wabbit/ && \  
make && make install && \  
cd / && \  
apk del build-deps && \  
rm -rf /var/cache/apk/* /opt/vowpal_wabbit/ && \  
apk \--no-cache add \--virtual run-deps boost-program_options zlib libstdc++

