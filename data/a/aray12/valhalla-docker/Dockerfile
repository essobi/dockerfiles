FROM ubuntu:trusty  
MAINTAINER Andrew Ray (Andrew.ray@optum.com)  
  
RUN apt-get update && apt-get upgrade -y && \  
apt-get install -y git \  
libtool \  
automake \  
pkg-config \  
libcurl4-gnutls-dev \  
sudo \  
build-essential \  
libboost1.54-all-dev \  
software-properties-common \  
axel \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN git clone \--depth=1 \--recurse-submodules \--single-branch
\--branch=master https://github.com/valhalla/mjolnir.git && \  
cd mjolnir && \  
./scripts/dependencies.sh && \  
./scripts/install.sh && \  
cd .. && \  
git clone \--depth=1 \--recurse-submodules \--single-branch \--branch=master
https://github.com/valhalla/tools.git && \  
cd tools && \  
./scripts/dependencies.sh && \  
./scripts/install.sh && \  
cd .. && \  
git clone \  
\--depth=1 \  
\--recurse-submodules \  
\--single-branch \  
\--branch=master https://github.com/valhalla/conf.git && \  
ldconfig  
  
  
# image incomplete, needs data and tiles built before publish, below items to
be uncommented in builds derived from this base.  
#RUN axel -a -n 32 -N http://download.geofabrik.de/north-america-
latest.osm.pbf | awk -W interactive '$0~/\\[/{printf "%s'$'\r''", $0}'  
#RUN mkdir -p /data/valhalla  
#RUN valhalla_build_admins -c conf/valhalla.json *.pbf  
#RUN valhalla_build_tiles -c conf/valhalla.json *.pbf  
  
EXPOSE 8002  
CMD ["tools/valhalla_route_service", "conf/valhalla.json"]  
  

