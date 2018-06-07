FROM nixos/nix:1.11  
MAINTAINER Jordan Cran jordan@instantepiphany.com.au  
  
RUN nix-channel --add https://nixos.org/channels/nixpkgs-unstable nixpkgs  
RUN nix-channel --update  
  
RUN nix-env --install yarn  
RUN nix-env --install wget  
RUN nix-env --install nodejs  
  
RUN wget https://github.com/barnybug/s3/releases/download/1.1.4/s3-linux-amd64
\  
&& mv s3-linux-amd64 s3 && chmod +x s3 && mv s3 /usr/local/bin/s3  
  
CMD [ "/bin/bash" ]  

