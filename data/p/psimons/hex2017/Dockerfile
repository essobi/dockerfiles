FROM alpine  
  
# Enable HTTPS support in wget.  
RUN apk add \--update openssl  
  
# Download Nix and install it into the system.  
RUN wget -O-
https://nixos.org/releases/nix/nix-1.11.14/nix-1.11.14-x86_64-linux.tar.bz2 |
bzcat - | tar xf - \  
&& addgroup -g 30000 -S nixbld \  
&& for i in $(seq 1 30); do adduser -S -D -h /var/empty -g "Nix build user $i"
-u $((30000 + i)) -G nixbld nixbld$i ; done \  
&& mkdir -m 0755 /nix && USER=root sh nix-*-x86_64-linux/install \  
&& ln -s /nix/var/nix/profiles/default/etc/profile.d/nix.sh /etc/profile.d/ \  
&& rm -r /nix-*-x86_64-linux \  
&& rm -r /var/cache/apk/* \  
&& echo >>/etc/profile
'GIT_SSL_CAINFO=/nix/var/nix/profiles/default/etc/ssl/certs/ca-bundle.crt' \  
&& echo >>/etc/profile
'SSL_CERT_FILE=/nix/var/nix/profiles/default/etc/ssl/certs/ca-bundle.crt' \  
&& echo >>/etc/profile
'NIX_SSL_CERT_FILE=/nix/var/nix/profiles/default/etc/ssl/certs/ca-bundle.crt'
\  
&& echo >>/etc/profile
'SYSTEM_CERTIFICATE_PATH=/nix/var/nix/profiles/default/etc/ssl/certs/ca-
bundle.crt' \  
&& echo >>/etc/profile 'export GIT_SSL_CAINFO SSL_CERT_FILE NIX_SSL_CERT_FILE
SYSTEM_CERTIFICATE_PATH' \  
&& . /etc/profile \  
&& nix-channel \--add https://nixos.org/channels/nixos-17.09 nixpkgs \  
&& nix-channel \--update \  
&& echo >>/etc/profile export NIX_PATH=nixpkgs=/nix/var/nix/profiles/per-
user/root/channels/nixpkgs/nixpkgs \  
&& rm -r ~/.nix-defexpr \  
&& ln -s /nix/var/nix/profiles/per-user/root/channels/nixpkgs/nixpkgs ~/.nix-
defexpr \  
&& nix-env -u \--always \  
&& nix-env -iA bash-completion bashInteractive coreutils curl wget \  
&& echo >>/etc/shells /nix/var/nix/profiles/default/bin/bash \  
&& echo >>/etc/profile 'test -z "${BASH_VERSION:-}" || . /etc/bash.bashrc' \  
&& echo >>/etc/bash.bashrc BASH_COMPLETION_COMPAT_DIR=~/.nix-
profile/etc/bash_completion.d \  
&& echo >>/etc/bash.bashrc 'test -z "${PS1:-}" || . ~/.nix-profile/share/bash-
completion/bash_completion' \  
&& chmod -R ugo-w /nix/store/* \  
&& nix-collect-garbage \--delete-old \  
&& nix-store \--optimise  
# Set up a basic Haskell development environment.  
RUN . /etc/profile \  
&& nix-env -iA \  
binutils \  
cabal-install \  
cabal2nix \  
dnsutils \  
gcc \  
ghc \  
haskellPackages.alex \  
haskellPackages.happy \  
pkgconfig \  
stack \  
&& nix-store \--optimise  
  
WORKDIR /root  
CMD ["/nix/var/nix/profiles/default/bin/bash", "--login", "-i"]  

