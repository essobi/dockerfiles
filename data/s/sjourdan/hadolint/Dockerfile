FROM debian:jessie-slim  
LABEL name="hadolint"  
LABEL version=1.2.1  
ENV HADOLINT_VERSION=1.2.1  
MAINTAINER Stephane Jourdan <fasten@fastmail.fm>  
RUN apt-get update -y \  
&& apt-get -y install --no-install-recommends wget=1.16-1+deb8u1
libgmp10=2:6.0.0+dfsg-6 ca-certificates=20141019+deb8u1 \  
&& wget -O /usr/bin/hadolint
"https://github.com/lukasmartinelli/hadolint/releases/download/v${HADOLINT_VERSION}/hadolint_linux_amd64"
\  
&& chmod +x /usr/bin/hadolint \  
&& apt-get remove -y wget ca-certificates \  
&& apt-get -y clean \  
&& apt-get -y autoremove \  
&& rm -rf /var/lib/apt/* \  
&& rm -rf /var/lib/cache/* \  
&& rm -rf /var/lib/log/* \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /tmp/*  
ENTRYPOINT ["/usr/bin/hadolint"]  
CMD ["-"]  

