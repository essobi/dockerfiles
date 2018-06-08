FROM debian:wheezy  
MAINTAINER Roman Atachiants "roman@misakai.com"  
# The versions (github branches) that should be pulled and compiled  
ENV MONO_VERSION=mono-4.4.0.182  
# The dependencies needed for the compilation process, they will be deleted
once the docker image is baked  
ENV SETUP_TOOLS="git autoconf libtool automake build-essential mono-devel
gettext python"  
WORKDIR /deploy  
  
RUN apt-get update \  
&& apt-get install -y curl unzip s3cmd $SETUP_TOOLS \  
&& apt-key adv --keyserver pgp.mit.edu --recv-keys
3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF \  
&& git clone git://github.com/mono/llvm.git \  
&& cd /deploy/llvm \  
&& ./configure --enable-optimized --enable-targets="x86 x86_64" \  
&& make \  
&& make install \  
&& cd /deploy \  
&& git clone git://github.com/mono/mono --branch $MONO_VERSION \  
&& cd /deploy/mono \  
&& bash ./autogen.sh --enable-llvm=yes \  
&& make get-monolite-latest \  
&& make \  
&& make install \  
&& apt-get remove -y --purge $SETUP_TOOLS \  
&& apt-get autoremove -y \  
&& rm -rf /deploy \  
&& mkdir /app  
  
WORKDIR /app  

