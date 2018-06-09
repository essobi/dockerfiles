FROM ubuntu:16.04 as tidlc  
  
RUN \  
apt-get update \  
&& apt-get install -y \  
git \  
flex \  
bison \  
libgtest-dev \  
libperl-dev \  
libgtk2.0-dev \  
build-essential \  
cmake \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN \  
cd /usr/src/gtest \  
&& cmake CMakeLists.txt \  
&& make \  
&& cp ./*.a /usr/lib/  
RUN \  
git clone https://git.tizen.org/cgit/platform/core/appfw/tidl -b tizen \  
&& cd tidl \  
&& ./build.sh build \  
&& cp ./build/idlc/tidlc /usr/local/bin/tidlc  
  
FROM ubuntu:16.04  
  
ARG user=developer  
ARG group=developer  
ARG uid=2000  
ARG gid=2000  
  
# Install prerequisites  
RUN \  
apt-get update \  
&& apt-get install -y \  
ca-certificates \  
wget \  
curl \  
zip \  
software-properties-common \  
apt-transport-https \  
pciutils \  
libxcb-xfixes0 \  
libxi6 \  
libpixman-1-0 \  
libxcb-render-util0 \  
python2.7 \  
libwebkitgtk-1.0-0 \  
libxcb-image0 \  
acl \  
libsdl1.2debian \  
libv4l-0 \  
libxcb-randr0 \  
libxcb-shape0 \  
libx11-xcb1 \  
libxcb-icccm4 \  
libfontconfig1 \  
libsm6 \  
libjpeg-turbo8 \  
gettext \  
rpm2cpio \  
cpio \  
make \  
bridge-utils \  
openvpn \  
git \  
ruby \  
tzdata \  
virtualenv \  
python \  
python-requests \  
python-pycurl \  
python-lxml \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install Java  
RUN \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
debconf-set-selections \  
&& add-apt-repository -y ppa:webupd8team/java \  
&& apt-get update \  
&& apt-get install -y oracle-java8-installer \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /var/cache/oracle-jdk8-installer  
  
# Install dotnet core prerequisites  
RUN \  
apt-get update \  
&& apt-get install -y \  
libunwind8 \  
liblttng-ust0 \  
libcurl3 \  
libssl1.0.0 \  
libuuid1 \  
libkrb5-3 \  
zlib1g \  
libicu55 \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install dotnet core 2.0 sdk  
RUN \  
curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor >
microsoft.gpg \  
&& mv microsoft.gpg /etc/apt/trusted.gpg.d/microsoft.gpg  
RUN \  
sh -c 'echo "deb [arch=amd64] https://packages.microsoft.com/repos/microsoft-
ubuntu-xenial-prod xenial main" > /etc/apt/sources.list.d/dotnetdev.list' \  
&& apt-get update \  
&& apt-get install -y dotnet-sdk-2.0.3 \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install mono-devel and nuget  
RUN \  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys
3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF \  
&& sh -c 'echo "deb https://download.mono-project.com/repo/ubuntu stable-
xenial main" > /etc/apt/sources.list.d/mono-official-stable.list' \  
&& apt-get update \  
&& apt-get install -y mono-devel \  
&& rm -rf /var/lib/apt/lists/* \  
&& wget https://dist.nuget.org/win-x86-commandline/latest/nuget.exe \  
&& mv nuget.exe /usr/lib/nuget.exe \  
&& sh -c 'echo "#!/bin/bash \n/usr/bin/cli /usr/lib/nuget.exe \$@" >
/usr/bin/nuget' \  
&& chmod 755 /usr/bin/nuget  
  
# Copy tidlc binary  
COPY --from=tidlc /usr/local/bin/tidlc /usr/local/bin/tidlc  
  
# Setup timezone to avoid error from nuget cli  
ENV TZ 'Asia/Seoul'  
RUN \  
echo $TZ > /etc/timezone \  
&& rm /etc/localtime \  
&& ln -snf /usr/share/zoneinfo/$TZ /etc/localtime \  
&& dpkg-reconfigure -f noninteractive tzdata  
  
# Add a user  
ENV HOME /home/${user}  
RUN groupadd -g ${gid} ${group} \  
&& useradd -d "$HOME" -u ${uid} -g ${gid} -m -s /bin/bash ${user}  
  
USER ${user}  
WORKDIR ${HOME}  
  
# Install tizen studio 2.4  
RUN \  
wget http://download.tizen.org/sdk/Installer/tizen-studio_2.4/web-
cli_Tizen_Studio_2.4_ubuntu-64.bin \  
&& chmod +x web-cli_Tizen_Studio_2.4_ubuntu-64.bin \  
&& echo y | ./web-cli_Tizen_Studio_2.4_ubuntu-64.bin --accept-license \  
&& rm -rf web-cli_Tizen_Studio_2.4_ubuntu-64.bin  
  
# Install sdk-build  
RUN \  
git clone git://git.tizen.org/sdk/tools/sdk-build -b tizen  
  
# Set PATH  
ENV PATH $PATH:$HOME/tizen-studio/tools/ide/bin/:$HOME/tizen-studio/package-
manager/:$HOME/sdk-build/  
  
# Setup python3 virtualenv  
RUN \  
virtualenv venv -p python3 \  
&& . venv/bin/activate \  
&& pip install requests pyyaml lxml jinja2 \  
&& deactivate  

