FROM nixos/nix  
  
MAINTAINER jaka@gatehub.net  
  
RUN nix-env -iA nixpkgs.docker nixpkgs.kubernetes -j $(grep -c ^processor
/proc/cpuinfo)  
RUN nix-env -f https://github.com/xtruder/nix-
kubernetes/archive/v0.25.0.tar.gz -iA package -j $(grep -c ^processor
/proc/cpuinfo)  

