FROM commiebstrd/afl-rs-docker:pull  
MAINTAINER Spenser Reinhardt <spenserreinhardt@gmail.com>  
  
# update system  
#RUN pacman -Sy --noconfirm && \  
#pacman -S --noconfirm archlinux-keyring && \  
#pacman -S --noconfirm pacman && \  
#pacman-db-upgrade && \  
#pacman -Syu --noconfirm && \  
#pacman -S --noconfirm wget curl git base-devel clang openssl python2 python
cmake vim llvm  
  
WORKDIR /opt  
  
# RUN git clone https://github.com/rust-lang/rust.git && \  
# git clone https://github.com/rust-lang/cargo && \  
# wget http://lcamtuf.coredump.cx/afl/releases/afl-$VERSION.tgz  
  
RUN cd rust && \  
./configure --enable-clang --disable-libcpp --enable-optimize --disable-docs
&& \  
make -j 4 && \  
cd .. && \  
export PATH=$PATH:/opt/rust/x86_64-unknown-linux-gnu/stage2/bin && \  
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/rust/x86_64-unknown-linux-
gnu/stage2/lib/ && \  
echo 'export PATH=$PATH:/opt/rust/x86_64-unknown-linux-gnu/stage2/bin' >>
/root/.bashrc && \  
echo 'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/rust/x86_64-unknown-linux-
gnu/stage2/lib/' >> /root/.bashrc  
  
# RUN cd cargo && \  
# ./configure --local-rust-root=/opt/rust/x86_64-unknown-linux-gnu/stage2/
--enable-optimize && \  
# make && \  
# export PATH=$PATH:/opt/cargo/target/x86_64-unknown-linux-gnu/release && \  
# echo 'export PATH=$PATH:/opt/cargo/target/x86_64-unknown-linux-gnu/release'
>> /root/.bashrc  
#  
# RUN VERSION=1.96b && \  
# tar xf afl-$VERSION.tgz && \  
# cd afl-$VERSION && \  
# make && \  
# make install  
#  
# ENV USER root  
# ENV PATH
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/opt/cargo/target/x86_64-unknown-
linux-gnu/release:/opt/cargo/target/x86_64-unknown-linux-
gnu/release:/opt/afl-1.96b  
  
WORKDIR /root/  
ENTRYPOINT ["/usr/bin/bash"]  
  
# To build and properly execute this container:  
#  
# docker build --force-rm --rm=true -t arch-rust-afl .  
# echo core > /proc/sys/kernel/core_pattern  
# cd /sys/devices/system/cpu # echo performance | tee
cpu*/cpufreq/scaling_governor  
  
# compilation instructions  
#  
# add deps and features for afl to cargo.toml  
# add to main/lib.rs  
# cargo rustc --verbose --features fuzz -- -Z no-landing-pads  

