FROM postgres:10.3-alpine  
  
MAINTAINER Ivan Kuznetsov <kuzma.wm@gmail.com>  
  
RUN apk add \--no-cache --virtual build-deps g++ make perl-dev tzdata openssh
git curl && \  
cp /usr/share/zoneinfo/UTC /etc/localtime && \  
echo UTC > /etc/timezone && \  
cd ~ && curl "https://bitbucket.org/eradman/pg-safeupdate/get/pg-
safeupdate-1.1.zip" \--output pg-safeupdate.zip && \  
unzip pg-safeupdate.zip && cd eradman-pg-safeupdate-3e34b479661d && make
install && \  
cd .. && rm -rf eradman-pg-safeupdate-3e34b479661d && rm pg-safeupdate.zip &&
\  
echo "shared_preload_libraries=safeupdate" >>
/usr/local/share/postgresql/postgresql.conf.sample && \  
apk del build-deps  

