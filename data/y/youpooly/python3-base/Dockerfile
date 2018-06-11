FROM frolvlad/alpine-python3:latest  
  
MAINTAINER Christopher Lege <christopher.lege@youpooly.com>  
  
  
RUN apk update && apk add gcc musl-dev linux-headers python3-dev make libffi-
dev openssl-dev g++ ca-certificates libtool m4 libuv-dev automake autoconf \  
&& pip3 install --upgrade pip \  
&& pip3 install nose \  
&& pip3 install certifi==14.5.14 cloudinary==1.1.1 coverage==3.7.1
easydict==1.6 elasticsearch==2.2.0 enum34==1.1.2 jmespath==0.4.1
libnacl==1.4.3 motorengine==0.9.0 onesky-python==1.0.2 polib==1.0.6
psutil==2.2.1 pyasn1==0.1.7 pycares==0.6.1 pycparser==2.10 pymacaroons==0.8.0
pyOpenSSL==0.14 pyprofiler==22 python-dateutil==2.2 python-etcd==0.3.2 python-
json-logger==0.1.1 python-logstash==0.4.5 pytz==2015.2 redis==2.10.5
PyYAML==3.11 boto pyzmq==14.5.0 requests sendgrid validate_email==1.3
six==1.9.0 smtpapi==0.2.0 termcolor==1.1.0 tornado uvloop tornaduv ujson==1.33
icalendar awesome-slugify \  
&& apk del gcc musl-dev linux-headers python3-dev make libffi-dev openssl-dev
g++ python3-tests python3-doc openssl-dev openssl-doc make linux-headers
libffi-dev g++ libc-dev musl-dev libc6-compat musl-dbg gcc mpc1 mpfr3 gmp
pkgconfig libstdc++ libgcc  

