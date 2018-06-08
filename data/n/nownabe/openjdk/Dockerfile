FROM phusion/baseimage:0.9.15  
MAINTAINER nownabe  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# apt-get高速化のためにミラーサーバを設定  
ADD sources.list /etc/apt/sources.list  
  
# apt-get高速化、キャッシュ無効化  
# https://github.com/docker/docker/issues/824  
RUN echo "force-unsafe-io" > /etc/dpkg/dpkg.cfg.d/02apt-speedup && \  
echo "Acquire::http {No-Cache=True;};" > /etc/apt/apt.conf.d/no-cache  
  
# open-jdkインストール  
RUN apt-get update && \  
apt-get upgrade -yq && \  
apt-get remove -yq ca-certificates && \  
apt-get install -yq --no-install-recommends \  
openjdk-7-jre-headless && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  

