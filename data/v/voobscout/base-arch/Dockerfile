FROM base/archlinux:latest  
MAINTAINER Voobscout <voobscout@archlinux.info>  
  
ENV container docker  
ENV TERM screen  
  
ONBUILD RUN bash -c "export COUNTRY=$(curl http://country.io/names.json 2>
/dev/null | jq -r .$(curl ipinfo.io/$(dig +short myip.opendns.com
@resolver1.opendns.com)/country 2> /dev/null)); awk -v GG=\${COUNTRY}
'{if(match(\$0,GG) != 0)AA=1;if(AA == 1){if( length(\$2) != 0 )print
substr(\$0,2) ;else AA=0} }' <(curl
https://www.archlinux.org/mirrorlist/?country=all&protocol=http&protocol=https&ip_version=4)
> $HOME/mirrors_\${COUNTRY} && rankmirrors -n 0 $HOME/mirrors_\${COUNTRY} >
/etc/pacman.d/mirrorlist"  
  
RUN pacman --noconfirm -Syyu sed grep jq bind-tools  
RUN bash -c "export COUNTRY=$(curl http://country.io/names.json 2> /dev/null |
jq -r .$(curl ipinfo.io/$(dig +short myip.opendns.com
@resolver1.opendns.com)/country 2> /dev/null)); awk -v GG=\${COUNTRY}
'{if(match(\$0,GG) != 0)AA=1;if(AA == 1){if( length(\$2) != 0 )print
substr(\$0,2) ;else AA=0} }' <(curl
https://www.archlinux.org/mirrorlist/?country=all&protocol=http&protocol=https&ip_version=4)
> $HOME/mirrors_\${COUNTRY} && rankmirrors -n 0 $HOME/mirrors_\${COUNTRY} >
/etc/pacman.d/mirrorlist"  
  
RUN sed -i '/#\[multilib\]/,/#Include = \/etc\/pacman.d\/mirrorlist/ s/#//'
/etc/pacman.conf && \  
pacman --force --noconfirm --needed -Syyu \  
base-devel \  
git \  
iproute2 \  
ncurses \  
ruby \  
vim \  
zsh \  
python-pip \  
openssl \  
sudo && \  
pacman --force --noconfirm -Scc && \  
sed -i 's/#MAKEFLAGS="-j2"/MAKEFLAGS="-j$(($(nproc)*2))"/' /etc/makepkg.conf
&& \  
sed -i 's/xz /xz -T0 /' /etc/makepkg.conf && \  
sed -i "s/#Color/Color/" /etc/pacman.conf && \  
pip install dumb-init && \  
chmod +x /usr/bin/dumb-init && \  
useradd -m -u 1000 -G wheel,video,audio -s /bin/zsh dev && \  
echo "%wheel ALL=(ALL) NOPASSWD: ALL, SETENV: ALL" > /etc/sudoers.d/10-admins  
  
RUN runuser -l dev -c 'cd $HOME && \  
mkdir -p yaourt-src && \  
cd yaourt-src && \  
git clone https://aur.archlinux.org/package-query.git && \  
git clone https://aur.archlinux.org/yaourt.git && \  
cd package-query && \  
makepkg --noconfirm -si && \  
cd ../yaourt && \  
makepkg --noconfirm -si && \  
cd $HOME && \  
rm -rf $HOME/yaourt-src && \  
mkdir -p $HOME/tmp/yaourt && \  
echo "TMPDIR=$HOME/tmp/yaourt" > ~/.yaourtrc && \  
echo "UP_NOCONFIRM=1" >> ~/.yaourtrc && \  
echo "BUILD_NOCONFIRM=1" >> ~/.yaourtrc && \  
echo "PU_NOCONFIRM=1" >> ~/.yaourtrc && \  
echo "EDITFILES=0" >> ~/.yaourtrc' && \  
runuser -l dev -c "yaourt --noconfirm -S localepurge" && \  
runuser -l dev -c 'bash -c "$(wget
https://raw.githubusercontent.com/robbyrussell/oh-my-
zsh/master/tools/install.sh -O -)" && \  
git clone https://github.com/nojhan/liquidprompt.git ~/.liquidprompt' && \  
echo '[ ! $TERM = "dumb" ] && [[ $\- = *i* ]] && .
~/.liquidprompt/liquidprompt' >> /home/dev/.zshrc && \  
echo '[[ -z $STY ]] && export LP_PS1_POSTFIX="¬» " || export
LP_PS1_POSTFIX="§» "' >> /home/dev/.zshrc && \  
chown dev:users /home/dev/.zshrc && \  
sed -i "s/NEEDSCONFIGFIRST/#NEEDSCONFIGFIRST/" /etc/locale.nopurge && \  
sed -i "s/#DONTBOTHERNEWLOCALE/DONTBOTHERNEWLOCALE/" /etc/locale.nopurge && \  
find /var/cache/pacman/pkg -mindepth 1 -delete  
  
ENTRYPOINT ["/usr/bin/dumb-init"]  
CMD ["/bin/bash", "-l"]  

