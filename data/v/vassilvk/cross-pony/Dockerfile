FROM ubuntu:16.04  
# Space-separated list of extra libraries to pass to the linker.  
# Put those libraries in the following locations depending on what platform
you target:  
# - Linux: /usr/local/lib/extra/linux-amd64/  
# - Windows: /usr/local/lib/extra/windows-amd64/  
ENV EXTRA_LIBS=  
  
# LLVM version used by pony  
ENV LLVM_PONY_VERSION 3.9.1  
# Side-by-side LLVM version used to cross-compile pony code.  
ENV LLVM_CROSS_COMPILE_VERSION 6.0  
# Copy arm64v8 libraries.  
COPY --from=vassilvk/arm64v8-ponyc:latest /lib/ /opt/aarch64-linux-gnu/lib/  
COPY --from=vassilvk/arm64v8-ponyc:latest /usr/lib/ /opt/aarch64-linux-
gnu/usr/lib/  
COPY --from=vassilvk/arm64v8-ponyc:latest /usr/local/lib/pony/
/opt/aarch64-linux-gnu/usr/local/lib/pony/  
COPY --from=vassilvk/arm64v8-ponyc:latest /lib/aarch64-linux-gnu/
/lib/aarch64-linux-gnu/  
# Copy windows libraries.  
COPY --from=vassilvk/cross-pony-winlib:latest /windows-amd64/
/usr/local/lib/windows-amd64/  
  
# Copy bootstrap script.  
COPY bin/ /usr/local/bin/  
  
RUN apt-get update \  
&& apt-get install -y \  
apt-transport-https \  
g++ \  
git \  
libncurses5-dev \  
libpcre2-dev \  
libssl-dev \  
make \  
wget \  
xz-utils \  
zlib1g-dev \  
# Install pony stable.  
&& apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys "D401AB61
DBE1D0A2" \  
&& echo "deb https://dl.bintray.com/pony-language/pony-stable-debian /" | tee
-a /etc/apt/sources.list \  
&& apt-get update \  
&& apt-get install -y \  
pony-stable \  
# Install pony's LLVM.  
&& rm -rf /var/lib/apt/lists/* \  
&& echo Deploying LLVM ${LLVM_PONY_VERSION}... \  
&& wget -q -O -
http://llvm.org/releases/${LLVM_PONY_VERSION}/clang+llvm-${LLVM_PONY_VERSION}-x86_64-linux-
gnu-ubuntu-16.04.tar.xz \  
| tar xJf - --strip-components 1 -C /usr/local/
clang+llvm-${LLVM_PONY_VERSION}-x86_64-linux-gnu-ubuntu-16.04 \  
# Turn off SSL cert verification for git as github ca-certificates are broken
for ubuntu 16.04.  
&& git config --global http.sslVerify false \  
# Grab ponyc source.  
&& cd /tmp \  
&& git clone https://github.com/ponylang/ponyc.git \  
&& cd /tmp/ponyc \  
# Remove .git - this will prevent git-tagging the target folder where ponyc is
installed.  
&& rm -rf .git \  
# Build ponyc.  
&& export CC=`which gcc` \  
&& make arch=x86-64 tune=intel \  
&& make install \  
# Install LLVM used for cross-compiling pony code.  
&& echo "deb http://apt.llvm.org/xenial/ llvm-toolchain-
xenial-${LLVM_CROSS_COMPILE_VERSION} main" | tee -a /etc/apt/sources.list \  
&& wget -O - https://apt.llvm.org/llvm-snapshot.gpg.key|apt-key add - \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends \  
clang-${LLVM_CROSS_COMPILE_VERSION} \  
lld-${LLVM_CROSS_COMPILE_VERSION} \  
# Make all library names lower-case.  
&& find /usr/local/lib/windows-amd64 -depth -exec rename
's/(.*)\/([^\/]*)/$1\/\L$2/' {} \; \  
# Create upper-case symlink to each Windows library name (i.e.
/usr/local/lib/windows-amd64/msvc/MSVCRT.lib => /usr/local/lib/windows-
amd64/msvc/msvcrt.lib).  
# Some libs are being referred to by their upper-case name, some by their
lower-case names.  
&& for FILE in /usr/local/lib/windows-amd64/*/**; do echo $FILE | sed -r -e
"s|(.*/)(.*)(\\.lib)|\1\U\2\L\3|" | xargs -L1 bash -c 'ln -s "${0,,}" "$0" ';
done \  
# Fix arm64v8 lost symlinks.  
&& rm /opt/aarch64-linux-gnu/usr/lib/gcc/aarch64-linux-gnu/5.4.0/libgcc_s.so \  
&& ln -s /opt/aarch64-linux-gnu/lib/aarch64-linux-gnu/libgcc_s.so.1
/opt/aarch64-linux-gnu/usr/lib/gcc/aarch64-linux-gnu/5.4.0/libgcc_s.so \  
&& rm /opt/aarch64-linux-gnu/usr/lib/gcc/aarch64-linux-gnu/5/libgcc_s.so \  
&& ln -s /opt/aarch64-linux-gnu/lib/aarch64-linux-gnu/libgcc_s.so.1
/opt/aarch64-linux-gnu/usr/lib/gcc/aarch64-linux-gnu/5/libgcc_s.so \  
&& ln -s /opt/aarch64-linux-gnu/lib/aarch64-linux-gnu/ /lib/aarch64-linux-gnu/
\  
# Set up cross-ponyc.  
&& chmod +x /usr/local/bin/cross-ponyc* \  
# Create extra lib directories.  
&& mkdir -p /usr/local/lib/extra/linux-amd64/ \  
&& mkdir -p /usr/local/lib/extra/linux-arm64v8/ \  
&& mkdir -p /usr/local/lib/extra/windows-amd64/ \  
# Cleanup.  
&& cd / \  
&& rm -rf /tmp/ponyc \  
&& rm -rf /tmp/cross-pony/ \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
WORKDIR /src/main  
  
ENTRYPOINT ["cross-ponyc"]

