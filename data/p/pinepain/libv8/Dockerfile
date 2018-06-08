FROM ubuntu:xenial as build  
  
ARG V8=6.6.286  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV TERM=xterm-256color  
ENV LC_ALL=C.UTF-8  
ENV NO_INTERACTION=1  
ENV REPORT_EXIT_STATUS=1  
ENV DEPOT_TOOLS_UPDATE=0  
  
RUN apt-get update && \  
apt-get install -y libglib2.0-dev git curl && \  
mkdir /opt/libv8  
  
RUN echo 'solutions = [' >> /tmp/.gclient && \  
echo ' {' >> /tmp/.gclient && \  
echo ' "url": "https://chromium.googlesource.com/v8/v8.git",' >> /tmp/.gclient
&& \  
echo ' "managed": False,' >> /tmp/.gclient && \  
echo ' "name": "v8",' >> /tmp/.gclient && \  
echo ' "deps_file": "DEPS",' >> /tmp/.gclient && \  
echo ' "custom_deps": {},' >> /tmp/.gclient && \  
echo ' },' >> /tmp/.gclient && \  
echo ']' >> /tmp/.gclient && \  
echo 'target_os = [ "linux" ]' >> /tmp/.gclient && \  
echo 'target_os_only = True' >> /tmp/.gclient  
  
RUN cd /tmp && git clone --depth=1
https://chromium.googlesource.com/chromium/tools/depot_tools.git && \  
export PATH=`pwd`/depot_tools:"${PATH}" && \  
export NPROCS=`grep -c ^processor /proc/cpuinfo` && \  
gclient sync --no-history --reset -j ${NPROCS} -r ${V8} && \  
cd v8 && \  
gn gen out.gn/x64.release --args="is_debug=false is_official_build=true
is_component_build=true is_cfi=false is_clang=false
v8_use_external_startup_data=false treat_warnings_as_errors=false
use_custom_libcxx=false use_sysroot=false use_gold=false
use_allocator_shim=false" && \  
gn args out.gn/x64.release --list > out.gn/x64.release/gn_args.txt && \  
ninja -j ${NPROCS} -v d8 -C out.gn/x64.release  
  
RUN cd /tmp/v8 && \  
mkdir -p /opt/libv8/include && \  
mkdir -p /opt/libv8/lib && \  
mkdir -p /opt/libv8/dbg && \  
cp -R include /opt/libv8/ && \  
cp out.gn/x64.release/*.so /opt/libv8/lib/ && \  
cp out.gn/x64.release/icudtl.dat /opt/libv8/lib/ && \  
cp out.gn/x64.release/d8 /opt/libv8/lib/ && \  
cp out.gn/x64.release/gn_args.txt /opt/libv8/lib/ && \  
debugdir=/opt/libv8/dbg && \  
for tostripfile in /opt/libv8/lib/*.so; do \  
filename=$(basename "${tostripfile}") ; \  
debugfile="${filename}.dbg" ; \  
objcopy --only-keep-debug "${tostripfile}" "${debugdir}/${debugfile}" ; \  
strip --strip-debug --strip-unneeded "${tostripfile}" ; \  
objcopy --add-gnu-debuglink="${debugdir}/${debugfile}" "${tostripfile}" ; \  
done  
  
  
FROM ubuntu:xenial  
  
COPY --from=build /opt/libv8 /opt/libv8  

