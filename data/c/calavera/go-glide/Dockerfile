FROM golang:1.8.0-stretch  
  
ENV GLIDE_VERSION v0.12.3  
ENV GLIDE_DOWNLOAD_URL
https://github.com/Masterminds/glide/releases/download/$GLIDE_VERSION/glide-$GLIDE_VERSION-
linux-amd64.tar.gz  
ENV GLIDE_DOWNLOAD_SHA256
0e2be5e863464610ebc420443ccfab15cdfdf1c4ab63b5eb25d1216900a75109  
  
ENV PATH $PATH:/usr/local/glide/linux-amd64  
  
RUN curl -fsSL "$GLIDE_DOWNLOAD_URL" -o glide.tar.gz \  
&& echo "$GLIDE_DOWNLOAD_SHA256 glide.tar.gz" | sha256sum -c - \  
&& mkdir -p /usr/local/glide \  
&& tar -C /usr/local/glide -xzf glide.tar.gz \  
&& rm glide.tar.gz  

