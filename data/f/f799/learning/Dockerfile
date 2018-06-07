FROM ubuntu:16.04  
# system update 50MB程度  
ENV TZ Asia/Tokyo  
RUN apt-get -y update \  
&& apt-get install -y tzdata \  
# && rm -rf /var/lib/apt/lists/* \  
&& echo "${TZ}" > /etc/timezone \  
&& rm /etc/localtime \  
&& ln -s /usr/share/zoneinfo/Asia/Tokyo /etc/localtime \  
&& dpkg-reconfigure -f noninteractive tzdata  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get install -y apt-utils  
#RUN apt-get install -y --no-install-recommends apt-utils  
# set locale  
RUN apt-get install -y language-pack-ja  
#RUN unlink /etc/localtime  
#RUN ln -s /usr/share/zoneinfo/Japan /etc/localtime  
#RUN apt-get reinstall -y glibc-common  
#RUN apt-get reinstall -y glibc  
#RUN yum group install -y "Japanese Support"  
#RUN mkdir /usr/share/i18n/  
#RUN touch /usr/share/i18n/charmaps  
#RUN locale-gen ja_JP.UTF-8  
RUN localedef -f UTF-8 -i ja_JP ja_JP  
  
ENV LANG ja_JP.UTF-8  
ENV LC_CTYPE ja_JP.UTF-8  
ENV LC_NUMERIC ja_JP.UTF-8  
ENV LC_TIME ja_JP.UTF-8  
ENV LC_COLLATE ja_JP.UTF-8  
ENV LC_MONETARY ja_JP.UTF-8  
ENV LC_MESSAGES ja_JP.UTF-8  
ENV LC_PAPER ja_JP.UTF-8  
ENV LC_NAME ja_JP.UTF-8  
ENV LC_ADDRESS ja_JP.UTF-8  
ENV LC_TELEPHONE ja_JP.UTF-8  
ENV LC_MEASUREMENT ja_JP.UTF-8  
ENV LC_IDENTIFICATION ja_JP.UTF-8  
ENV LC_ALL ja_JP.UTF-8  
ENV LANGUAGE ja_JP:ja  
  
RUN apt-get -y update  
RUN apt-get -y install kbd  
  
# editor install 191kB程度  
RUN apt-get -y install nano  
  
## dotnet core  
RUN apt-get -y install apt-transport-https  
ENV PROJECT /project  
RUN mkdir $PROJECT  
WORKDIR $PROJECT  
RUN apt-get -y install curl  
#RUN curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor >
microsoft.gpg  
#RUN mv microsoft.gpg /etc/apt/trusted.gpg.d/microsoft.gpg  
## https://github.com/dotnet/core/blob/master/release-notes/download-
archive.md  
RUN sh -c 'echo "deb [arch=amd64] https://apt-
mo.trafficmanager.net/repos/dotnet-release/ xenial main" >
/etc/apt/sources.list.d/dotnetdev.list'  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 417A0893  
RUN apt-get update  
RUN apt-get -y install dotnet-dev-1.0.4  
  
ENV DOTNET_SKIP_FIRST_TIME_EXPERIENCE true  
ENV UGET_XMLDOC_MODE skip  
#ENV ASPNETCORE_ENVIROMENT=Development,Staging,Production  
#How to Use  
#docker build -t <tag> .  
#docker run -it -p 5000:5000 <tag> /bin/bash  
#dotnet restore  
#dotnet build  
#ASPNETCORE_URLS="http://*:5000" dotnet run  
#curl http://192.168.99.100:5000  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys
3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF  
RUN sh -c 'echo "deb http://download.mono-project.com/repo/debian
wheezy/snapshots/4.6.0.245 main" > /etc/apt/sources.list.d/mono-xamarin.list'  
RUN apt-get update  
RUN apt-get -y install mono-complete  
RUN apt-get -y install mono-devel referenceassemblies-pcl  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys
3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF  
RUN sh -c 'echo "deb http://download.mono-project.com/repo/debian
wheezy/snapshots/4.6.0.245 main" > /etc/apt/sources.list.d/mono-xamarin.list'  
RUN apt-get update  
RUN apt-get -y install mono-complete  
RUN apt-get -y install mono-devel referenceassemblies-pcl  
  
ENV DEBIAN_FRONTEND teletype  

