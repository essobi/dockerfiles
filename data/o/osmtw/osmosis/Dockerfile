FROM osmtw/ubuntu  
  
MAINTAINER Rex Tsai "https://about.me/chihchun"  
ENV OSMOSIS_VERSION=0.45  
ENV MAPSFORGE_VERSION=0.6.1  
ENV DEBIAN_FRONTEND=noninteractive  
RUN apt-get install -y --no-install-recommends wget  
  
# Install prebuilt Osmosis  
RUN wget http://bretth.dev.openstreetmap.org/osmosis-
build/osmosis-${OSMOSIS_VERSION}.tgz  
RUN mkdir -p /usr/local/osmosis \  
&& tar zxvf osmosis-${OSMOSIS_VERSION}.tgz -C /usr/local/osmosis  
# Install Osmosis Mapsforge Map Writer  
RUN wget
http://ci.mapsforge.org/job/$MAPSFORGE_VERSION/lastSuccessfulBuild/artifact/mapsforge-
map-writer/build/libs/mapsforge-map-writer-$MAPSFORGE_VERSION.jar \  
&& mv mapsforge-map-writer-$MAPSFORGE_VERSION.jar /usr/local/osmosis  
  
# https://github.com/mapsforge/mapsforge/issues/303  
RUN echo "load /usr/share/java/xalan2.jar" >>
/usr/local/osmosis/config/plexus.conf \  
&& echo "JAVACMD_OPTIONS=-Xmx2G" > /root/.osmosis  
  
RUN ln -s /usr/local/osmosis/bin/* /usr/bin  
RUN apt-get install -y --no-install-recommends default-jre-headless \  
libbatik-java \  
libcommons-codec-java \  
libcommons-compress-java \  
libcommons-dbcp-java \  
libcommons-pool-java \  
libjpf-java \  
libmysql-java \  
libnetty-3.9-java \  
libpostgis-java \  
libpostgresql-jdbc-java \  
libspring-beans-java \  
libspring-context-java \  
libspring-core-java \  
libspring-jdbc-java \  
libspring-transaction-java \  
libosmpbf-java \  
libplexus-classworlds-java \  
libprotobuf-java \  
libxerces2-java \  
libxz-java  
  
  
RUN apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
WORKDIR /data  

