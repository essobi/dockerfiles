# Defines an image that is used as the base for all FFIG Docker images. This  
# includes the dependencies required to build and use FFIG, but not the FFIG  
# code or derived applications.  
FROM ubuntu:17.10  
MAINTAINER FFIG <support@ffig.org>  
  
RUN apt-get -y update && \  
apt-get install -y \  
python-software-properties \  
software-properties-common  
  
# Software dependencies - sorted alphabetically  
RUN add-apt-repository -y ppa:ubuntu-toolchain-r/test && \  
apt-get -y update && \  
apt-get install -y \  
clang \  
cmake \  
curl \  
dos2unix \  
git \  
golang \  
libc++-dev \  
libc++1 \  
libclang-5.0-dev \  
libunwind8 \  
luajit \  
mono-devel \  
ninja-build \  
pypy \  
python-pip \  
python3 \  
python3-pip \  
ruby \  
ruby-dev  
  
# Install .NET Core  
ENV DOTNET_SDK_VERSION 2.0.2  
ENV DOTNET_DOWNLOAD_URL
https://dotnetcli.blob.core.windows.net/dotnet/Sdk/$DOTNET_SDK_VERSION/dotnet-
sdk-$DOTNET_SDK_VERSION-linux-x64.tar.gz  
  
RUN curl -SL $DOTNET_DOWNLOAD_URL \--output dotnet.tar.gz \  
&& mkdir -p /usr/share/dotnet \  
&& tar -zxf dotnet.tar.gz -C /usr/share/dotnet \  
&& rm dotnet.tar.gz \  
&& ln -s /usr/share/dotnet/dotnet /usr/bin/dotnet  
  
# Trigger the population of the local package cache  
ENV NUGET_XMLDOC_MODE skip  
RUN mkdir warmup \  
&& cd warmup \  
&& dotnet new \  
&& cd .. \  
&& rm -rf warmup \  
&& rm -rf /tmp/NuGetScratch  
  
# Python dependencies  
RUN pip2 install --upgrade pip && \  
pip2 install jinja2 nose pycodestyle virtualenv && \  
pip3 install --upgrade pip && \  
pip3 install jinja2 nose pycodestyle virtualenv  
  
# Ruby dependencies  
RUN gem install ffi  
  
# Cleanup  
RUN apt-get autoremove -y && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# User and environment setup  
RUN useradd ffig && \  
mkdir -p /home/ffig && \  
chown ffig /home/ffig  
  
ENV HOME=/home/ffig \  
LD_LIBRARY_PATH=/usr/lib/llvm-5.0/lib:$LD_LIBRARY_PATH  

