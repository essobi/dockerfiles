FROM rawmind/alpine-monit:0.5.20-2 as builder  
ENV QUERYSTRING_VERSION=1.0.4  
  
COPY vmod-querystring-${QUERYSTRING_VERSION}.tar.gz /tmp/vmod-
querystring-${QUERYSTRING_VERSION}.tar.gz  
RUN apk add \--no-cache varnish varnish-dev openrc alpine-sdk autoconf
automake \  
libtool python py-docutils  
  
RUN mkdir -p /usr/src \  
&& cd /usr/src \  
&& tar -xzf /tmp/vmod-querystring-${QUERYSTRING_VERSION}.tar.gz \  
&& ls \  
&& cd vmod-querystring-${QUERYSTRING_VERSION} \  
&& ./configure \--prefix=/usr \  
&& make \  
&& make check \  
&& make install  
  
FROM rawmind/alpine-monit:0.5.20-2  
  
# Set environment  
ENV SERVICE_NAME=varnish \  
SERVICE_HOME=/opt/varnish \  
SERVICE_VERSION=v1.1.1 \  
SERVICE_USER=varnish \  
SERVICE_UID=100 \  
SERVICE_GROUP=varnish \  
SERVICE_GID=101  
ENV
PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/opt/monit/bin:/opt/varnish/bin/"  
RUN apk add \--no-cache varnish openrc  
  
# Download and install varnish  
COPY root /  
RUN mkdir -p "$SERVICE_HOME/run" && chown -R ${SERVICE_USER}:${SERVICE_GROUP}
"$SERVICE_HOME" /opt/monit  
COPY varnishd /etc/conf.d/  
COPY \--from=builder /lib/varnish/vmods /usr/lib/varnish/vmods  
  
WORKDIR $SERVICE_HOME  
USER $SERVICE_USER  

