FROM openjdk:8-jdk  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Enable UTF-8 by default  
RUN apt-get update && apt-get install -y locales && rm -rf
/var/lib/apt/lists/* \  
&& localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias
en_US.UTF-8  
ENV LANG en_US.utf8  
  
# Build default yamcs installation to /src/yamcs  
# Extending containers wishing to do so can just choose  
# to ignore this, and instead mount a local volume to  
# this same path.  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends maven \  
&& mkdir /src \  
&& env GIT_SSL_NO_VERIFY=true git clone --depth 1 \--branch yamcs-3.1.0
https://github.com/yamcs/yamcs.git /src/yamcs \  
&& cd /src/yamcs \  
&& mvn package -DskipTests \  
&& rm -rf .git \  
&& rm -rf ~/.m2 \  
&& apt-get purge -y --auto-remove maven \  
&& rm -rf /var/lib/apt/lists/*  
# Build web dashboard, we should have this maybe in git  
# or on npm, but alas  
RUN curl -sL https://deb.nodesource.com/setup_4.x | bash - \  
&& apt-get install -y --no-install-recommends nodejs \  
&& npm install -g bower gulp \  
&& cd /src/yamcs/yamcs-web \  
&& bower install --allow-root --config-interactive=false \  
&& npm install \  
&& gulp \  
&& npm uninstall -g bower gulp \  
&& rm -rf bower_components \  
&& rm -rf node_modules \  
&& apt-get purge -y --auto-remove nodejs \  
&& rm -rf /var/lib/apt/lists/*  
# Install default-built JARs under /opt/yamcs  
# Same as RPM deploy path  
RUN mkdir -p /opt/yamcs/etc \  
&& mkdir -p /opt/yamcs/bin \  
&& mkdir -p /opt/yamcs/lib/ext \  
&& mkdir -p /opt/yamcs/log \  
&& mkdir -p /opt/yamcs/mdb \  
&& mkdir -p /opt/yamcs/web \  
&& cp /src/yamcs/yamcs-core/bin/* /opt/yamcs/bin \  
&& ln -s /src/yamcs/yamcs-core/target/*.jar /opt/yamcs/lib \  
&& ln -s /src/yamcs/yamcs-core/lib/*.jar /opt/yamcs/lib \  
&& ln -s /src/yamcs/yamcs-web/build /opt/yamcs/web/base  
  
# Location where extending images can put random .sh  
# To run at every container start (typical use is to  
# install plugin jars, or configuration files)  
RUN mkdir /entrypoint.d  
  
ENV PATH /opt/yamcs/bin:$PATH  
  
ENV YAMCS_DATA /storage/yamcs-data  
ENV YAMCS_INCOMING /storage/yamcs-incoming  
VOLUME /storage/yamcs-data /storage/yamcs-incoming  
  
COPY entrypoint.sh /  
ENTRYPOINT ["/entrypoint.sh"]  
  
EXPOSE 5445 8090  
CMD ["yamcs"]  

