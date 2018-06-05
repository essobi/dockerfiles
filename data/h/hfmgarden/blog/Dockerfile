FROM debian:9-slim  
  
ENV H2O_VER 2.2.4  
RUN build_deps='build-essential cmake wget zlib1g-dev ruby bison' \  
&& apt-get -qq update \  
&& apt-get -qq -y install --no-install-recommends $build_deps ca-certificates
\  
&& rm -rf /var/lib/apt/lists/* \  
&& wget -q https://github.com/h2o/h2o/archive/v${H2O_VER}.tar.gz -O- | tar xz
\  
&& cd "h2o-${H2O_VER}" \  
&& cmake -DWITH_BUNDLED_SSL=on -DWITH_MRUBY=ON . \  
&& make \  
&& make install \  
&& cd \  
&& rm -rf "h2o-${H2O_VER}" \  
&& apt-get purge -y --auto-remove $build_deps  
  
COPY h2o.conf /etc/h2o.conf  
EXPOSE 80 443  
CMD "h2o"  

