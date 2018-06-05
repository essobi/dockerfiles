FROM ubuntu:16.04  
ARG DEBIAN_FRONTEND=noninteractive  
  
RUN set -xe && \  
buildDependencies=curl && \  
apt-get update && \  
apt-get upgrade -y && \  
apt-get install --no-install-recommends -y $buildDependencies locales ca-
certificates && \  
TINI_LATEST_RELEASE=$(curl -L -s -H 'Accept: application/json'
https://github.com/krallin/tini/releases/latest) && \  
TINI_LATEST_VERSION=$(echo $TINI_LATEST_RELEASE | sed -e
's/.*"tag_name":"v\\([^"]*\\)".*/\1/') && \  
curl -L
"https://github.com/krallin/tini/releases/download/v${TINI_LATEST_VERSION}/tini_${TINI_LATEST_VERSION}.deb"
> tini.deb && \  
dpkg -i tini.deb && \  
rm tini.deb && \  
apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false
$buildDependencies && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \  
sed -i -e 's/# de_DE.UTF-8 UTF-8/de_DE.UTF-8 UTF-8/' /etc/locale.gen && \  
echo 'LANG="en_US.UTF-8"'>/etc/default/locale && \  
dpkg-reconfigure --frontend=noninteractive locales && \  
update-locale LANG=en_US.UTF-8 && \  
localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8  
  
ENV LANG=en_US.UTF-8  
ENTRYPOINT ["tini", "--"]  

