# Sample contents of Dockerfile  
# Stage 1  
# TO REPLACE FROM microsoft/aspnetcore-build:2.0.2-stretch AS builder  
  
FROM buildpack-deps:stretch-scm  
  
ENV NET_VERSION 2.0.2  
  
RUN buildDeps='apt-transport-https curl' \  
&& set -x \  
&& apt-get update \  
&& apt-get -y install $buildDeps --no-install-recommends \  
&& curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor >
microsoft.gpg \  
&& mv microsoft.gpg /etc/apt/trusted.gpg.d/microsoft.gpg \  
&& sh -c 'echo "deb [arch=amd64]
https://packages.microsoft.com/repos/microsoft-debian-stretch-prod stretch
main" > /etc/apt/sources.list.d/dotnetdev.list' \  
&& apt-get update \  
&& apt-get install -y dotnet-sdk-$NET_VERSION nuget \  
&& apt-get purge -y \--auto-remove $buildDeps \  
&& apt-get autoremove \  
&& apt-get clean  
  
  
WORKDIR /

