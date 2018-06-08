FROM gipert/centos-base:latest  
  
USER root  
  
RUN yum install -y -q libedit-devel ncurses-devel \  
openssl openssl-devel symlinks && \  
yum -q clean all  
  
WORKDIR /scif  
RUN mkdir -p /scif/julia/pkgs && \  
wget -q -O- https://baltig.infn.it/gerda/baseos-
binaries/raw/master/julia-0.6.2-centos7-x86_64.tar.gz \  
| tar --strip-components 1 -xz -C "/scif/julia"  
  
#WORKDIR /scif/julia  
#RUN git clone https://github.com/JuliaLang/julia.git src && \  
# cd src && git checkout v0.6.2 && \  
# echo "BUILD_LLVM_CLANG=1" >> Make.user && \  
# export MARCH=core2 && \  
# time make -j"$(nproc)"  
#  
#WORKDIR /scif/julia/src  
#RUN symlinks -r -c . && \  
# rsync -a "usr" "base" "test" "LICENSE.md" "/scif/julia/" && \  
# rm -f "/scif/julia/usr/bin"/*clang* "/scif/julia/usr/bin"/scan-* && \  
# rm -f "/scif/julia/usr/share/julia/test" && rsync -a "/scif/julia/src/test"
"/scif/julia/usr/share/julia/" && \  
# rm -f "/scif/julia/usr/share/julia/base" && rsync -a "/scif/julia/src/base"
"/scif/julia/usr/share/julia/"  
#  
#RUN rsync -a "Make.user" "/scif/julia/" && \  
# mkdir -p "/scif/julia/deps" && rsync -a "deps/Versions.make"
"/scif/julia/deps/Versions.make" && \  
# SRCCACHE_LLVM_PATH=`find deps/srccache -maxdepth 1 -type d -name "llvm-*" |
head -n1` && \  
# mkdir -p "/scif/julia/$SRCCACHE_LLVM_PATH/tools/clang" && \  
# rsync -a "$SRCCACHE_LLVM_PATH/tools/clang/"lib
"/scif/julia/$SRCCACHE_LLVM_PATH/tools/clang/"  
#  
#WORKDIR /scif/julia  
#RUN rm -rf src  
  
ENV PATH="$PATH:/scif/julia/usr/bin" \  
LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/usr/lib64:/scif/julia/usr/lib" \  
MANPATH="$MANPATH:/scif/julia/usr/share/man" \  
JULIA_HOME="/scif/julia/usr/bin" \  
JULIA_PKGDIR="/scif/julia/pkgs"  
  
RUN julia -e 'Pkg.init()'  
  
WORKDIR /data  
CMD /scif/julia/usr/bin/julia  

