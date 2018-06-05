FROM bradjones/dotnet:latest  
LABEL maintainer "brad@bjc.id.au"  
# Install Node.js repo  
RUN curl -sL https://deb.nodesource.com/setup_7.x | bash -  
  
# Install the Xamarin Mono Repo  
# NOTE: The intention is not to target "Mono" but the the "CoreCLR".  
# Mono & MsBuild are however used for the IDE's to run things like Omnisharp,
etc.  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 \--recv-keys
3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF && \  
echo "deb http://download.mono-project.com/repo/debian wheezy main" | tee
/etc/apt/sources.list.d/mono-xamarin.list && \  
echo "deb http://download.mono-project.com/repo/debian wheezy-apache24-compat
main" | tee -a /etc/apt/sources.list.d/mono-xamarin.list && \  
echo "deb http://download.mono-project.com/repo/debian wheezy-libjpeg62-compat
main" | tee -a /etc/apt/sources.list.d/mono-xamarin.list  
  
# Install everything needed to run an X app inside a container.  
# NOTE: I copied this from some other Dockerfile, it can probably  
# be optimized a little bit.  
RUN export DEBIAN_FRONTEND=noninteractive && \  
apt-get update && \  
apt-get install -y --no-install-recommends \  
mono-complete \  
msbuild \  
nodejs \  
chromium \  
git \  
libc6-dev \  
libgtk2.0-0 \  
libgtk-3-0 \  
libpango-1.0-0 \  
libcairo2 \  
libfontconfig1 \  
libgconf2-4 \  
libnss3 \  
libasound2 \  
libxtst6 \  
unzip \  
libglib2.0-bin \  
libcanberra-gtk-module \  
libgl1-mesa-glx \  
build-essential \  
gettext \  
libstdc++6 \  
software-properties-common \  
xterm \  
automake \  
libtool \  
autogen \  
libnotify-bin \  
aspell \  
aspell-en \  
htop \  
gvfs-bin \  
libxss1 \  
rxvt-unicode-256color \  
x11-xserver-utils \  
sudo \  
vim \  
xdg-utils \  
libgl1-mesa-dri \  
libcanberra-gtk-module \  
libexif-dev \  
pulseaudio && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# Install typescript, its highly likely that  
# C# and TypeScript will be used together.  
RUN npm install -g typescript

