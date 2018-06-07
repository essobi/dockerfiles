FROM debian:jessie  
  
ENV GNUPGHOME=/app/.gnupg  
  
COPY * /app/  
  
RUN ( \  
export DEBIAN_FRONTEND=noninteractive; \  
BUILD_DEPS=""; \  
APP_DEPS="ca-certificates s3cmd gawk"; \  
# so that each command can be seen clearly in the build output  
set -e -x; \  
# update to pull package list from apt sources  
apt-get update; \  
apt-get install --no-install-recommends -y $BUILD_DEPS $APP_DEPS ; \  
# If this container is run as any user other than root, GNUPGHOME would need
different ownership. At run time this  
# can to an extend be resolved by using a 'tmpfs' mount, which can take 'uid'
option.  
mkdir -p "$GNUPGHOME" && chmod go-rwx "$GNUPGHOME"; \  
# remove packages that we don't need  
[ -z "$BUILD_DEPS" ] || apt-get remove -y $BUILD_DEPS; \  
apt-get autoremove -y ; \  
apt-get clean; \  
rm -rf /var/lib/apt/* /var/lib/dpkg/* /var/lib/cache/* /var/lib/log/*; \  
)  
  
WORKDIR /app  
  
ENTRYPOINT [ "/app/entrypoint.sh" ]  
CMD [ "backup" ]  

