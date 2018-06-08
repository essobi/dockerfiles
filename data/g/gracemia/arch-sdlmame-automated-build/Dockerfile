FROM base/archlinux:2017.09.01  
RUN pacman -Sy  
RUN pacman -S --noconfirm sdlmame  
RUN pacman -Scc --noconfirm  
COPY mame.ini /root/.mame/mame.ini  
ENTRYPOINT ["/usr/sbin/sdlmame"]  

