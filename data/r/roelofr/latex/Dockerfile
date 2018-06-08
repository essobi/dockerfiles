# vim: set ft=docker :  
FROM debian:stable-slim  
  
LABEL maintainer="Roelof Roos <github@roelof.io>"  
  
RUN apt-get update -yq \  
&& apt-get install -yq \  
curl \  
git \  
make \  
perl \  
tar \  
wget \  
zip \  
&& apt-get clean -yq \  
&& rm -rf /var/cache/apt/*  
  
# Install the texlive installer  
RUN mkdir -p /usr/src/texlive-installer \  
&& wget \  
\--output-document=/tmp/texlive-installer.tar.gz \  
http://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz \  
&& tar \  
\--dir=/usr/src/texlive-installer \  
\--extract \  
\--file=/tmp/texlive-installer.tar.gz \  
\--gzip \  
\--strip-components=1 \  
&& rm /tmp/texlive-installer.tar.gz  
  
# Install TexLive with the correct flavour  
WORKDIR /usr/src/texlive-installer/  
  
LABEL texlive.flavour="tetex"  
  
COPY ./texlive.profile /usr/src/texlive-installer/texlive.profile  
  
RUN /usr/src/texlive-installer/install-tl \  
\--repository ctan \  
\--profile /usr/src/texlive-installer/texlive.profile  
  
WORKDIR /usr/src/texlive-installer  
  
CMD ["/bin/sh"]  

