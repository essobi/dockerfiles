FROM tianon/debian-devel  
  
# since we're uploading to experimental, let's build with deps from it too  
RUN echo 'APT::Default-Release "experimental";' > /etc/apt/apt.conf.d/default  
  
# start by adding just "debian/control" so we can get mk-build-deps with
maximum caching  
COPY control /usr/src/docker.io/debian/  
WORKDIR /usr/src/docker.io  
  
# get all the build deps of _this_ package in a nice repeatable way  
RUN apt-get update && mk-build-deps -irt'apt-get --no-install-recommends -yV'
debian/control && dpkg-checkbuilddeps  
  
# need our debian/ directory to compile _this_ package  
COPY . /usr/src/docker.io/debian  
  
# go download and unpack our upstream source  
RUN uscan --force-download --verbose --download-current-version  
RUN DOCKER_TARBALLS=.. ./debian/helpers/download-libcontainer  
RUN /tianon/extract-origtargz.sh  
  
RUN dpkg-buildpackage -us -uc && lintian -EvIL+pedantic  

