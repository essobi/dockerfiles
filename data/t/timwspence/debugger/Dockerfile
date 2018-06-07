FROM base/archlinux  
  
RUN pacman -Syyu --noconfirm && \  
pacman -S curl traceroute nload mtr netdata tcpdump wireshark-cli nmap ngrep
lsof strace htop --noconfirm && \  
pacman -Scc --noconfirm  
  
CMD ["bash"]  

