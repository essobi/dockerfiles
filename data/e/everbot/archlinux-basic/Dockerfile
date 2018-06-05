# Build with:  
# docker build --rm -t everbot/archlinux-basic .  
# Run with:  
# docker run -ti --restart always --name ltt-arch -v $(pwd):/data
everbot/archlinux-basic  
FROM everbot/archlinux  
MAINTAINER everbot  
  
ADD mirrorlist /etc/pacman.d/  
RUN chmod 644 /etc/pacman.d/mirrorlist  
  
RUN pacman -Syy && \  
pacman --noconfirm -Syu  
  
RUN pacman --noconfirm -S base-devel \  
git vim ruby python \  
the_silver_searcher \  
tmux zsh ranger ttf-dejavu  
  
# fix key repetition when running tmux  
RUN pacman --noconfirm -S rxvt-unicode  
  
RUN useradd -m -g users -s /bin/zsh tung && \  
echo "tung ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers && \  
sed -i '/Defaults requiretty/d' /etc/sudoers  
  
USER tung  
  
# install `package-query`  
RUN mkdir ~/Downloads && \  
cd ~/Downloads && \  
curl -O https://aur.archlinux.org/cgit/aur.git/snapshot/package-query.tar.gz
&& \  
tar xzvf package-query.tar.gz && \  
cd package-query && \  
makepkg -sri --noconfirm  
  
# install `yaourt`  
RUN cd ~/Downloads && \  
curl -O https://aur.archlinux.org/cgit/aur.git/snapshot/yaourt.tar.gz && \  
tar xzvf yaourt.tar.gz && \  
cd yaourt && \  
makepkg -sri --noconfirm  
  
ADD bootstrap.sh /home/tung/bootstrap.sh  
RUN sudo chown tung:users /home/tung/bootstrap.sh && chmod a+rx
/home/tung/bootstrap.sh  
  
# dotfiles stuff  
RUN mkdir ~/dev  
RUN cd ~/dev/ && \  
git clone http://github.com/tungel/mylinux && \  
cd mylinux && \  
bash setup.sh  
  
# for Neovim  
RUN sudo pacman --noconfirm -S neovim python-pip  
RUN pip3 install --user neovim  
  
CMD ["/home/tung/bootstrap.sh", "-zsh"]  
  

