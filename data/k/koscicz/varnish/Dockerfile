FROM baseruntime/baseruntime:latest  
  
# Image metadata  
ENV NAME=varnish \  
VARNISH_VERSION=5.0.0 \  
VERSION=0 \  
RELEASE=1 \  
ARCH=x86_64  
  
# Labels  
LABEL com.redhat.component="$NAME" \  
name="$FGC/$NAME" \  
summary="Varnish is an HTTP accelerator" \  
description="Varnish is an HTTP accelerator designed for content-heavy dynamic
web sites." \  
version="$VERSION" \  
release="$RELEASE.$DISTTAG" \  
architecture="$ARCH" \  
usage="docker run -p <PORT>:6081 -p <MANAGEMENT_PORT>:6082" \  
io.k8s.description="Varnish is an HTTP accelerator designed for content-heavy
dynamic web sites." \  
io.k8s.display-name="Varnish" \  
io.openshift.expose-services="6801:http" \  
io.openshift.tags="http,proxy,varnish,varnish5"  
#install varnish  
RUN microdnf install -y varnish --nodocs && \  
microdnf clean all && \  
mkdir /varnish_secret && mkdir /varnish_config && \  
dd if=/dev/random of=/varnish_secret/varnish_secret count=1  
  
# Add configuration file  
COPY files/default.vcl /varnish_config/default.vcl  
  
# Copy help file  
COPY root/help.1 /  
  
# Expose ports for varnish and it's admin CLI  
EXPOSE 6801 6802  
  
# Generate a new secret and start varnish in the foreground  
CMD /usr/sbin/varnishd -f /varnish_config/default.vcl -a :6081 -T :6082 -s
malloc,256M -S /varnish_secret/varnish_secret -F  

