FROM pritunl/archlinux:latest  
  
RUN echo >> ~/.gnupg/dirmngr_ldapservers.conf && \  
printf "[archstrike]\nServer = https://mirror.archstrike.org/\$arch/\$repo\n"
>> /etc/pacman.conf;  
  
RUN NUM=$(awk '/#\\[multilib\\]/{print NR}' /etc/pacman.conf) && \  
NUMP1=$(expr $NUM \+ 1) && \  
SEDSTRING=$(echo $NUM","$NUMP1"s/^#//") && \  
sed -i $SEDSTRING /etc/pacman.conf && \  
unset NUM NUMP1 SEDSTRING;  
  
RUN pacman -Syy && \  
pacman-key --init && \  
dirmngr < /dev/null && \  
pacman-key -r 9D5F1C051D146843CDA4858BDE64825E7CBC0D51 && \  
pacman-key --lsign-key 9D5F1C051D146843CDA4858BDE64825E7CBC0D51 && \  
pacman -S --noconfirm archstrike-keyring archstrike-mirrorlist man-db iproute2
vim;  
  
RUN printf "$(head -n -2 /etc/pacman.conf)\n[archstrike]\nInclude =
/etc/pacman.d/archstrike-mirrorlist\n" > /etc/pacman.conf && \  
pacman -Syyu;  
  
CMD ["/bin/bash"]  

