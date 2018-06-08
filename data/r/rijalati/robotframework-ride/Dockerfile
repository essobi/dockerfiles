from base/arch  
  
MAINTAINER rijalati@gmail.com  
  
RUN [ -d /etc/pacman.d ] || mkdir -p /etc/pacman.d  
  
RUN pacman -Syy  
RUN pacman -S --noconfirm archlinux-keyring  
RUN pacman -Syu -y --needed --noconfirm --force  
RUN pacman-db-upgrade  
RUN pacman -Syu --noconfirm --needed \  
base-devel \  
python2 \  
wxgtk2.8 \  
curl \  
git \  
wxpython2.8 \  
bash \  
python2-pip \  
xorg-xauth \  
xorg-fonts \  
xorg-fonts-75dpi \  
xorg-fonts-100dpi \  
firefox \  
emacs-nox \  
vim \  
vim-plugins \  
sudo  
  
RUN pip2 install \  
Paver \  
robotframework \  
robotframework-tools \  
robotframework-rfdoc \  
robotframework-selenium2library \  
robotframework-selenium2screenshots \  
robotframework-sshlibrary \  
robotframework-hub \  
robotframework-lint \  
robotframework-pageobjects \  
robotframework-pycurllibrary \  
robotframework-httplibrary \  
sphinxcontrib-robotframework \  
Pygments \  
jedi \  
pep8 \  
pylint \  
pyflakes \  
requests \  
rope  
  
RUN useradd -m -G wheel -U admin  
RUN echo 'admin:secret' | chpasswd  
RUN echo 'admin ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers  
  
#RUN chown -R admin:admin /RIDE  
USER admin  
RUN git clone https://github.com/robotframework/RIDE.git /home/admin/RIDE  
ENV HOME /home/admin  
WORKDIR /home/admin/RIDE  
CMD ["/usr/bin/paver", "run"]  
  

