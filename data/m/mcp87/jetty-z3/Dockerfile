FROM jetty:9  
  
ENV Z3_VERSION "4.5.0"  
  
# install debian packages  
RUN apt-get update -qq -y \  
&& apt-get install default-jdk binutils python g++ make ant -y \  
  
# purge caches  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
  
# download, compile and install z3  
&& mkdir /opt/z3 && cd /opt/z3 \  
&& wget -qO- https://github.com/Z3Prover/z3/archive/z3-${Z3_VERSION}.tar.gz |
tar xz --strip-components=1 \  
&& python scripts/mk_make.py \--java \  
&& cd build && make && make install

