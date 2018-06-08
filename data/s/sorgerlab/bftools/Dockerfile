FROM alpine:3.5  
RUN apk -Uuv add bash openjdk8-jre \  
&& mkdir /opt \  
&& wget http://downloads.openmicroscopy.org/latest/bio-
formats5.6/artifacts/bftools.zip \  
&& unzip bftools.zip -x '*.bat' -d /opt/ \  
&& rm /var/cache/apk/*  
  
ENV PATH $PATH:/opt/bftools/  
  
WORKDIR /tmp  

