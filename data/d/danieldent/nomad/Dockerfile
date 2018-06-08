FROM debian:jessie  
RUN DEBIAN_FRONTEND=noninteractive apt-get update -q \  
&& DEBIAN_FRONTEND=noninteractive apt-get dist-upgrade -y \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y wget unzip libvirt-bin
qemu-kvm bridge-utils \  
&& cd / \  
&& wget
'https://releases.hashicorp.com/nomad/0.2.3/nomad_0.2.3_linux_amd64.zip' \  
&& echo "0f3a7083d160893a291b5f8b4359683c2df7991fa0a3e969f8785ddb40332a8c
nomad_0.2.3_linux_amd64.zip"|shasum -c \  
&& unzip nomad_0.2.3_linux_amd64.zip \  
&& rm nomad_0.2.3_linux_amd64.zip \  
&& chmod +x nomad \  
&& wget https://apt.dockerproject.org/gpg \  
&& echo "c836dc13577c6f7c133ad1db1a2ee5f41ad742d11e4ac860d8e658b2b39e6ac1 gpg"
| sha256sum -c \  
&& apt-key add gpg \  
&& rm gpg \  
&& echo "deb http://apt.dockerproject.org/repo debian-jessie main" >
/etc/apt/sources.list.d/docker.list \  
&& DEBIAN_FRONTEND=noninteractive apt-get update -q \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y docker-
engine=1.9.1-0~jessie \  
&& DEBIAN_FRONTEND=noninteractive apt-get autoremove -y curl unzip \  
&& rm -Rf /var/lib/apt /var/cache/apt  
EXPOSE 4646  
EXPOSE 4647  
EXPOSE 4648  
EXPOSE 4648/UDP  
VOLUME "/workdir"  
WORKDIR "/workdir"  
ENTRYPOINT ["/nomad"]

