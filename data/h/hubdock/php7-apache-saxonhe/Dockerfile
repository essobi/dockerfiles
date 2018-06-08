FROM php:7-apache  
  
ARG DEBIAN_FRONTEND=noninteractive  
  
# edit this to use a different version of Saxon  
ARG saxon='libsaxon-HEC-setup64-v1.1.0'  
  
ARG jdk='openjdk-8-jdk-headless'  
  
ARG jvm='/usr/lib/jvm/java-8-openjdk-amd64'  
# needed for default-jre-headless  
RUN mkdir -p /usr/share/man/man1  
  
RUN apt-get update \  
## dependencies  
&& apt-get install -y --no-install-recommends ${jdk} unzip wget \  
## fetch and install  
&& wget https://www.saxonica.com/saxon-c/${saxon}.zip \  
&& unzip ${saxon}.zip -d saxon \  
&& saxon/${saxon} -batch -dest /opt/saxon \  
&& rm ${saxon}.zip \  
&& rm -r saxon \  
## prepare  
&& ln -s /opt/saxon/libsaxonhec64.so /usr/lib/ \  
&& ln -s /opt/saxon/rt /usr/lib/ \  
&& ln -s ${jvm}/include/linux/jni_md.h ${jvm}/include/ \  
## build  
&& cd /opt/saxon/Saxon.C.API \  
&& phpize \  
&& ./configure --enable-saxon CPPFLAGS="-I${jvm}/include" \  
&& make \  
&& make install \  
&& echo 'extension=saxon.so' > /usr/local/etc/php/conf.d/saxon.ini \  
&& rm -r /opt/saxon/Saxon.C.API \  
## clean  
&& apt-get clean \  
&& apt-get remove -y ${jdk} unzip wget \  
&& apt-get autoremove -y \  
&& rm -rf /var/lib/apt/lists/  

