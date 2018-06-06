# Extend minimal jeanblanchard/java:jre-8  
FROM darekxan/alpinelinux-jre8-libxml2-dev-libstdc:latest  
  
########### TODO: remove asap - reverted version of glibc  
  
ENV GLIBC_VERSION 2.22-r8  
  
# Download and install specific glibc; effectively downgrade  
RUN apk add --update curl && \  
curl -o glibc.apk -L "https://github.com/andyshinn/alpine-pkg-
glibc/releases/download/${GLIBC_VERSION}/glibc-${GLIBC_VERSION}.apk" && \  
apk add --allow-untrusted glibc.apk && \  
curl -o glibc-bin.apk -L "https://github.com/andyshinn/alpine-pkg-
glibc/releases/download/${GLIBC_VERSION}/glibc-bin-${GLIBC_VERSION}.apk" && \  
apk add --allow-untrusted glibc-bin.apk && \  
/usr/glibc-compat/sbin/ldconfig /lib /usr/glibc/usr/lib && \  
echo 'hosts: files mdns4_minimal [NOTFOUND=return] dns mdns4' >>
/etc/nsswitch.conf && \  
apk del curl && \  
rm -f glibc.apk glibc-bin.apk && \  
rm -rf /var/cache/apk/*  
  
###########  
# py-scipy is in testing repo, py-numpy in community  
RUN echo http://dl-cdn.alpinelinux.org/alpine/edge/testing >>
/etc/apk/repositories &&\  
echo http://dl-cdn.alpinelinux.org/alpine/edge/community >>
/etc/apk/repositories &&\  
# refresh apk index  
apk update &&\  
# install scipy and as dependencies: python and numpy  
apk add py-scipy &&\  
# scikit-learn compilation depenndencies: g++, openblas-dev, py-numpy-dev  
apk add g++ &&\  
apk add openblas-dev &&\  
apk add py-numpy-dev &&\  
# add python dependency manager  
apk add py-pip &&\  
# update pip  
pip install --upgrade pip &&\  
# install scikit-learn from sources scikit-learn  
pip install --upgrade scikit-learn &&\  
# install rethinkdb  
pip install --upgrade rethinkdb &&\  
# all done - cleanup phase  
# remove scikit-learn compilation requirements  
apk del openblas-dev &&\  
apk del py-numpy-dev &&\  
apk del g++ &&\  
# clean package manager cache  
rm -rf /var/cache/apk/* &&\  
# clean pip cache  
rm -rf ~/.cache/pip/*  

