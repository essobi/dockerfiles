FROM debian:jessie  
MAINTAINER Ted Zlatanov <tzz@lifelogs.com>  
  
LABEL org.label-schema.vendor="Ted Zlatanov <tzz@lifelogs.com>" \  
org.label-schema.url="http://lifelogs.com/" \  
org.label-schema.name="sftp" \  
org.label-schema.description="SFTP server with S3 capability (clones
atmoz/sftp)" \  
org.label-schema.usage="/README.md" \  
org.label-schema.license="Apache" \  
org.label-schema.schema-version="1.0" \  
org.label-schema.docker.params=""  
  
# - Install packages  
# - OpenSSH needs /var/run/sshd to run  
# - Remove generic host keys, entrypoint generates unique keys  
RUN apt-get update && \  
apt-get -y install openssh-server && \  
rm -rf /var/lib/apt/lists/* && \  
mkdir -p /var/run/sshd && \  
rm -f /etc/ssh/ssh_host_*key*  
  
# - Install packages to build s3fs and make it  
RUN apt-get update && \  
apt-get -y install automake autotools-dev g++ git libcurl4-gnutls-dev libfuse-
dev libssl-dev libxml2-dev make pkg-config  
  
RUN git clone https://github.com/s3fs-fuse/s3fs-fuse.git && \  
cd s3fs-fuse && \  
./autogen.sh && \  
./configure && \  
make && \  
make install  
  
COPY sshd_config /etc/ssh/sshd_config  
COPY entrypoint /  
COPY README.md /  
  
EXPOSE 22  
ENTRYPOINT ["/entrypoint"]  

