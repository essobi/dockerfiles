FROM debian:jessie  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV PSSH_VERSION 2.3.1  
ENV PSSH_DEB_VERSION 2.3.1-1  
RUN set -x \  
&& apt-get update -qq \  
&& apt-get install -qq --no-install-recommends pssh=${PSSH_DEB_VERSION} \  
&& apt-get clean -qq \  
&& rm -rf /var/lib/apt/lists/*  
  
CMD ["parallel-ssh"]  

