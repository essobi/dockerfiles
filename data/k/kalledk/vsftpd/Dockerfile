FROM debian:jessie  
  
MAINTAINER Kalle R. Møller <docker@k-moeller.dk>  
  
ARG DEBIAN_FRONTEND=noninteractive  
ARG S6_VERSION=v1.18.1.5  
RUN apt-get update -q -y \  
&& apt-get install -q -y --no-install-recommends curl ca-certificates \  
&& curl -L -o /tmp/s6-overlay-amd64.tar.gz "https://github.com/just-
containers/s6-overlay/releases/download/${S6_VERSION}/s6-overlay-amd64.tar.gz"
\  
&& tar xzf /tmp/s6-overlay-amd64.tar.gz -C / \  
&& apt-get --purge autoremove curl ca-certificates -q -y \  
&& apt-get clean -q -y  
  
RUN apt-get update -q -y \  
&& apt-get install -q -y --no-install-recommends \  
vsftpd \  
libpam-pwdfile \  
apache2-utils \  
openssl \  
&& apt-get clean -q -y  
  
COPY etc/vsftpd.conf /etc/  
COPY etc/vsftpd /etc/pam.d/  
COPY etc/01-vsftpd-data-dir /etc/fix-attrs.d/  
COPY etc/01-vsftpd-external-ip /etc/cont-init.d/  
COPY etc/genpass /bin/genpass  
  
RUN \  
useradd -m \  
\--home /home/vsftpd \  
\--gid nogroup \  
\--shell /bin/false \  
vsftpd \  
&& mkdir -p /var/run/vsftpd/empty \  
&& mkdir -p /etc/vsftpd \  
&& mkdir -p /etc/vsftpd/users \  
&& touch /etc/vsftpd/ftpd.passwd  
  
VOLUME ["/var/vsftpd"]  
  
EXPOSE 21 10100-10199  
ENTRYPOINT ["/init"]  
  
CMD ["/usr/sbin/vsftpd"]  

