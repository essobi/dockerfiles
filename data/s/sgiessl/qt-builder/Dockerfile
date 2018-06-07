FROM ubuntu:xenial  
  
# Increment in order to enforce rebuilding the build-environment (invalidating
cached docker layers).  
ENV REFRESHED_AT 2018-06-01  
ENV DEBIAN_FRONTEND noninteractive  
ENV DEBCONF_NONINTERACTIVE_SEEN true  
  
#########################  
### Update repository & install dependencies  
#########################  
RUN apt-get update  
RUN apt-get install --no-install-recommends -y --force-yes \  
software-properties-common \  
runit \  
build-essential \  
ccache \  
cmake \  
git \  
vim \  
ninja-build \  
wget \  
gcc \  
g++ \  
&& apt-get clean  
  
#########################  
### QT dev modules  
#########################  
# Similar to this in effect: add-apt-repository ppa:beineri/opt-qt59-xenial  
ADD files/apt-key-qt5.asc /tmp/  
RUN echo 'deb http://ppa.launchpad.net/beineri/opt-qt59-xenial/ubuntu xenial
main' > /etc/apt/sources.list.d/qt5x.list && \  
apt-key add /tmp/apt-key-qt5.asc && \  
rm /tmp/apt-key-qt5.asc && \  
apt-get update  
RUN apt-get install --no-install-recommends -y --force-yes \  
qt59-meta-minimal \  
qt59declarative \  
&& apt-get clean  
  
#########################  
### Custom project dependencies....  
#########################  
RUN apt-get install --no-install-recommends -y --force-yes \  
libssh-dev \  
libgl1-mesa-dev \  
&& apt-get clean  
  
#########################  
### Convenience wrappers  
#########################  
ADD files/init files/wrap-user files/wrap-build-env /  
  
ENTRYPOINT ["/init"]  

