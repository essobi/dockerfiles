FROM ubuntu:16.04  
MAINTAINER Stanislav Vitkovskiy <stas.vitkovsky@gmail.com>  
  
# Don't consider sources and choose the fastest mirrors  
RUN sed -i 's|^deb-src |# deb-src |' /etc/apt/sources.list && \  
sed -i 's|^deb \S\\+ |deb mirror://mirrors.ubuntu.com/mirrors.txt |'
/etc/apt/sources.list  
  
# Install Exim4  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends
awscli pbzip2 mysql-client-5.7 && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
mkdir ~/.aws && chmod 0600 ~/.aws  
  
COPY entrypoint /bin/entrypoint  
  
ENTRYPOINT ["/bin/entrypoint"]  

