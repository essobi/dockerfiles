FROM avatao/webide:ubuntu-16.04  
RUN apt-get update \  
&& apt-get install -qy \  
cmake \  
valgrind \  
&& rm -rf /var/lib/apt/lists/* /var/lib/mysql/*  
  
COPY . /  
  
RUN cd /usr/src/cmocka \  
&& sed -i 's/#define __func__ __FUNCTION__//g'
/usr/src/cmocka/include/cmocka.h \  
&& mkdir build \  
&& cd build \  
&& cmake -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_BUILD_TYPE=Release .. \  
&& make \  
&& make install \  
&& make clean \  
&& rm -f /etc/nginx/sites-available/server \  
&& rm -f /etc/php/7.0/fpm/pool.d/server.conf \  
&& ln -s /usr/share/pin/pin /usr/bin/pin  
  
VOLUME ["/var/run/php-fpm", "/var/cache/nginx", "/run", "/tmp", "/var/log"]  
  
EXPOSE 8888 7777  
CMD ["supervisord", "-c", "/etc/supervisor/server.conf"]  

