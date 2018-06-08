FROM debian:wheezy  
MAINTAINER Christopher J Lyth <cjlyth@gmail.com>  
  
RUN apt-get update \  
&& apt-get -qq -y install \  
build-essential \  
git \  
curl \  
cmake \  
\--no-install-recommends  
  
RUN echo 'deb http://http.us.debian.org/debian/ testing non-free contrib main'
\  
>> /etc/apt/sources.list \  
&& apt-get update \  
&& apt-get -qq -y -t testing install \  
valac=0.26.* \  
libgtk-3-dev=3.14.* \  
intltool=0.50.* \  
libclutter-gtk-1.0-0=1.6.* \  
libkeybinder-3.0-dev=0.3.* \  
libgee-0.8-dev=0.16.* \  
libnotify-bin=0.7.* \  
libmx-dev=1.4.* \  
clutter-gtk-1.0 \  
\--no-install-recommends  
  
# at the time of writing there were no tags in github  
ENV SRC_VERSION master  
ENV SRC_TAR_URL https://github.com/p-e-w/finalterm/archive/master.tar.gz  
ENV SRC_REPO_URL https://github.com/p-e-w/finalterm.git  
ENV SRC_DIR /usr/src/finalterm  
  
ENV DESTDIR /opt/finalterm  
VOLUME ["/opt/finalterm"]  
VOLUME ["/usr/src/finalterm/build"]  
COPY entrypoint.sh /usr/local/bin/  
  
WORKDIR /usr/src/finalterm  
RUN mkdir -p /usr/src/finalterm \  
&& curl -sSL $SRC_TAR_URL \  
| tar -xz --strip-components=1 \  
&& chmod +x /usr/local/bin/entrypoint.sh  
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]  
CMD ["cmake"]  
  

