FROM folsomlabs/base  
  
RUN adduser --disabled-password --gecos '' produser  
RUN mkdir -m 0755 /nix && chown produser /nix  
  
USER produser  
ENV USER produser  
WORKDIR /home/produser  
  
# FIXME(ben): I hate curl|sh. At least it's https.  
RUN curl https://nixos.org/nix/install | sh \  
&& . /home/produser/.profile \  
&& nix-env -u \  
&& nix-collect-garbage --delete-old \  
&& nix-store --optimise  
  
# I can't tell if setting ENV= actually has any effect.  
ENV ENV /home/produser/.profile  
ONBUILD ENV ENV /home/produser/.profile  
  
ENV PATH /home/produser/.nix-profile/bin:/home/produser/.nix-
profile/sbin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin  
ENV NIX_PATH nixpkgs=/home/produser/.nix-defexpr/channels/nixpkgs  
  
# Help various things find the system CA cert store, including our internal CA  
ENV SSL_CERT_FILE /etc/ssl/certs/ca-certificates.crt  
ENV CURL_CA_BUNDLE /etc/ssl/certs/ca-certificates.crt  
ENV GIT_SSL_CAINFO /etc/ssl/certs/ca-certificates.crt  
ENV OPENSSL_X509_CERT_FILE /etc/ssl/certs/ca-certificates.crt  

