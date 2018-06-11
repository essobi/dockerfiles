FROM python:alpine3.4  
MAINTAINER chesnut - https://imsweb.com  
  
ENV VERSION_WAPITI 3.0.0  
RUN buildDeps="libxml2-dev libxslt-dev python3-dev musl-dev gcc" && \  
runDeps="openssl py-xml libxml2 libxslt" && \  
apk --update add $runDeps $buildDeps && \  
pip install beautifulsoup4 requests && \  
mkdir /opt && cd /opt && \  
wget
"http://downloads.sourceforge.net/project/wapiti/wapiti/wapiti-$VERSION_WAPITI/wapiti-$VERSION_WAPITI.tar.gz"
&& \  
tar xvzf wapiti-$VERSION_WAPITI.tar.gz && \  
rm wapiti-$VERSION_WAPITI.tar.gz && \  
cd wapiti-$VERSION_WAPITI && \  
python setup.py install && \  
ln -sf /opt/wapiti-$VERSION_WAPITI /opt/wapiti && \  
chmod 755 /opt/wapiti/bin/wapiti && \  
mkdir /work && \  
apk del $buildDeps && \  
apk --update add $runDeps && \  
rm -f /var/cache/apk/* && \  
adduser -D -s /bin/sh user user && chown -R user /work  
  
USER user  
RUN chmod 775 /work  
  
ENV LANG en  
ENV PATH /opt/wapiti/bin:$PATH  
ENV HOME /work  
  
VOLUME /work  
WORKDIR /work  
  
ENTRYPOINT ["wapiti"]  
  
CMD ["--help"]

