FROM python:3  
ARG BUILD_DATE  
ARG BUILD_PACKAGES="\  
curl \  
"  
ARG VCS_REF  
ARG VERSION=1.8  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/kc8apf/docker-fusesoc" \  
org.label-schema.version=$VERSION \  
org.label-schema.schema-version="1.0"  
  
RUN apt-get update && \  
apt-get install -y $BUILD_PACKAGES  
  
# Install gosu so the entrypoint can switch to a non-root account at runtime.  
RUN gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4  
RUN curl -o /usr/local/bin/gosu -SL
"https://github.com/tianon/gosu/releases/download/1.4/gosu-$(dpkg --print-
architecture)" \  
&& curl -o /usr/local/bin/gosu.asc -SL
"https://github.com/tianon/gosu/releases/download/1.4/gosu-$(dpkg --print-
architecture).asc" \  
&& gpg --verify /usr/local/bin/gosu.asc \  
&& rm /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu  
  
RUN apt-get remove --purge -y $BUILD_PACKAGES && \  
rm -rf /var/lib/apt/lists/*  
  
RUN pip install --no-cache-dir fusesoc==$VERSION  
  
ENV XDG_CONFIG_HOME /data  
ENV XDG_DATA_HOME /data  
COPY fusesoc.conf /data/fusesoc/  
VOLUME /data  
WORKDIR /data  
ENTRYPOINT ["fusesoc"]  

