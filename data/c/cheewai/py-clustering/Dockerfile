FROM ubuntu:trusty  
LABEL maintainer "Cheewai Lai <clai@csir.co.za>"  
  
ARG GOSU_VERSION=1.10  
ARG
GOSU_DOWNLOAD_URL="https://github.com/tianon/gosu/releases/download/${GOSU_VERSION}/gosu-
amd64"  
ARG S6_OVERLAY_VERSION=v1.17.2.0  
ARG DEBIAN_FRONTEND=noninteractive  
ARG DOCKERIZE_VERSION=v0.5.0  
# For sklearn.cluster: python-numpy libatlas-dev libatlas3gf-base  
# For scipy: liblapack3gf liblapack-dev gfortran  
# For Python script to interact with Postgis database: python-psycopg2
libgeos-3.4.2 libgeos-dev  
# For geolookup: python-simplejson  
RUN sed 's/main$/main universe multiverse/' -i /etc/apt/sources.list \  
&& set -x \  
&& apt-get update \  
&& apt-get -y upgrade \  
&& apt-get install -y curl software-properties-common wget unzip build-
essential git python python-dev python-setuptools \  
&& curl -o gosu -kfsSL "$GOSU_DOWNLOAD_URL" \  
&& mv gosu /usr/bin/gosu \  
&& chmod +x /usr/bin/gosu \  
&& curl -k -fsSL https://github.com/just-
containers/s6-overlay/releases/download/${S6_OVERLAY_VERSION}/s6-overlay-
amd64.tar.gz | tar xfz - -C / \  
&& curl -k -fsSL
https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-
linux-amd64-$DOCKERIZE_VERSION.tar.gz | tar xfz - -C /usr/bin \  
&& easy_install pip \  
&& pip install --upgrade pip \  
&& apt-get install -y libatlas-dev libatlas3gf-base liblapack3gf liblapack-dev
gfortran python-psycopg2 libgeos-3.4.2 libgeos-dev \  
&& ldconfig \  
&& pip install numpy \  
&& pip install scipy>=0.12.0 \  
&& pip install scikit-learn>=0.14.0 \  
&& pip install Shapely \  
&& pip install geopy>=1.10.0 \  
&& pip install pika \  
&& pip install kombu \  
&& pip install librabbitmq \  
&& pip install python-daemon \  
&& pip install pyproj \  
&& pip install pytest \  
&& pip install reverse_geocoder \  
&& pip install python-logstash \  
&& pip install subprocess32 \  
&& pip install rethinkdb \  
&& pip install dateutils \  
&& pip install blinker raven --upgrade \  
&& pip install redis rq \  
&& apt-get -y install python-yaml python-gdal libgdal1h gdal-bin
libspatialindex-dev \  
&& pip install rtree \  
&& apt-get -y remove --purge software-properties-common build-essential git
python-dev \  
&& apt-get -y autoremove \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
ADD docker-entrypoint.sh /docker-entrypoint.sh  
ENTRYPOINT ["/docker-entrypoint.sh"]  

