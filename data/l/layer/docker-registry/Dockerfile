FROM phusion/baseimage:0.9.11  
  
RUN \  
printf 'APT::Get::Assume-Yes "true";\nAPT::Install-Recommends "false";\n' >
/etc/apt/apt.conf.d/99-defaults && \  
echo "deb http://nginx.org/packages/ubuntu/ trusty nginx" >
/etc/apt/sources.list.d/nginx.list && \  
curl --silent -L http://nginx.org/keys/nginx_signing.key | apt-key add \- && \  
apt-get update && \  
apt-get install libssl-dev>=1.0.1f openssl>=1.0.1f nginx=1.6.2-1~trusty && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /var/cache/*  
  
# Order matters: after nginx install, before docker-registry install.  
ADD image-files /  
  
RUN \  
apt-get update && \  
apt-get install git && \  
apt-get install build-essential libevent-dev libssl-dev liblzma-dev libffi-dev
python-dev python-pip && \  
git clone https://github.com/dotcloud/docker-registry.git /tmp/docker-registry
&& \  
mv /tmp/docker-registry/.git /opt/docker-registry/.git && \  
cd /opt/docker-registry && git checkout tags/0.7.2 && git reset --hard HEAD &&
\  
pip install /opt/docker-registry && \  
pip install --upgrade /opt/docker-registry && \  
pip install git+git://github.com/dmp42/docker-registry-driver-gcs#egg=docker-
registry-driver-gcs && \  
apt-get install redis-server && \  
rm /etc/my_init.d/00_regen_ssh_host_keys.sh && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /var/cache/* && \  
mkdir /var/cache/nginx  
  
CMD ["/sbin/my_init"]  

