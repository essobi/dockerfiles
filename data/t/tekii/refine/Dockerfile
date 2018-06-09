#  
# REFINE Dockerfile  
#  
#  
FROM tekii/server-jre  
  
MAINTAINER Pablo Jorge Eduardo Rodriguez <pr@tekii.com.ar>  
  
LABEL version=2.6-rc.2  
  
COPY config.patch /opt/refine/  
  
RUN apt-get \--quiet=2 update && \  
apt-get \--quiet=2 install \--assume-yes \--no-install-recommends wget patch
&& \  
echo "start downloading and decompressing
https://github.com/OpenRefine/OpenRefine/releases/download/2.6-rc.2/openrefine-
linux-2.6-rc.2.tar.gz" && \  
wget -q -O -
https://github.com/OpenRefine/OpenRefine/releases/download/2.6-rc.2/openrefine-
linux-2.6-rc.2.tar.gz | tar -xz \--strip=1 -C /opt/refine && \  
echo "end downloading and decompressing." && \  
cd /opt/refine && patch \--strip=1 \--input=config.patch && cd \- && \  
apt-get purge \--assume-yes patch && \  
apt-get \--quiet=2 autoremove \--assume-yes && \  
apt-get \--quiet=2 clean && \  
apt-get \--quiet=2 autoclean && \  
rm -rf /var/lib/{apt,dpkg,cache,log}/ && \  
chown \--recursive root:root /opt/refine  
  
ENV REFINE_HOME=/var/refine \  
REFINE_VERSION=2.6-rc.2 \  
REFINE_PORT=3333 \  
REFINE_HOST=0.0.0.0 \  
REFINE_MEMORY=2400M \  
JAVA_OPTIONS=-Drefine.headless=true\ -Drefine.data_dir=/var/refine  
# you must 'chown __USER__.__GROUP__ .' this directory in the host in  
# order to allow the jira user to write in it.  
VOLUME /var/refine  
  
EXPOSE 3333  
  
USER daemon:daemon  
  
ENTRYPOINT ["/opt/refine/refine", ""]  

