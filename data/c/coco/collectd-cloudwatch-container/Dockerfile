FROM alpine:3.5  
MAINTAINER 'Jussi Heinonen<jussi.heinonen@ft.com>'  
ADD etc/collectd.d /etc/collectd.d/  
ADD opt/collectd-plugins /opt/collectd-plugins/  
  
# Install dependencies  
RUN apk add -U linux-headers bash bash-doc bash-completion curl git \  
python python-dev py-pip py-cffi py-openssl openssl-dev \  
build-base gcc abuild binutils binutils-doc gcc-doc &&\  
pip install --upgrade pip awscli boto3 requests pyyaml &&\  
git clone https://github.com/Financial-Times/collective.git  
  
# reference: https://github.com/rightscale/collectd-
container/blob/master/Dockerfile  
# Compile collectd from source in order to change the location of /proc to
/host/proc,  
# this assumes the container is launched with -v /proc:/host/proc  
RUN curl https://collectd.org/files/collectd-5.7.1.tar.bz2 | tar xjf - &&\  
cd collectd* &&\  
./configure --prefix=/usr --sysconfdir=/etc/collectd --localstatedir=/var
--enable-debug --enable-python &&\  
grep -rl /proc/ . | xargs sed -i "s/\/proc\//\/host\/proc\//g" &&\  
make all install &&\  
make clean &&\  
echo 'Include "/etc/collectd.d"' > /etc/collectd/collectd.conf  
  
ADD alarms.yml /  
ADD run.sh /  
  
# Clean  
#RUN rm -rf /var/cache/apk/*  
CMD /bin/bash /run.sh  

