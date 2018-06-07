FROM ubuntu:trusty  
  
MAINTAINER steranin  
  
ENV HERITRIX_VERSION 3.2.0  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && \  
apt-get install -y openjdk-7-jre-headless curl  
  
RUN curl
http://builds.archive.org/maven2/org/archive/heritrix/heritrix/${HERITRIX_VERSION}/heritrix-${HERITRIX_VERSION}-dist.tar.gz
-s -o /tmp/heritrix-${HERITRIX_VERSION}-dist.tar.gz  
  
RUN mkdir /opt/heritrix && tar xvfz
/tmp/heritrix-${HERITRIX_VERSION}-dist.tar.gz -C /opt/heritrix --strip-
components=1  
  
RUN useradd -U -s /bin/false heritrix && \  
chown -R heritrix:heritrix /opt/heritrix  
  
RUN mkdir /mnt/heritrix-ext  
VOLUME /mnt/heritrix-ext  
  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
USER heritrix  
  
EXPOSE 8443  
ENV FOREGROUND false  
ENTRYPOINT ["/opt/heritrix/bin/heritrix", "--web-bind-hosts 0.0.0.0", "--jobs-
dir /mnt/heritrix-ext/jobs"]  
CMD ["--web-admin heritrix:heritrix"]  

