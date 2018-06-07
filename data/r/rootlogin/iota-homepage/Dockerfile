FROM debian:stretch as builder  
  
ADD
https://github.com/gohugoio/hugo/releases/download/v0.33/hugo_0.33_Linux-64bit.tar.gz
/tmp/hugo.tgz  
  
RUN set -x \  
&& mkdir -p /opt/hugo /tmp/homepage \  
&& tar xvzf /tmp/hugo.tgz -C /opt/hugo \  
&& chmod +x /opt/hugo/hugo \  
&& apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get -y --no-install-recommends install \  
git  
  
COPY ./ /tmp/homepage  
  
WORKDIR /tmp/homepage  
  
RUN git submodule init \  
&& git submodule update \  
&& /opt/hugo/hugo  
  
FROM nginx:stable-alpine  
  
COPY --from=builder /tmp/homepage/public /usr/share/nginx/html/  

