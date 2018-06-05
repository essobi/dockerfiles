FROM bitnami/minideb:stretch  
MAINTAINER Olivier ORABONA <github.com/oorabona>  
  
ENV DEBIAN_FRONTEND=noninteractive \  
LISTEN_IP=0.0.0.0 \  
LISTEN_PORT=443 \  
SSH_HOST=localhost \  
SSH_PORT=22 \  
OPENVPN_HOST=localhost \  
OPENVPN_PORT=1194 \  
HTTPS_HOST=localhost \  
HTTPS_PORT=8443  
  
COPY docker-entrypoint.sh /  
  
# Add dependencies to compile sslh from sources  
RUN apt-get update \  
&& install_packages ca-certificates git make gcc libc6-dev libpcre3-dev
libwrap0-dev libconfig8-dev \  
&& git clone https://github.com/yrutschle/sslh.git /sslh \  
&& cd /sslh && make install \  
&& rm -rf /sslh \  
&& chmod +x /docker-entrypoint.sh  
  
EXPOSE 443  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
# By default we return sslh version. It has two reasons:  
# First, it shows the current built version (and since we are git cloning that
might be useful)  
# Second, it makes sure that we actually did configure it at least to change
to foreground mode !  
CMD ["-V"]  

