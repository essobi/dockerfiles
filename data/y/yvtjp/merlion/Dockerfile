  
# Dockerfile for MerlionServer.  
FROM debian:jessie  
MAINTAINER Tomoaki KAWADA <i@yvt.jp>  
  
# Install Clang and so on  
RUN apt-get update \  
&& apt-get install -y curl clang git python-dev libbz2-dev  
&& rm -rf /var/lib/apt/lists/*  
  
# Install Mono (based on
https://github.com/mono/docker/blob/master/3.10.0/Dockerfile)  
RUN apt-key adv --keyserver pgp.mit.edu --recv-keys
3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF  
  
# FIXME: Debian release mismatch!  
RUN echo "deb http://download.mono-project.com/repo/debian
wheezy/snapshots/3.10.0 main" > /etc/apt/sources.list.d/mono-xamarin.list \  
&& apt-get update \  
&& apt-get install -y mono-devel fsharp mono-vbnc nuget \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN mozroots --machine --import --sync --quiet  
  
# Install Boost  
WORKDIR /tmp  
RUN curl -L
"http://sourceforge.net/projects/boost/files/boost/1.57.0/boost_1_57_0.tar.gz/download"
\  
| gunzip | tar -x && mv boost_1_57_0 boost \  
&& cd boost && ./bootstrap.sh --with-toolset=clang && ./b2 -j4 && ./b2 install
\  
&& cd .. && rm -R boost  
  
# Install make  
RUN apt-get update \  
&& apt-get install -y cmake libssl-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV MERLION_ROOT /opt/merlion  
ENV MERLION_SRC_ROOT ${MERLION_ROOT}/src  
ENV MERLION_CONFIG_ROOT ${MERLION_ROOT}/etc  
ENV MERLION_BIN_ROOT ${MERLION_ROOT}/bin  
  
RUN mkdir -p ${MERLION_SRC_ROOT}  
RUN mkdir -p ${MERLION_CONFIG_ROOT}  
RUN mkdir -p ${MERLION_BIN_ROOT}  
  
# Add Merlion source code  
ADD Merlion.sln LICENSE.md README.md ${MERLION_SRC_ROOT}/  
ADD Merlion ${MERLION_SRC_ROOT}/Merlion  
ADD MerlionFramework ${MERLION_SRC_ROOT}/MerlionFramework  
ADD MerlionServer ${MERLION_SRC_ROOT}/MerlionServer  
ADD MerlionServerCore ${MERLION_SRC_ROOT}/MerlionServerCore  
ADD MerlionServerUtils ${MERLION_SRC_ROOT}/MerlionServerUtils  
  
# Build MerlionServerCore  
WORKDIR ${MERLION_BIN_ROOT}  
ENV CC /usr/bin/clang  
ENV CXX /usr/bin/clang++  
RUN cmake \  
${MERLION_SRC_ROOT}/MerlionServerCore \  
&& cd ${MERLION_BIN_ROOT} && make -j4 \  
&& rm -Rf CMakeFiles  
  
# Build MerlionServer  
WORKDIR ${MERLION_SRC_ROOT}  
RUN nuget restore -NonInteractive  
RUN xbuild /property:Configuration=Release
/property:OutDir=${MERLION_BIN_ROOT}/ /target:MerlionServer  
  
# Put default config  
WORKDIR ${MERLION_CONFIG_ROOT}  
ADD docker/server.config docker/make_cert.sh ${MERLION_CONFIG_ROOT}/  
RUN ./make_cert.sh  
  
# Link config  
WORKDIR ${MERLION_BIN_ROOT}  
RUN rm -f MerlionServer.exe.config && ln -s
${MERLION_CONFIG_ROOT}/server.config MerlionServer.exe.config  
  
# Command  
ENTRYPOINT ["/usr/bin/mono", "MerlionServer.exe"]  
  
# Accept nodes (master only)  
EXPOSE 5000  
# Accept web management console access (master only)  
EXPOSE 11450  
# Accept clients (master only)  
EXPOSE 16070  

