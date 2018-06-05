# shoifele/bone  
  
FROM debian:jessie  
  
MAINTAINER Sebastian Sauer <info@dynpages.de>  
MAINTAINER Christoph Wiechert <wio@psitrax.de>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV HOME /root  
ENV REFRESHED_AT="2016-03-16"  
  
ADD rootfs /  
  
# Add dotdeb Repo to get newer packages  
RUN echo "deb http://packages.dotdeb.org jessie all" >
/etc/apt/sources.list.d/dotdeb.list && \  
echo "deb-src http://packages.dotdeb.org jessie all" >>
/etc/apt/sources.list.d/dotdeb.list && \  
apt-key add /root/dotdeb.gpg && rm /root/dotdeb.gpg  
  
# Install common tools  
RUN apt-get update \  
&& apt-get upgrade -y \  
&& apt-get install -y --no-install-recommends \  
openssh-client \  
git \  
debconf-utils \  
apt-utils \  
dialog \  
less \  
curl \  
wget \  
vim \  
net-tools \  
locales \  
sendmail \  
gettext-base \  
netcat \  
openssl \  
ca-certificates \  
bzip2 \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /build  
  
CMD ["/init"]  

