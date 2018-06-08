# Edit FROM line to something else based on Archlinux if you want it to run on
other architectures. (eg yyolk/rpi-archlinuxarm for ARMv6)  
FROM base/archlinux  
  
# Pacman fixes  
RUN pacman -Sy --noconfirm  
RUN pacman -S --noconfirm --needed archlinux-keyring  
RUN pacman -S --noconfirm --needed openssl pacman  
RUN pacman-db-upgrade  
  
# Install Java  
RUN pacman -S --noconfirm --needed jre8-openjdk-headless wget git  
  
# Pacman breaks again... wget needs to be installed alongside with ca-
certificates thingy  
# Clean up cache  
RUN pacman -Scc --noconfirm  
RUN rm -rf /var/cache/pacman/pkg  
  
# Add Minecraft user  
RUN useradd -m -g users -s /bin/bash -m -d /minecraft minecraft  
RUN chown -R minecraft:users /minecraft  
  
# Add build and init script  
ADD startServer.sh /  
  
RUN chmod +x /startServer.sh  
  
# Switch to Minecraft user  
USER minecraft  
  
ENTRYPOINT ["/bin/bash", "-c", "/startServer.sh"]

