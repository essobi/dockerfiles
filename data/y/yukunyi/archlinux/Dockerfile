FROM base/archlinux  
RUN curl -o /etc/pacman.d/mirrorlist
"https://www.archlinux.org/mirrorlist/?country=all&protocol=https&ip_version=4&use_mirror_status=on"
&& \  
sed -i 's/^#//' /etc/pacman.d/mirrorlist  
  
ONBUILD RUN cp -af /etc/pacman.d/mirrorlist /etc/pacman.d/mirrorlist.backup &&
\  
rankmirrors -n 6 /etc/pacman.d/mirrorlist.backup > /etc/pacman.d/mirrorlist &&
(\  
cat /etc/pacman.d/mirrorlist | \  
sed '/^#/d' | \  
sed '/^$/d' | \  
cut -d ' ' -f 3 \  
)  
ONBUILD RUN pacman -Sy --noconfirm && \  
pacman -S pacman --noconfirm && \  
pacman-db-upgrade && \  
pacman -Syyu --noconfirm  

