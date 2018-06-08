FROM debian:latest  
  
# Credits go to Henri Menke <texlive@henrimenke.de>  
# https://github.com/pycnic/tl-
docker/tree/57d05320f9541a4d5152e5bb1f57c4953cf061ca/2016  
MAINTAINER Andreas Sorge <as@pycnic.org>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
COPY texlive.profile /  
  
RUN apt-get update \  
&& apt-get install --no-install-recommends -y \  
wget xzdec perl fontconfig \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
&& wget http://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz \  
&& tar xzvf install-tl-unx.tar.gz \  
&& ./install-tl-*/install-tl -profile texlive.profile \  
&& rm -rf install-tl-*  
  
RUN mkdir /var/tex  
WORKDIR /var/tex  
CMD ["/usr/local/bin/pdflatex", "--version"]  

