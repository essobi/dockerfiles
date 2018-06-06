FROM debian:testing-slim  
  
RUN mkdir /root/export  
RUN mkdir /root/ffmpeg  
  
RUN echo '#!/bin/bash\n\  
tstamp=`date +%s`\n\  
ffmpeg_git_checkout_version=master\n\  
USAGE="--ffmpeg-git-checkout-version=[master] a particular version of FFmpeg,
ex: n4.0 or a specific git hash\n\  
\--ivybridge=y ivybridge optimizations"\n\  
if [ "$#" == "0" ]; then\n\  
echo "$USAGE"\n\  
exit 1\n\  
fi\n\  
\n\  
while true; do\n\  
case $1 in\n\  
-h | --help ) echo "$USAGE\n\  
"; exit 0 ;;\n\  
\--ffmpeg-git-checkout-version=* ) ffmpeg_git_checkout_version="${1#*=}";
shift ;;\n\  
\--ivybridge=* ) ivybridge="${1#*=}"; shift ;;\n\  
\-- ) shift; break ;;\n\  
-* ) echo "Error, unknown option: $1."; exit 1 ;;\n\  
* ) break ;;\n\  
esac\n\  
done\n\  
\n\  
date +%s >/root/export/start_tstamp\n\  
echo ${ffmpeg_git_checkout_version}\n\  
cd /root/ffmpeg\n\  
git clone https://github.com/vookimedlo/ffmpeg-windows-build-helpers.git\n\  
cd /root/ffmpeg/ffmpeg-windows-build-helpers\n\  
[ $ivybridge = "y" ] && git checkout ivybridge && git pull\n\  
./cross_compile_ffmpeg.sh --ffmpeg-git-checkout-
version=${ffmpeg_git_checkout_version} --disable-nonfree=n --compiler-
flavors=win64 2>&1 | tee -a build-log\n\  
\n\  
cd /root/ffmpeg/ffmpeg-windows-build-helpers\n\  
[ -e /root/ffmpeg-${ffmpeg_git_checkout_version}-logs-${tstamp}.7z ] && rm
/root/ffmpeg-${ffmpeg_git_checkout_version}-logs-${tstamp}.7z\n\  
7z a -mx=9
/root/export/ffmpeg-${ffmpeg_git_checkout_version}-logs-${tstamp}.7z build-
log\n\  
\n\  
cd /root/ffmpeg/ffmpeg-windows-build-
helpers/sandbox/cross_compilers/mingw-w64-x86_64/x86_64-w64-mingw32/bin/\n\  
[ -e /root/ffmpeg-${ffmpeg_git_checkout_version}-${tstamp}.7z ] && rm
/root/ffmpeg-${ffmpeg_git_checkout_version}-${tstamp}.7z\n\  
7z a -mx=9 /root/export/ffmpeg-${ffmpeg_git_checkout_version}-${tstamp}.7z
ffmpeg.exe ffplay.exe x264.exe x265.exe\n\  
date +%s >/root/export/end_tstamp\n\  
' > /root/ffmpeg/build_ffmpeg  
  
RUN chmod 755 /root/ffmpeg/build_ffmpeg  
  
RUN cat /root/ffmpeg/build_ffmpeg  
  
RUN apt-get update && apt-get -y install software-properties-common  
RUN apt-get update && apt-get -y --allow-unauthenticated install \  
autoconf \  
autoconf-archive \  
autogen \  
automake \  
bison \  
bzip2 \  
cmake \  
curl \  
cvs \  
ed \  
flex \  
g++ \  
gcc \  
git \  
gperf \  
libtool \  
make \  
mercurial \  
nasm \  
p7zip-full \  
pax \  
pkg-config \  
subversion \  
texinfo \  
unzip \  
wget \  
yasm \  
zlib1g-dev \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV PATH /root/ffmpeg/:$PATH  
ENTRYPOINT ["build_ffmpeg"]  
CMD ["--help"]  
  
  
# execution chain  
#  
  
#docker build -t debian-ffmpeg-crosscompile-win_x64 .  
#docker run debian-ffmpeg-crosscompile-win_x64 --ffmpeg-git-checkout-
version=n4.0 --ivybridge=y  
#docker container wait `docker ps -alq` > docker_exitcode  
#docker container logs `docker ps -alq` > docker_logs  
#docker cp `docker ps -alq`:'/root/export' ~/  
#docker container rm `docker ps -alq`  
#docker image rm debian-ffmpeg-crosscompile-win_x64  

