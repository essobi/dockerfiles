FROM nvidia/cuda:9.0-runtime-ubuntu16.04  
ENV NVIDIA_DRIVER_CAPABILITIES compute,utility,video  
  
ENV FFMPEG_VERSION=4.0 \  
FFMPEG_RELEASE=4.0 \  
FFMPEG_CHECKSUM=ed945daf40b124e77a685893cc025d086f638bc703183460aff49508edb3a43f
\  
FFMPEG_SOURCE=/usr/local/src/ffmpeg \  
FFMPEG_TARBALL=/usr/local/src/ffmpeg-4.0.tar.xz \  
HOME=/srv/stream  
  
LABEL name="bbxnet/transcode-ffmpeg" \  
version="${FFMPEG_VERSION}" \  
release="1" \  
maintainer="Tomáš Havlas <havlas@bbxnet.sk>" \  
vendor="BBXNET"  
  
ENV TRANSCODE_CONF_PATH=/etc/transcode \  
TRANSCODE_INPUTD_PATH=/etc/transcode/input.d \  
TRANSCODE_OUTPUTD_PATH=/etc/transcode/output.d  
  
RUN apt-get update \  
&& RUNTIME_DEPS=" \  
gettext-base \  
libass5 \  
libfdk-aac0 \  
libmp3lame0 \  
libnss-wrapper \  
openssl " \  
&& apt-get install --yes --no-install-recommends --verbose-versions
${RUNTIME_DEPS} \  
&& rm --recursive /var/lib/apt/lists/*  
  
RUN apt-get update \  
&& BUILD_DEPS=" \  
autoconf \  
automake \  
build-essential \  
ca-certificates \  
cmake \  
cuda-libraries-dev-${CUDA_PKG_VERSION} \  
cuda-nvml-dev-${CUDA_PKG_VERSION} \  
cuda-minimal-build-${CUDA_PKG_VERSION} \  
cuda-command-line-tools-${CUDA_PKG_VERSION} \  
git \  
libass-dev \  
libfdk-aac-dev \  
libfreetype6-dev \  
libmp3lame-dev \  
libnccl-dev=${NCCL_VERSION}-1+cuda9.0 \  
libtheora-dev \  
libtool \  
libvorbis-dev \  
mercurial \  
pkg-config \  
texinfo \  
wget \  
zlib1g-dev " \  
&& apt-get install --yes --no-install-recommends --verbose-versions
${BUILD_DEPS} \  
\  
&& cd /usr/local/src \  
&& wget http://www.nasm.us/pub/nasm/releasebuilds/2.13.03/nasm-2.13.03.tar.bz2
\  
&& tar xjvf nasm-2.13.03.tar.bz2 \  
&& cd nasm-2.13.03 \  
&& ./autogen.sh \  
&& ./configure --prefix=/usr/local \--bindir=/usr/local/bin \  
&& make --jobs=$( nproc ) \  
&& make --jobs=$( nproc ) install \  
&& cd / \  
\  
&& cd /usr/local/src \  
&& wget -O yasm-1.3.0.tar.gz
http://www.tortall.net/projects/yasm/releases/yasm-1.3.0.tar.gz \  
&& tar xzvf yasm-1.3.0.tar.gz \  
&& cd yasm-1.3.0 \  
&& ./configure --prefix=/usr/local \--bindir=/usr/local/bin \  
&& make --jobs=$( nproc ) \  
&& make --jobs=$( nproc ) install \  
&& cd / \  
\  
&& cd /usr/local/src \  
&& git -C x264 pull 2> /dev/null || git clone \--branch stable --depth 1
https://git.videolan.org/git/x264.git \  
&& cd x264 \  
&& PKG_CONFIG_PATH="/usr/local/lib/pkgconfig" ./configure --prefix=/usr/local
\--bindir=/usr/local/bin --enable-static \  
&& make --jobs=$( nproc ) \  
&& make --jobs=$( nproc ) install \  
&& cd / \  
\  
&& cd /usr/local/src \  
&& if cd x265 2> /dev/null; then hg pull && hg update; else hg clone
https://bitbucket.org/multicoreware/x265; fi \  
&& cd x265/build/linux \  
&& cmake -G "Unix Makefiles" -DCMAKE_INSTALL_PREFIX=/usr/local
-DENABLE_SHARED:bool=off ../../source \  
&& make --jobs=$( nproc ) \  
&& make --jobs=$( nproc ) install \  
&& cd / \  
\  
&& cd /usr/local/src \  
&& git clone https://git.videolan.org/git/ffmpeg/nv-codec-headers.git \  
&& cd nv-codec-headers \  
&& make --jobs=$( nproc ) \  
&& make --jobs=$( nproc ) install \  
\  
&& wget -O "${FFMPEG_TARBALL}"
"https://ffmpeg.org/releases/ffmpeg-${FFMPEG_RELEASE}.tar.xz" \  
&& echo "${FFMPEG_CHECKSUM} *${FFMPEG_TARBALL}" | sha256sum --check - \  
&& mkdir -p "${FFMPEG_SOURCE}" \  
&& tar --extract --xz --strip-components=1 \  
\--directory="${FFMPEG_SOURCE}" \  
\--file="${FFMPEG_TARBALL}" \  
&& cd "${FFMPEG_SOURCE}" \  
&& PKG_CONFIG_PATH="/usr/local/lib/pkgconfig" ./configure \  
\--prefix="/usr/local" \  
\--pkg-config-flags="--static" \  
\--extra-cflags="-I/usr/local/include -I/usr/local/cuda/include" \  
\--extra-ldflags="-L/usr/local/lib -L/usr/local/cuda/lib64" \  
\--extra-libs="-lpthread -lm" \  
\--bindir="/usr/local/bin" \  
\--enable-gpl \  
\--enable-libass \  
\--enable-libfdk-aac \  
\--enable-libfreetype \  
\--enable-libmp3lame \  
\--enable-libx264 \  
\--enable-libx265 \  
\--enable-nonfree \  
\--enable-cuda \  
\--enable-cuvid \  
\--enable-nvenc \  
\--enable-nonfree \  
\--enable-libnpp \  
&& make --jobs=$( nproc ) \  
&& make --jobs=$( nproc ) install \  
&& echo | gcc -shared -o /usr/lib/x86_64-linux-gnu/libGL.so.1
-Wl,-soname=libGL.so.1 -x c - \  
&& cd / \  
\  
&& apt-get purge --yes --auto-remove ${BUILD_DEPS} \  
&& rm --recursive \  
/usr/local/src/* \  
/var/lib/apt/lists/*  
  
ENV CONTAINER_ENTRYPOINT_PATH=/usr/share/container-entrypoint \  
CONTAINER_PASSWD_PATH="${TRANSCODE_CONF_PATH}/passwd"  
  
COPY [ "./common/root", "./transcode-ffmpeg/root", "/" ]  
  
VOLUME [ "${HOME}" ]  
  
WORKDIR "${HOME}"  
ENTRYPOINT [ "container-entrypoint" ]  
CMD [ "run-transcode" ]  

