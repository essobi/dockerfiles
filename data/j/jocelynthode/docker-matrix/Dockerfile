## We need to install gnupg to import the repo key  
FROM debian:stretch-slim as keyring  
RUN export DEBIAN_FRONTEND=noninteractive \  
&& apt-get update -qq \  
&& apt-get install -yq gnupg \  
&& rm -rf /var/lib/apt/lists/*  
COPY adds/matrix-repo-key.asc /  
## equivalent to RUN apt-key --keyring /matrix.gpg add /matrix-repo-key.asc  
RUN touch /matrix.gpg && gpg --no-default-keyring --keyring /matrix.gpg \  
\--quiet --import /matrix-repo-key.asc  
  
FROM debian:stretch-slim  
  
## setup repository  
COPY \--from=keyring /matrix.gpg /etc/apt/trusted.gpg.d/  
RUN echo 'deb http://matrix.org/packages/debian/ stretch main' \  
> /etc/apt/sources.list.d/matrix.list  
  
## install latest version of matrix  
RUN export DEBIAN_FRONTEND=noninteractive \  
&& apt-get update -qq \  
&& apt-get install -yq --no-install-recommends \  
dumb-init \  
matrix-synapse \  
## Suggested deps for email notifications \  
# python-bleach python-jinja2 \  
&& rm -rf /var/lib/apt/lists/*  
RUN dpkg-query --show -f '${Version}' matrix-synapse >/synapse.version  
  
## user configuration  
ENV MATRIX_UID=991 MATRIX_GID=991  
RUN groupadd -r -g $MATRIX_GID matrix \  
&& useradd -r -d /data -M -u $MATRIX_UID -g matrix matrix  
  
## startup configuration  
COPY adds/entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["python", "-m", "synapse.app.homeserver", "-c", "/data/conf/matrix-
server.yaml"]  
USER matrix  
EXPOSE 8448  
VOLUME ["/data"]  

