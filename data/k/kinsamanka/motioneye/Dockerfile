FROM alpine:3.6  
MAINTAINER GP Orcullo  
  
RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories \  
&& apk add --no-cache curl-dev gcc jpeg-dev musl-dev openssl-dev \  
python-dev py-pip zlib-dev bash curl libcrypto1.0 libssl1.0 motion \  
python py-setuptools v4l-utils \  
&& pip install --upgrade pip motioneye \  
&& apk --purge -v del curl-dev gcc jpeg-dev musl-dev openssl-dev \  
python-dev py-pip \  
&& mkdir /etc/motioneye/ /var/lib/motioneye \  
&& cp /usr/share/motioneye/extra/motioneye.conf.sample
/etc/motioneye/motioneye.conf \  
&& chown -R motion:motion /etc/motioneye /var/lib/motioneye /var/log \  
&& chmod a+rw /run /var/run \  
&& mkdir -p /data /data.org/conf \  
&& chmod 0777 -R /data.org \  
&& mv /etc/motioneye /data.org/conf \  
&& mv /var/lib/motioneye /data.org \  
&& mv /var/log /data.org \  
&& ln -sf /data/conf/motioneye /etc/motioneye \  
&& ln -sf /data/motioneye /var/lib/motioneye \  
&& ln -sf /data/log /var/log \  
&& mkdir /data/conf \  
&& ln -sf /data.org/conf/motioneye /data/conf/motioneye \  
&& ln -sf /data.org/motioneye /data/motioneye \  
&& ln -sf /data.org/log /data/log \  
&& touch /data/.ok \  
&& chown -R operator:motion /data  
  
VOLUME /data  
  
CMD test ! -f /data/.ok && \  
(cp -a /data.org/* /data; touch /data/.ok); \  
su operator -c "/usr/bin/meyectl startserver -c /etc/motioneye/motioneye.conf"  
  
EXPOSE 8765  
  

