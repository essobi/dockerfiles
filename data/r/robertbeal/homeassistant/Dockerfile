FROM alpine:3.7  
MAINTAINER Robert Beal <rob@kohi.uk>  
  
WORKDIR /tmp  
  
# bluez  
ENV BLUEZ_VERSION=5.43  
RUN apk add --update --no-cache --virtual=build-dependencies \  
alpine-sdk \  
dbus-dev \  
eudev-dev \  
glib-dev \  
libical-dev \  
linux-headers \  
readline-dev \  
wget \  
&& wget --no-check-certificate
https://www.kernel.org/pub/linux/bluetooth/bluez-${BLUEZ_VERSION}.tar.gz \  
&& tar -xzf bluez-${BLUEZ_VERSION}.tar.gz \  
&& cd bluez-${BLUEZ_VERSION} \  
&& ./configure --disable-systemd \  
&& make \  
&& cp attrib/gatttool /usr/local/bin \  
&& apk del --purge build-dependencies \  
&& rm -rf /tmp/*  
  
# homeassistant  
ENV HASS_VERSION=0.70.0  
RUN adduser -s /bin/false -D -h /app -u 4900 homeassistant \  
&& apk add --no-cache --virtual=build-dependencies \  
alpine-sdk \  
autoconf \  
eudev-dev \  
glib-dev \  
jpeg-dev \  
libffi-dev \  
libressl-dev=2.6.4-r2 \  
libxml2-dev \  
libxslt-dev \  
linux-headers \  
mariadb-dev \  
python3-dev \  
zlib-dev \  
&& apk add --no-cache \  
curl \  
glib \  
openssh-client \  
python3 \  
su-exec \  
&& python3 -m pip install --no-cache-dir \  
homeassistant==$HASS_VERSION \  
&& curl -L https://github.com/home-assistant/home-
assistant/archive/$HASS_VERSION.tar.gz | tar zx \  
&& LIBRARY_PATH=/lib:/usr/lib /bin/sh -c "python3 -m pip install -r /tmp/home-
assistant-$HASS_VERSION/requirements_all.txt" \  
&& apk del --purge build-dependencies \  
&& rm -rf /tmp/*  
  
WORKDIR /config  
VOLUME /config  
EXPOSE 8123  
HEALTHCHECK \--interval=30s --retries=3 CMD curl --fail
http://localhost:8123/api/ || exit 1  
  
COPY entrypoint.sh /usr/local/bin  
ENTRYPOINT ["entrypoint.sh"]  
CMD ["--skip-pip", "--config", "/config"]  

