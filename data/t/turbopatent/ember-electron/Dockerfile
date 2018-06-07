FROM circleci/node:8.9.0-stretch-browsers  
  
ENV MONO_VERSION 4.8.0.495  
USER root  
  
# WineHQ repo  
RUN curl -sS https://dl.winehq.org/wine-builds/Release.key | apt-key add -  
RUN echo "deb https://dl.winehq.org/wine-builds/debian/ stretch main" | tee
/etc/apt/sources.list.d/winehq.list  
  
# Mono repo  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys
3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF  
RUN echo "deb http://download.mono-project.com/repo/debian stretch main" | tee
/etc/apt/sources.list.d/mono-official.list  
  
RUN dpkg --add-architecture i386  
RUN apt-get install apt-transport-https  
RUN apt-get update && \  
apt-get install -y --no-install-recommends \  
golang \  
vim \  
fakeroot \  
mono-devel \  
ca-certificates-mono \  
osslsigncode \  
# libsecret needed for keytar  
libsecret-1-dev \  
# libc6-dev-i386 needed to build for 32-bit (keytar native)  
libc6-dev-i386  
RUN apt-get install -y --install-recommends winehq-stable  
RUN apt-get clean && rm -rf /var/lib/apt/lists/*  
  
# build stubbed signtool.exe which can run under wine and call osslsigntool  
COPY ./main.go /gosigntool/main.go  
WORKDIR /gosigntool  
RUN GOOS=windows GOARCH=386 go build -o signtool.exe main.go  
RUN cp signtool.exe /usr/local/bin/signtool.exe  
COPY ./osslsign.sh /usr/local/bin/osslsign.sh  
  
USER circleci  
  
ENV WINEDEBUG -all,err+all  
ENV WINEDLLOVERRIDES winemenubuilder.exe=d  
ENV WINEARCH=win64  
  
RUN wineboot --init  

