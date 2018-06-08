# Glitch ruby scripts to have fun with the interpreter.  
#  
# RUN sudo docker run --init shyouhei/ruby-afl  
# MONITOR: sudo docker exec deadbeef afl-whatsup /root/test_out  
# RESULT: sudo docker cp deadbeef:/root/test_out ~/result  
#  
FROM debian:stretch-slim  
MAINTAINER shyouhei@ruby-lang.org  
ADD sources.list /etc/apt/  
ADD keywords /root/  
  
WORKDIR /root  
  
# RUN echo 'Acquire::HTTP::Proxy "http://172.17.0.1:3142";' >>
/etc/apt/apt.conf.d/01proxy  
RUN set -ex && \  
apt update && \  
apt-get build-dep -y --no-install-recommends ruby2.3 && \  
apt install -y --no-install-recommends git clang llvm llvm-dev && \  
apt upgrade -y && \  
apt autoremove && \  
apt clean && \  
rm -rf /var/cache/apt/archives /var/lib/apt/lists  
RUN git clone https://github.com/mirrorer/afl && \  
cd afl && \  
make -j4 all && \  
make -C llvm_mode -j4 all LLVM_CONFIG=llvm-config-3.8 && \  
make install && \  
cd && \  
rm -rf afl  
RUN git clone \--depth 1 --branch american-fuzzy-lop --single-branch \  
https://github.com/shyouhei/ruby && \  
cd ruby && \  
autoconf && \  
./configure -C --disable-install-doc --with-gcc=afl-clang-fast && \  
make -j4 miniruby  
ADD test_in /root/test_in  
RUN mkdir test_cmin && \  
mkdir test_tmin && \  
mkdir test_out && \  
afl-cmin -i test_in -o test_cmin ruby/miniruby @@ && \  
cd test_cmin && \  
for i in *.rb; do \  
afl-tmin -i $i -o /root/test_tmin/$i \-- /root/ruby/miniruby @@; \  
done && \  
cd && \  
rm -rf test_in && mkdir test_in && \  
afl-cmin -i test_tmin -o test_in ruby/miniruby @@ && \  
rm -rf test_cmin test_tmin  
  
CMD afl-fuzz -i test_in -o test_out -M bunny1 -x keywords -t 128 -m 256 --
ruby/miniruby @@ sleep 1 & \  
afl-fuzz -i test_in -o test_out -S bunny2 -x keywords -t 128 -m 256 --
ruby/miniruby @@ sleep 1 & \  
afl-fuzz -i test_in -o test_out -S bunny3 -x keywords -t 128 -m 256 --
ruby/miniruby @@  

