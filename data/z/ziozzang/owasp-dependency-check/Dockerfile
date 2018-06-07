FROM openjdk:8-jre-slim  
  
MAINTAINER Jioh L. Jung <ziozzang@gmail.com>  
#Original code is maintained by Timo Pagel <dependencycheckmaintainer@timo-
pagel.de>  
ENV DEBIAN_FRONTEND=noninteractive  
  
ENV version_url=https://jeremylong.github.io/DependencyCheck/current.txt  
ENV download_url=https://dl.bintray.com/jeremy-long/owasp  
  
RUN apt-get update && apt-get upgrade -fy && \  
apt-get install -y --no-install-recommends wget ruby mono-runtime && \  
gem install bundle-audit && \  
gem cleanup  
  
RUN wget -O /tmp/current.txt ${version_url} && \  
version=$(cat /tmp/current.txt) && \  
file="dependency-check-${version}-release.zip" && \  
wget "$download_url/$file" && \  
unzip ${file} && \  
rm ${file} && \  
mv dependency-check /usr/share/ && \  
mkdir /report && \  
apt-get remove --purge -y wget && \  
apt-get autoremove -y && \  
rm -rf /var/lib/apt/lists/* /tmp/*  
  
VOLUME ["/src" "/usr/share/dependency-check/data" "/report"]  
  
WORKDIR /src  
  
CMD ["--help"]  
ENTRYPOINT ["/usr/share/dependency-check/bin/dependency-check.sh"]  

