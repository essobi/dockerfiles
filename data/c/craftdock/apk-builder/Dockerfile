FROM alpine:3.7  
LABEL maintainer="Hexosse <hexosse@gmail.com>" \  
description="Create your own packages."  
  
ENV PACKAGER "Hexosse <hexosse@gmail.com>"  
ENV RSA_PRIVATE_KEY_NAME key.rsa  
ENV PACKAGER_PRIVKEY /package/ssh/${RSA_PRIVATE_KEY_NAME}  
ENV PACKAGER_PUBKEY /package/ssh/${RSA_PRIVATE_KEY_NAME}.pub  
  
RUN \  
# Create builder user member of group abuild  
adduser -D -s /bin/ash -G abuild -g "Alpine Package Builder" builder \  
# Make our builder user like sudo  
&& echo "builder ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers  
  
RUN \  
# Print executed commands  
set -x \  
# Update repository indexes  
&& apk update --update-cache \  
# Install latest versions of packages included in alpine-sdk  
&& apk add \  
# alpine-sdk: abuild build-base git squashfs-tools xorriso acct mkinitfs
mtools  
abuild git squashfs-tools xorriso acct mkinitfs mtools \  
# build-base: binutils file gcc g++ make libc-dev fortify-headers  
binutils file gcc g++ make libc-dev fortify-headers \  
# Just in case of new packages  
alpine-sdk \  
# common tools  
cmake coreutils curl go govendor \  
# Clear apk's cache  
&& rm -rf /var/cache/apk/* /tmp/* /var/tmp/*  
  
# Copy entrypoint script  
COPY /entrypoint /  
  
# Entrypoint  
ENTRYPOINT ["/entrypoint"]  
  
# Set default user to builder  
USER builder  
  
# Default command  
CMD ["abuild", "-r", "-P", "/packages"]  
  
# All can be found in the builder folder  
VOLUME ["/packages"]  

