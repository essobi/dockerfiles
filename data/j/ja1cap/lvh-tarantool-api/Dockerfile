FROM centos:7  
RUN groupadd tarantool \  
&& adduser -g tarantool tarantool  
  
ENV
LUAROCKS_URL=http://keplerproject.github.io/luarocks/releases/luarocks-2.3.0.tar.gz
\  
MONGO_C_DRIVER_URL=https://github.com/mongodb/mongo-c-
driver/releases/download/1.8.1/mongo-c-driver-1.8.1.tar.gz \  
APP_SOURCE_PATH=/var/www/api/tarantool \  
TARANTOOL_INSTANCE_NAME=api \  
TARANTOOL_ENV=docker  
  
RUN yum -y install nano curl wget git cmake gcc-c++ build-essential openssl-
devel pcre pcre-devel  
  
# Install Tarantool  
RUN yum clean all  
RUN rm -f /etc/yum.repos.d/*tarantool*.repo  
RUN echo $'\n\  
[tarantool_1_7]\n\  
name=EnterpriseLinux-\$releasever - Tarantool\n\  
baseurl=http://download.tarantool.org/tarantool/1.7/el/\$releasever/\$basearch/\n\  
gpgkey=http://download.tarantool.org/tarantool/1.7/gpgkey\n\  
repo_gpgcheck=1\n\  
gpgcheck=0\n\  
enabled=1\n\  
\n\  
[tarantool_1_7-source]\n\  
name=EnterpriseLinux-\$releasever - Tarantool Sources\n\  
baseurl=http://download.tarantool.org/tarantool/1.7/el/\$releasever/SRPMS\n\  
gpgkey=http://download.tarantool.org/tarantool/1.7/gpgkey\n\  
repo_gpgcheck=1\n\  
gpgcheck=0\n\  
' >> /etc/yum.repos.d/tarantool_1_7.repo  
RUN yum makecache -y --disablerepo='*' \--enablerepo='tarantool_1_7'  
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
  
# Install mongo-c-driver  
RUN yum -y install pkg-config openssl-devel cyrus-sasl-devel  
RUN wget -O mongo-c-driver.tar.gz "$MONGO_C_DRIVER_URL"  
RUN mkdir -p /usr/src/mongo-c-driver  
RUN tar -xzf mongo-c-driver.tar.gz -C /usr/src/mongo-c-driver --strip-
components=1  
RUN (cd /usr/src/mongo-c-driver; ./configure --disable-automatic-init-and-
cleanup; make; make install)  
# Install lua-mongo  
RUN git clone https://github.com/neoxic/lua-mongo.git /usr/src/lua-mongo  
RUN (cd /usr/src/lua-mongo && cmake . && make && make install)  
  
# Install MySQL luarock  
# RUN yum -y install mysql-devel  
# RUN git clone https://github.com/tarantool/mysql.git /usr/src/tarantool-
mysql  
# RUN (cd /usr/src/tarantool-mysql && cmake .
-DCMAKE_BUILD_TYPE=RelWithDebInfo && make && make install)  
# Symlink /usr/local/lib64  
RUN echo "/usr/local/lib" >> /etc/ld.so.conf.d/libc.conf  
RUN rm -rf /usr/local/lib64  
RUN ln -s /usr/local/lib /usr/local/lib64  
# Update shared library cache  
RUN rm -rf /etc/ld.so.cache && ldconfig  
  
RUN mkdir -p /tmp/build  
COPY Makefile /tmp/build/  
COPY vendor /tmp/build/vendor  
RUN make -C /tmp/build install_modules  
RUN mkdir -p $APP_SOURCE_PATH  
  
COPY console.lua /usr/local/bin/console  
COPY tarantool_is_up.bash /usr/local/bin/tarantool_is_up  
  
RUN rm -rf /etc/tarantool/instances.available  
RUN ln -s $APP_SOURCE_PATH /etc/tarantool/instances.available  
RUN chmod 0777 -Rf /var/log/tarantool  
  
VOLUME [ "$APP_SOURCE_PATH", "/var/log/tarantool", "/var/lib/tarantool" ]  
  
EXPOSE 3301  
WORKDIR $APP_SOURCE_PATH  
  
HEALTHCHECK CMD tarantool_is_up  
  
CMD mkdir -p /var/lib/tarantool/${HOSTNAME} /var/log/tarantool/${HOSTNAME} \  
&& chown -R tarantool:tarantool /var/lib/tarantool/${HOSTNAME}
/var/log/tarantool/${HOSTNAME} \  
&& cp -a /tmp/build/lua_modules $APP_SOURCE_PATH \  
&& tarantool $TARANTOOL_INSTANCE_NAME.lua  

