FROM centos:7  
RUN groupadd tarantool \  
&& adduser -g tarantool tarantool  
  
ENV
LUAROCKS_URL=http://keplerproject.github.io/luarocks/releases/luarocks-2.3.0.tar.gz  
  
ENV TARANTOOL_INSTANCE_NAME=geonames \  
TARANTOOL_ENV=docker  
  
ENV APP_SOURCE_PATH=/usr/src/tarantool/$TARANTOOL_INSTANCE_NAME \  
APP_DATA_PATH=/var/lib/tarantool/$TARANTOOL_INSTANCE_NAME  
  
RUN yum -y install curl wget git cmake gcc-c++ build-essential openssl-devel
pcre pcre-devel  
  
# Install Tarantool  
RUN yum clean all  
RUN rm -f /etc/yum.repos.d/*tarantool*.repo  
RUN echo $'\n\  
[tarantool_1_8]\n\  
name=EnterpriseLinux-\$releasever - Tarantool\n\  
baseurl=http://download.tarantool.org/tarantool/1.8/el/\$releasever/\$basearch/\n\  
gpgkey=http://download.tarantool.org/tarantool/1.8/gpgkey\n\  
repo_gpgcheck=1\n\  
gpgcheck=0\n\  
enabled=1\n\  
\n\  
[tarantool_1_8-source]\n\  
name=EnterpriseLinux-\$releasever - Tarantool Sources\n\  
baseurl=http://download.tarantool.org/tarantool/1.8/el/\$releasever/SRPMS\n\  
gpgkey=http://download.tarantool.org/tarantool/1.8/gpgkey\n\  
repo_gpgcheck=1\n\  
gpgcheck=0\n\  
' >> /etc/yum.repos.d/tarantool_1_8.repo  
RUN yum makecache -y --disablerepo='*' \--enablerepo='tarantool_1_8'  
RUN yum -y install tarantool tarantool-devel  
  
# Install LUA  
RUN yum -y install lua lua-devel  
  
# Required for installing rock from .rock files  
RUN yum -y install zip unzip  
  
# Install LUAROCKS  
RUN wget -O luarocks.tar.gz "$LUAROCKS_URL"  
RUN mkdir -p /usr/src/luarocks  
RUN tar -xzf luarocks.tar.gz -C /usr/src/luarocks --strip-components=1  
RUN (cd /usr/src/luarocks; ./configure; make build; make install)  
RUN rm -r /usr/src/luarocks  
  
# Install MySQL rock  
RUN yum -y install mysql-devel  
RUN git clone https://github.com/tarantool/mysql.git tarantool-mysql  
RUN (cd tarantool-mysql && cmake . -DCMAKE_BUILD_TYPE=RelWithDebInfo && make
&& make install)  
  
# Install GIS rock  
RUN yum -y install https://download1.rpmfusion.org/free/el/rpmfusion-free-
release-7.noarch.rpm  
RUN yum -y install geos-devel proj-devel  
RUN yum -y install tarantool-gis  
  
# Install dump rock  
RUN tarantoolctl rocks install dump  
  
RUN mkdir -p /tmp/build  
COPY Makefile /tmp/build/  
COPY vendor /tmp/build/vendor  
RUN make -C /tmp/build install_modules  
RUN mkdir -p $APP_SOURCE_PATH  
  
RUN mkdir -p $APP_DATA_PATH  
COPY data/* $APP_DATA_PATH/  
RUN chown -R tarantool:tarantool -R $APP_DATA_PATH  
  
COPY console.lua /usr/local/bin/console  
COPY tarantool_is_up.bash /usr/local/bin/tarantool_is_up  
  
RUN rm -rf /etc/tarantool/instances.available  
RUN ln -s $APP_SOURCE_PATH /etc/tarantool/instances.available  
  
VOLUME [ "$APP_SOURCE_PATH", "/var/log/tarantool", "/var/lib/tarantool" ]  
  
EXPOSE 3301  
WORKDIR $APP_SOURCE_PATH  
  
HEALTHCHECK CMD tarantool_is_up  
  
CMD mkdir -p /var/log/tarantool/${HOSTNAME} \  
&& chown -R tarantool:tarantool /var/log/tarantool/${HOSTNAME} \  
&& cp -a /tmp/build/lua_modules $APP_SOURCE_PATH \  
&& tarantool $TARANTOOL_INSTANCE_NAME.lua  

