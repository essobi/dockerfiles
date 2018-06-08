FROM gone/phusion:x86  
LABEL maintainer="Gone.io <hello@gone.io>"  
  
CMD ["/sbin/my_init"]  
  
## Install base packages  
ENV DEBIAN_FRONTEND noninteractive  
RUN echo "force-unsafe-io" > /etc/dpkg/dpkg.cfg.d/force-unsafe-io && \  
apt-get -qq update && \  
apt-get -yq install --no-install-recommends \  
inetutils-ping \  
host \  
curl \  
unzip \  
git \  
ca-certificates \  
tzdata \  
python-software-properties && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
echo Europe/London > /etc/timezone && \  
dpkg-reconfigure --frontend noninteractive tzdata  
  
RUN mkdir -p /app  
WORKDIR /app

