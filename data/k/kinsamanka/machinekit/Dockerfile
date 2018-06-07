FROM debian  
MAINTAINER GP Orcullo <kinsamanka@gmail.com>  
  
# install required dependencies  
RUN apt-key adv --keyserver hkp://keys.gnupg.net --recv-key 73571BB9 && \  
sh -c 'echo "deb http://deb.dovetail-automata.com wheezy main" \  
> /etc/apt/sources.list.d/machinekit.list' && \  
sh -c 'echo "deb http://http.debian.net/debian wheezy-backports main" \  
>> /etc/apt/sources.list' && \  
apt-get update && \  
apt-get install -y --no-install-recommends \  
git \  
devscripts \  
fakeroot \  
equivs \  
lsb-release && \  
apt-get install -y -t wheezy-backports cython  
  
WORKDIR /usr/src  
RUN git clone git://github.com/machinekit/machinekit.git  
  
WORKDIR machinekit  
RUN ./debian/configure -prx && \  
yes | mk-build-deps -i -r && \  
debuild -eDEB_BUILD_OPTIONS="parallel=4" -us -uc -b -j4  
  

