FROM verdel/alpine-base:latest  
MAINTAINER Vadim Aleksandrov <valeksandrov@me.com>  
  
ENV JAVA_HOME /usr  
  
COPY rootfs /  
  
RUN apk --no-cache --update add \  
bash \  
openjdk8-jre \  
py-pip \  
&& pip install --upgrade pip \  
&& pip install requests \  
# Clean up  
&& rm -rf \  
/tmp/* \  
/var/cache/apk/*  
  
RUN /opt/install/install_graylog.py  
  
RUN cd /opt/ \  
&& tar xfz graylog-*.tgz \  
&& mv graylog-*/ graylog/ \  
&& rm graylog-*.tgz \  
&& rm -rf /opt/install  
  
# gelf tcp/udp  
EXPOSE 12201  
EXPOSE 12201/udp  
  
# rest api  
EXPOSE 12900  
# syslog  
EXPOSE 514  
EXPOSE 514/udp  

