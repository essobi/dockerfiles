FROM ubuntu:16.04 as downloader  
LABEL maintainer "Corey Ryan Hanson"  
#This is a modified version of the dind dockerfile https://github.com/docker-
library/docker/blob/b9fd686dac473fb71ffb426a9ef8e0467208dd2f/17.12/Dockerfile#L51
to run using the CUDA images from NVIDIA as a base.  
#Installs dependencies.  
RUN export DEBIAN_FRONTEND=noninteractive && apt-get update && apt-get install
-y \  
ca-certificates \  
curl \  
tar \  
git && \  
rm -rf /var/lib/apt/lists/*  
  
RUN git clone https://github.com/docker-library/docker.git  
  
ENV DOCKER_CHANNEL stable  
ENV DOCKER_VERSION 17.12.0-ce  
ENV DOCKER_VERSION_SHORT 17.12  
# this "case" statement is generated via "update.sh"  
RUN apkArch="$(uname -m)"; \  
case "$apkArch" in \  
x86_64) dockerArch='x86_64' ;; \  
armhf) dockerArch='armel' ;; \  
aarch64) dockerArch='aarch64' ;; \  
ppc64le) dockerArch='ppc64le' ;; \  
s390x) dockerArch='s390x' ;; \  
*) echo >&2 "error: unsupported architecture ($apkArch)"; exit 1 ;;\  
esac; \  
\  
if ! curl -fL -o docker.tgz
"https://download.docker.com/linux/static/${DOCKER_CHANNEL}/${dockerArch}/docker-${DOCKER_VERSION}.tgz";
then \  
echo >&2 "error: failed to download 'docker-${DOCKER_VERSION}' from
'${DOCKER_CHANNEL}' for '${dockerArch}'"; \  
exit 1; \  
fi; \  
\  
tar --extract \  
\--file docker.tgz \  
\--strip-components 1 \  
\--directory /usr/local/bin/ \  
; \  
dockerd -v; \  
docker -v  
  
RUN cp /docker/${DOCKER_VERSION_SHORT}/modprobe.sh /usr/local/bin/modprobe &&
\  
cp /docker/${DOCKER_VERSION_SHORT}/docker-entrypoint.sh /usr/local/bin/  
  
#Begins stage2 of image.  
FROM ubuntu:16.04  
#Copies files that were extracted from stage 1.  
COPY \--from=downloader /usr/local/bin/ /usr/local/bin/  
  
ENTRYPOINT ["docker-entrypoint.sh"]  
CMD ["bash"]  

