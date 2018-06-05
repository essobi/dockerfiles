FROM finalduty/archlinux  
RUN curl -o /etc/pacman.d/mirrorlist
"https://www.archlinux.org/mirrorlist/?country=all&protocol=https&ip_version=6&use_mirror_status=on"
&& \  
sed -i 's/^#//' /etc/pacman.d/mirrorlist  
#RUN pacman -Syu --force openssl --noconfirm  
RUN pacman -Syu bash-completion vim bind-tools net-tools openssl lsof gnu-
netcat tcpdump --noconfirm  
RUN pacman -Syu --noconfirm  

