FROM buzzy/build-arch  
  
RUN curl -O http://public.redjack.com/arch/buzzy-0.5.1-1-x86_64.pkg.tar.xz \  
&& curl -O http://public.redjack.com/arch/buzzy-
debug-0.5.1-1-x86_64.pkg.tar.xz \  
&& sudo pacman -U --noconfirm buzzy-*.tar.xz \  
&& rm buzzy-*.tar.xz \  
&& mkdir -p /home/buzzy/.cache/buzzy  

