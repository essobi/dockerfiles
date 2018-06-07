# Use alpine to build JS files, it's easy to get nodejs in Alpine.  
FROM alpine:latest as prebuild_env  
  
ENV FINGERPRINT
"sha256:32:12:90:9a:70:64:82:1c:5b:52:cc:c3:0a:d0:79:db:e1:a8:62:1b:9a:9a:4c:f4:72:40:1c:a7:3a:d3:0a:8c"  
ENV BUILDDEPS "mercurial git nodejs make"  
WORKDIR /root  
RUN apk add --update ${BUILDDEPS} \  
&& hg clone \--config hostsecurity.bitbucket.org:fingerprints=$FINGERPRINT
https://bitbucket.org/blais/beancount \  
&& (cd beancount && hg log -l1) \  
&& git clone https://github.com/beancount/fava.git \  
&& (cd fava && git log -1) \  
&& echo "Deleting symlink files as they will cause docker build error" \  
&& find ./ -type l -delete -print \  
&& make -C fava \  
&& make -C fava mostlyclean  
  
FROM python:3.6.5-stretch as build_env  
ENV BUILDDEPS "libxml2-dev libxslt-dev build-essential"  
ENV PV "3.6"  
WORKDIR /root  
RUN apt-get update && apt-get install ${BUILDDEPS} -y  
COPY \--from=prebuild_env /root/fava /root/fava  
COPY \--from=prebuild_env /root/beancount /root/beancount  
RUN python3 -mpip install ./beancount \  
&& python3 -mpip install ./fava \  
&& echo "strip .so files:" \  
&& find /usr/local/lib/python${PV}/site-packages -name *.so -print0|xargs -0
strip -v \  
&& echo "remove __pycache__ directories" \  
&& find /usr/local/lib/python${PV} -name __pycache__ -exec rm -rf -v {} + \  
&& find /usr/local/lib/python${PV} -name '*.dist-info' -exec rm -rf -v {} +  
  
FROM python:3.6.5-stretch  
ENV PV "3.6"  
ENV BEANCOUNT_INPUT_FILE ""  
ENV FAVA_OPTIONS "-H 0.0.0.0"  
COPY \--from=build_env /usr/local/lib/python${PV}/site-packages
/usr/local/lib/python${PV}/site-packages  
COPY \--from=build_env /usr/local/bin/fava /usr/local/bin  
  
# Default fava port number  
EXPOSE 5000  
CMD fava $FAVA_OPTIONS $BEANCOUNT_INPUT_FILE  

