FROM ubuntu:14.04  
MAINTAINER Lukas Pessl <lukas.pessl@medunigraz.at>  
  
RUN useradd --system -U -u 500 plone \  
&& mkdir -p /plone /data/filestorage /data/blobstorage \  
&& chown -R plone:plone /plone /data  
  
ENV PLONE_MAJOR=4.3  
ENV PLONE_VERSION=4.3.9  
ENV RELEASE_VERSION="-r1"  
ENV PLONE_MD5="ac256fc1b388aea43ea799326d92ab23"  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && \  
apt-get install -q -y \  
apt-utils \  
wget \  
nano \  
sudo \  
supervisor \  
curl \  
git \  
build-essential \  
python-pip \  
python-dev \  
python-yaml \  
python-paramiko \  
python-six \  
python-httplib2 \  
python-jinja2 \  
&& apt-get autoremove \  
&& apt-get clean  
  
RUN apt-get update && \  
apt-get install -q -y \  
build-essential \  
gcc \  
python-setuptools \  
python-dev \  
git-core \  
libffi-dev \  
libpcre3 \  
libpcre3-dev \  
autoconf \  
libtool \  
pkg-config \  
zlib1g-dev \  
libssl-dev \  
libexpat1-dev \  
libxslt1.1 \  
libxml2-dev \  
libxslt1-dev \  
libbz2-dev \  
libjpeg62-dev \  
gnuplot \  
libcairo2 \  
libpango1.0-0 \  
libgdk-pixbuf2.0-0 \  
libxslt1.1 \  
libxml2 \  
libjpeg62  
  
RUN curl -o Plone.tgz -SL
https://launchpad.net/plone/$PLONE_MAJOR/$PLONE_VERSION/+download/Plone-$PLONE_VERSION$RELEASE_VERSION-
UnifiedInstaller.tgz  
RUN echo "$PLONE_MD5 Plone.tgz" | md5sum -c -  
RUN tar -xzf Plone.tgz  
RUN ./Plone-$PLONE_VERSION$RELEASE_VERSION-UnifiedInstaller/install.sh \  
\--password=admin \  
\--daemon-user=plone \  
\--owner=plone \  
\--group=plone \  
\--target=/plone \  
\--instance=instance \  
\--var=/data \  
none  
WORKDIR /plone/instance  
COPY buildout.cfg /plone/instance/buildout.cfg  
COPY sources.cfg /plone/instance/sources.cfg  
# && sed -i 's/parts =/parts =\n zeoserver/g' buildout.cfg \  
# && sed -i 's/eggs =/eggs =\n plone.jsonapi.core/g' buildout.cfg \  
# && sed -i 's/eggs =/eggs =\n bika.lims/g' buildout.cfg \  
# && echo '\n[zeoserver]\nrecipe = plone.recipe.zeoserver\nfile-storage =
/data/filestorage/Data.fs\nblob-storage = /data/blobstorage' >> buildout.cfg \  
RUN sudo -u plone bin/buildout  
RUN chown -R plone:plone /plone /data  
RUN rm -rf /Plone*  
RUN rm -rf /var/lib/apt/lists/*  
RUN rm -rf /plone/buildout-cache/downloads/*  
RUN find /plone \\( -type f -a -name '*.pyc' -o -name '*.pyo' \\) -exec rm -rf
'{}' +  
RUN apt-get autoremove  
RUN apt-get clean  
  
VOLUME /data/filestorage /data/blobstorage  
  
COPY docker-initialize.py docker-entrypoint.sh /  
  
RUN chmod a+x /docker-entrypoint.sh  
  
EXPOSE 8080  
USER plone  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["start"]  

