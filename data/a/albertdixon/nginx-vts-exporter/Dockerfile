FROM alpine:3.5  
MAINTAINER Albert Dixon <albert@dixon.rocks>  
  
EXPOSE 9913  
ENTRYPOINT ["/sbin/tini", "--", "su-exec", "nobody", "/bin/nginx-vts-
exporter"]  
ENV VERSION=v0.3  
RUN apk add --update --no-cache ca-certificates curl tar tini su-exec \  
&& curl -Ls https://github.com/hnlq715/nginx-vts-
exporter/releases/download/${VERSION}/nginx-vts-exporter-linux-amd64.tar.gz |\  
tar xvzf - -C /bin/ \  
&& chmod 755 /bin/nginx-vts-exporter \  
&& apk del --purge curl tar  

