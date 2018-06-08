FROM alpine:3.4  
  
ENV MINIFY_VERSION=2.0.0  
  
RUN apk add --no-cache wget ca-certificates \  
&& cd /tmp/ \  
&& wget https://bin.equinox.io/a/bj7R1Tn1wta/minify-${MINIFY_VERSION}-linux-
amd64.tar.gz \  
&& tar xzf minify-${MINIFY_VERSION}-linux-amd64.tar.gz \  
&& rm -r minify-${MINIFY_VERSION}-linux-amd64.tar.gz \  
&& mv minify /usr/bin/minify \  
&& apk del wget ca-certificates  

