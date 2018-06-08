FROM alpine  
MAINTAINER Naoki OKAMURA <nyarla@thotep.net>  
  
RUN apk update \  
&& apk upgrade \  
&& apk add -U \  
bash \  
ca-certificates \  
cyrus-sasl-dev \  
libffi-dev \  
libxml2-dev \  
libxslt-dev \  
yaml-dev \  
openldap-dev \  
openssl-dev \  
python \  
python-dev \  
py-pip \  
zlib-dev \  
&& grep ^P /lib/apk/db/installed | sed -e 's/^P://g' | sort > /tmp/before \  
&& apk add -U \  
build-base \  
&& pip install realms-wiki whoosh \  
&& grep ^P /lib/apk/db/installed | sed -e 's/^P://g' | sort > /tmp/after \  
&& diff /tmp/before /tmp/after | grep -e "^+[^+]" | sed -e 's#+##g' | xargs
-n1 apk del \  
&& rm /tmp/before /tmp/after \  
&& rm -rf /var/cache/apk/*  
  
RUN mkdir -p /opt/app \  
&& mkdir -p /opt/data  
  
COPY run /opt/app/run  
  
RUN chmod +x /opt/app/run  
  
WORKDIR /opt/data  
  
EXPOSE 8080  
ENTRYPOINT [ "/opt/app/run" ]  
CMD [ "start" ]  

