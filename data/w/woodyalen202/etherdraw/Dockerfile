FROM ubuntu:14.04  
MAINTAINER lucien <lucienchu@hotmail.com>  
  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv
E1DD270288B4E6030699E45FA1715D88E1DF1F24 \  
&& echo "deb http://ppa.launchpad.net/git-core/ppa/ubuntu trusty main" >>
/etc/apt/sources.list \  
# && sed -Ei
'1,$s/http:\/\/archive.ubuntu.com\/ubuntu\//http:\/\/cn.archive.ubuntu.com\/ubuntu\//g'
/etc/apt/sources.list \  
&& DEBIAN_FRONTEND=noninteractive apt-get update -q \  
&& apt-get upgrade -y \  
&& apt-get install -y libcairo2-dev \  
libjpeg8-dev \  
libpango1.0-dev \  
libgif-dev \  
build-essential \  
g++ \  
git-core \  
curl \  
mysql-client  
  
RUN curl -sL https://deb.nodesource.com/setup_4.x | sudo -E bash - \  
&& apt-get install -y nodejs \  
&& addgroup --quiet --gid 200 rain \  
&& useradd rain --uid=200 --gid=200 --home-dir /app --no-create-home  
  
WORKDIR /app  
RUN git clone git://github.com/JohnMcLear/draw.git  
  
RUN cd /app/draw \  
# && npm config set registry https://registry.npm.taobao.org \  
&& bin/installDeps.sh  
  
COPY docker-entrypoint.sh /app  
  
RUN mkdir -p /data \  
&& chown -R rain:rain /data \  
&& chown -R rain:rain /app \  
&& apt-get autoclean \  
&& rm -rf /tmp/* /usr/share/man/*  
  
VOLUME /data  
  
#USER rain  
ENTRYPOINT ["/app/docker-entrypoint.sh"]  
  

