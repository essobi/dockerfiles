FROM golang:1.9.3-stretch  
  
ENV GLIDE_VERSION v0.13.0  
ENV GLIDE_DOWNLOAD_URL
https://github.com/Masterminds/glide/releases/download/$GLIDE_VERSION/glide-$GLIDE_VERSION-
linux-amd64.tar.gz  
ENV GLIDE_DOWNLOAD_SHA256
77680bbd9e51de9a5cbd212f4d0aab51abac49971695f0bc779b117f8cb188ff  
  
ENV PATH $PATH:/usr/local/glide/linux-amd64  
  
RUN curl -fsSL "$GLIDE_DOWNLOAD_URL" -o glide.tar.gz \  
&& echo "$GLIDE_DOWNLOAD_SHA256 glide.tar.gz" | sha256sum -c - \  
&& mkdir -p /usr/local/glide \  
&& tar -C /usr/local/glide -xzf glide.tar.gz \  
&& rm glide.tar.gz  

