# Apt-Cacher NG  
#  
# A caching proxy. Specialized for package files from Linux distributors.  
FROM winggundamth/ubuntu-base:xenial  
MAINTAINER Jirayut Nimsaeng <w [at] winginfotech.net>  
ENV FROM_BASE=xenial-20160809  
# 1) Install apt-cacher-ng  
# 2) Clean to reduce Docker Image size  
ARG APT_CACHER_NG  
RUN [ -n "$APT_CACHER_NG" ] && \  
echo "Acquire::http::Proxy \"$APT_CACHER_NG\";" \  
> /etc/apt/apt.conf.d/11proxy || true; \  
apt-get update && \  
apt-get install -y apt-cacher-ng && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /etc/apt/apt.conf.d/11proxy  
  
CMD ["/usr/sbin/apt-cacher-ng", "-c", "/etc/apt-cacher-ng/", "ForeGround=1"]  
EXPOSE 3142  
# 1) Configure apt-cacher-ng to make sure it won't proxy https  
# 2) Link stdout and stderr to apt-cacher-ng log files  
RUN echo "PassThroughPattern: .*:443$" >> /etc/apt-cacher-ng/acng.conf && \  
ln -sf /dev/stdout /var/log/apt-cacher-ng/apt-cacher.log && \  
ln -sf /dev/stderr /var/log/apt-cacher-ng/apt-cacher.err  
  
VOLUME ["/var/log", "/var/cache/apt-cacher-ng"]  

