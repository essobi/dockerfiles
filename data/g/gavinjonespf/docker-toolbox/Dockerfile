FROM ubuntu:xenial  
MAINTAINER Gavin Jones <gjones@powerfarming.co.nz>  
# https://github.com/moby/moby/releases/  
# https://download.docker.com/linux/static/stable/x86_64/  
ENV DOCKER_VERSION 18.03.0-ce  
# https://github.com/docker/compose/releases/  
ENV DOCKER_COMPOSE_VERSION 1.20.0  
# https://github.com/docker/machine/releases/  
ENV DOCKER_MACHINE_VERSION 0.14.0  
ENV MACH_ARCH x86_64  
ENV TERM xterm  
#To override if needed  
ARG TAG=dev  
ENV TAG ${TAG}  
# https://www.microsoft.com/net/learn/get-started/linuxubuntu  
ENV DOTNET_PACKAGE dotnet-sdk-2.1.4  
# https://github.com/PowerShell/PowerShell/releases  
# Use official list instead  
#ENV POWERSHELL_DOWNLOAD_URL
https://github.com/PowerShell/PowerShell/releases/download/v6.0.0-beta.2/powershell_6.0.0-beta.2-1ubuntu1.16.04.1_amd64.deb  
ENV DISTRIB_CODENAME xenial  
ENV DISTRIB_RELEASE 16.04  
RUN apt-get update \  
&& apt-get install -y git subversion nano wget curl iputils-ping dnsutils \  
&& apt-get clean  
  
#Docker bins  
WORKDIR /home/toolbox/  
# Try new URL  
#RUN curl -L -o /tmp/docker-latest.tgz
https://get.docker.com/builds/Linux/x86_64/docker-${DOCKER_VERSION}.tgz && \  
RUN curl -L -o /tmp/docker-latest.tgz
https://download.docker.com/linux/static/stable/${MACH_ARCH}/docker-${DOCKER_VERSION}.tgz
&& \  
tar -xvzf /tmp/docker-latest.tgz && \  
mv docker/* /usr/bin/  
  
#Docker compose  
RUN curl -L
https://github.com/docker/compose/releases/download/${DOCKER_COMPOSE_VERSION}/docker-
compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose && \  
chmod +x /usr/local/bin/docker-compose  
  
#Docker machine  
RUN curl -L
https://github.com/docker/machine/releases/download/v${DOCKER_MACHINE_VERSION}/docker-
machine-`uname -s`-`uname -m` > /usr/local/bin/docker-machine && \  
chmod +x /usr/local/bin/docker-machine  
  
#Minio tools  
RUN curl -L https://dl.minio.io/server/minio/release/linux-amd64/minio >
/usr/local/bin/minio && \  
chmod +x /usr/local/bin/minio  
RUN curl -L https://dl.minio.io/client/mc/release/linux-amd64/mc >
/usr/local/bin/mc && \  
chmod +x /usr/local/bin/mc  
  
#Mono dev needed for some things with .NET Core for the moment  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys
3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF \  
&& echo "deb http://download.mono-project.com/repo/ubuntu $DISTRIB_CODENAME
main" > /etc/apt/sources.list.d/mono-official.list \  
&& apt-get update \  
&& DEBIAN_FRONTEND="noninteractive" apt-get -y install mono-devel \  
&& apt-get clean  
  
RUN cert-sync /etc/ssl/certs/ca-certificates.crt  
  
# MS Certs and setup needed  
RUN yes | certmgr -ssl -m https://go.microsoft.com \  
yes | certmgr -ssl -m https://nugetgallery.blob.core.windows.net \  
yes | certmgr -ssl -m https://nuget.org  
  
#RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -  
# Register the Microsoft Ubuntu repository  
#RUN apt-get install apt-transport-https curl -y && curl
https://packages.microsoft.com/config/ubuntu/$DISTRIB_RELEASE/prod.list >
/etc/apt/sources.list.d/microsoft.list  
### Install .NET Core, nuget, PowerShell  
RUN apt-get install apt-transport-https curl -y \  
&& apt-get install --reinstall ca-certificates \  
&& curl
https://packages.microsoft.com/config/ubuntu/$DISTRIB_RELEASE/prod.list >
/etc/apt/sources.list.d/microsoft.list \  
&& curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \  
&& apt-get update \  
&& sh -c 'echo "deb [arch=amd64] https://apt-
mo.trafficmanager.net/repos/dotnet-release/ xenial main" >
/etc/apt/sources.list.d/dotnetdev.list' \  
&& apt-get update \  
# && apt-get install ca-certificates \  
&& apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 417A0893
\  
&& apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys
B02C46DF417A0893 \  
# TODO: Fix issues with unauthenticated  
&& apt-get install ${DOTNET_PACKAGE} --allow-unauthenticated -y \  
&& apt-get install -y powershell \  
&& mkdir /powershell \  
&& DEBIAN_FRONTEND="noninteractive" apt-get -y install tzdata unzip nuget \  
&& apt-get clean  
  
  
### Set some environment variables  
# RUN curl -SL $POWERSHELL_DOWNLOAD_URL --output powershell.deb \  
# && apt-get install libunwind8 libicu55 \  
# && dpkg --install powershell.deb \  
# && rm powershell.deb \  
# && apt-get clean  
#Set PSGallery to trusted, and install PS module PSDepend by default  
RUN pwsh -c "Set-PSRepository -Name PSGallery -InstallationPolicy Trusted"  
#RUN powershell -c "Set-PSRepository -Name PSGallery -InstallationPolicy
Trusted"  
#PSDepend not currently working... Re-enable when it does  
RUN pwsh -c "Install-Module -Name PSDepend; Import-Module PSDepend"  
  
RUN echo $TAG >> build_tag  

