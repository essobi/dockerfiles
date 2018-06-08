FROM alpine:3.6  
ARG RANCHER_VERSION=v0.6.1  
ENV RANCHER_URL ''  
ENV RANCHER_ACCESS_KEY ''  
ENV RANCHER_SECRET_KEY ''  
RUN apk update && apk add bash ca-certificates curl && update-ca-certificates  
  
# RANCHER  
RUN curl -L
https://github.com/rancher/cli/releases/download/${RANCHER_VERSION}/rancher-
linux-amd64-${RANCHER_VERSION}.tar.gz -o /usr/share/rancher-linux.tar.gz \  
&& mkdir /usr/local/share/rancher/ \  
&& tar xvzf /usr/share/rancher-linux.tar.gz --strip 2 -C
/usr/local/share/rancher/ \  
&& chmod +x /usr/local/share/rancher/rancher \  
&& ln -s /usr/local/share/rancher/rancher /usr/local/bin/ \  
&& rm /usr/share/rancher-linux.tar.gz \  
&& mkdir /rancher  
  
WORKDIR /rancher  
  
# ENTRYPOINT  
ADD entrypoint.sh /usr/local/share/entrypoint/entrypoint  
RUN chmod +x /usr/local/share/entrypoint/entrypoint \  
&& ln -s /usr/local/share/entrypoint/entrypoint /usr/local/bin  
  
ENTRYPOINT ["entrypoint"]

