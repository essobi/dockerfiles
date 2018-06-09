FROM alpine  
  
# Install packages to download TeX live  
RUN apk update \  
&& apk add perl wget xz \  
&& rm -rf /var/cache/apk/*  
  
# Install TeX live  
COPY texlive.profile /  
RUN wget ftp://tug.org/historic/systems/texlive/2018/install-tl-unx.tar.gz \  
&& tar xzvf install-tl-unx.tar.gz \  
&& ./install-tl-*/install-tl -profile texlive.profile \  
&& rm -rf install-tl-* \  
&& rm texlive.profile  
  
ENV PATH="/usr/local/texlive/2018/bin/x86_64-linuxmusl:${PATH}"  

