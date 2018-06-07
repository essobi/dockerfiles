FROM studioetrange/docker-debian:wheezy  
MAINTAINER StudioEtrange <nomorgan@gmail.com>  
  
# DEBIAN packages : HUE dependencies install ----------  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \  
ant \  
gcc \  
g++ \  
build-essential \  
libkrb5-dev \  
libmysqlclient-dev \  
libssl-dev \  
libsasl2-dev \  
libsasl2-modules-gssapi-mit \  
libsqlite3-dev \  
libtidy-0.99-0 \  
libxml2-dev \  
libxslt-dev \  
maven \  
libldap2-dev \  
python-dev \  
python-simplejson \  
python-setuptools \  
openjdk-7-jdk \  
&& rm -rf /var/lib/apt/lists/*  
  
# HUE install -------------  
#ENV HUE_VERSION cdh5.3.0-release  
ENV HUE_VERSION release-3.7.1  
WORKDIR /opt/hue  
  
RUN curl -k -SL "https://github.com/cloudera/hue/archive/$HUE_VERSION.tar.gz"
\  
| tar -xzf - -C /opt/hue --strip-components=1  
  
# SUPERVISOR -------------  
COPY supervisord-hue.conf /etc/supervisor/conf.d/supervisord-hue.conf  
  
# BUILD  
RUN make apps && rm -Rf /root/.m2  
  
RUN useradd hue -r && chown hue:hue /opt/hue/desktop && chown hue:hue
/opt/hue/desktop/desktop.db  
  
# DOCKER -------------  
#VOLUME /opt/hue/desktop/conf /opt/hue/desktop/desktop.db desktop/app ?  
# Supervisord web interface -------  
EXPOSE 9999  
# hue http port  
EXPOSE 8000  
# run command by default  
CMD ["supervisord", "-c", "/etc/supervisor/supervisord.conf", "-n"]  

