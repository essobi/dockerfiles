FROM tweag/stack-docker-nix  
  
ADD stack-shell.nix /shell.nix  
RUN nix-env -iA nixpkgs.bash  
RUN nix-shell /shell.nix --indirect --add-root /nix-shell-gc-root \  
&& nix-collect-garbage  
RUN nix-instantiate \  
\--add-root /shell.drv --indirect /shell.nix \  
&& nix-collect-garbage  
  
ADD entrypoint.py /  
  
RUN chmod -R a+rw /nix/var  

