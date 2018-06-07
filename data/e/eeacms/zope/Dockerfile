FROM eeacms/centos:7s  
MAINTAINER "Alin Voinea" <alin.voinea@eaudeweb.ro>  
  
ENV PYTHON=python \  
CONFIG=base.cfg \  
SETUPTOOLS=7.0 \  
ZCBUILDOUT=2.2.1 \  
ZOPE_HOME=/opt/zope  
  
RUN mkdir -p $ZOPE_HOME/var && \  
groupadd -g 500 zope-www && \  
useradd -g 500 -u 500 -m -s /bin/bash zope-www && \  
chown -R 500:500 $ZOPE_HOME  
  
COPY src/requires.sh /bin/update-dependencies  
COPY src/docker-entrypoint.sh \  
src/zope-setup.sh \  
src/configure.py \  
src/requires.py \  
src/last-built-cfg.py /  
  
COPY src/versions.cfg \  
src/sources.cfg \  
src/zope.cfg \  
src/base.cfg \  
src/bootstrap.py \  
src/install.sh $ZOPE_HOME/  
  
ONBUILD USER root  
ONBUILD COPY . /opt/app  
ONBUILD RUN install-dependencies /opt/app  
ONBUILD USER zope-www  
  
WORKDIR $ZOPE_HOME  
RUN ./install.sh  
  
USER zope-www  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["start"]  

