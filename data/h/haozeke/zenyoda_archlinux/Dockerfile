# Use the latest arch with base-devel  
FROM base/devel  
  
# By Rohit Goswami  
LABEL maintainer="Rohit Goswami <rohit.1995@mail.ru>"  
LABEL name="zenYoda"  
# Update apt and get build reqs  
RUN pacman-key --refresh-keys && pacman-key -r 753E0F1F && pacman-key --lsign-
key 753E0F1F && pacman -Syy  
RUN pacman --noconfirm -S python-pip texlive-most yarn tup pandoc pandoc-
citeproc sassc git biber openssh  
  
# Add archLinuFr  
RUN echo -e "\n[archlinuxfr]\nSigLevel = Never\nServer =
http://repo.archlinux.fr/\$arch" >> /etc/pacman.conf  
  
# Get yaourt  
RUN pacman --noconfirm -Syy yaourt  
  
# Switch to the new user by default and make ~/ the working dir  
ENV USER zenyoda  
# WORKDIR /home/${USER}/  
# Add the build user, update password to build and add to sudo group  
RUN useradd --create-home ${USER} && echo "${USER}:${USER}" | chpasswd &&
usermod -aG wheel ${USER}  
RUN echo "${USER} ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers  
  
# Use ccache by default  
ENV USE_CCACHE 1  
  
# Fix permissions on home  
RUN chown -R ${USER}:${USER} /home/${USER}  
RUN sudo -u ${USER} mkdir -p /home/${USER}/aur  
  
# Switch to ${USER}  
# USER ${USER}  
RUN whoami  
  
# Extras  
RUN sudo pip install panflute pandoc-eqnos pandoc-fignos  
RUN yarn global add surge  
  
# Setup dummy git config  
RUN git config \--global user.name "${USER}" && git config \--global
user.email "${USER}@localhost"

