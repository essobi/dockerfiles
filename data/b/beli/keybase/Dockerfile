FROM debian:testing  
MAINTAINER Michal Belica <devel@beli.sk>  
RUN useradd -m -d /home/user user \  
&& apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y curl gnupg less vim \  
# download and check code signing key  
&& curl https://keybase.io/docs/server_security/code_signing_key.asc | gpg
--import \  
&& gpg --fingerprint 222B85B0F90BE2D24CFEB93F47484E50656D16C7 \  
# download and verify keybase package  
&& curl -o /home/user/keybase_amd64.deb
https://prerelease.keybase.io/keybase_amd64.deb \  
&& curl -o /home/user/keybase_amd64.deb.sig
https://prerelease.keybase.io/keybase_amd64.deb.sig \  
&& gpg --verify /home/user/keybase_amd64.deb.sig /home/user/keybase_amd64.deb
\  
# install keybase package  
&& dpkg --force-depends -i /home/user/keybase_amd64.deb \  
# fix package dependencies  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y -f \  
# cleanup  
&& apt-get clean && rm -rf /var/lib/apt/lists/* \  
&& rm -rf ~/.gnupg \  
&& rm -f /home/user/keybase_amd64.deb /home/user/keybase_amd64.deb.sig \  
# create /config volume linked to /home/user/.config/keybase  
&& mkdir /home/user/.config \  
&& mkdir /config \  
&& ln -s /config /home/user/.config/keybase \  
&& chown -hR user: /config /home/user/.config \  
# create /gnupg volume linked to /home/user/.gnupg  
&& mkdir /gnupg \  
&& ln -s /gnupg /home/user/.gnupg \  
&& chown -h user: /gnupg /home/user/.gnupg  
VOLUME /config  
VOLUME /gnupg  
USER user  
ENV HOME /home/user  
ENV USER user  
WORKDIR /home/user  
CMD ["/usr/bin/keybase", "ctl", "watchdog"]  

