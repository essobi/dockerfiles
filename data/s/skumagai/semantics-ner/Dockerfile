FROM greyltc/archlinux  
RUN useradd -ms /bin/sh nc_semantics && \  
pacman -Suyy \--noconfirm \--noprogressbar && \  
pacman -S \--noconfirm \--noprogressbar \--needed python uwsgi-plugin-python
git binutils \  
make yajl gcc fakeroot expac sudo automake pkg-config \  
python-pip cython && \  
sed -i s/lecture=once/lecture=never/ /etc/sudoers && \  
echo "ALL ALL = (ALL) NOPASSWD: ALL" >> /etc/sudoers && \  
cd /home/nc_semantics && \  
su nc_semantics -c "git clone https://aur.archlinux.org/cower.git" && \  
su nc_semantics -c "gpg --recv-keys --keyserver hkp://pgp.mit.edu
1EB2638FF56C0C53" && \  
cd cower && \  
su nc_semantics -c "makepkg --noconfirm" && \  
pacman -U \--noconfirm \--noprogressbar \--needed cower*.pkg.tar.xz && \  
cd .. && \  
su nc_semantics -c "git clone https://aur.archlinux.org/pacaur.git" && \  
cd pacaur && \  
su nc_semantics -c "makepkg --noconfirm" && \  
pacman -U \--noconfirm \--noprogressbar \--needed pacaur*.pkg.tar.xz && \  
cd .. && \  
rm -rf cower pacaur && \  
su nc_semantics -c "pacaur -S --noedit --noconfirm --needed --noprogressbar
frog" && \  
pip install \--no-cache-dir python-frog flask && \  
pacman -Rsc \--noconfirm git binutils make yajl gcc fakeroot expac sudo
automake pkg-config \  
python-pip cython pacaur && \  
yes | pacman -Scc  
  
WORKDIR /etc/uwsgi  
COPY ner.py ner.ini /etc/uwsgi/  
  
  
ENTRYPOINT ["uwsgi", "--ini", "/etc/uwsgi/ner.ini"]  

