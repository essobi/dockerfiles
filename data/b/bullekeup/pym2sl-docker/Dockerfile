#  
# pyM2SL container based on Archlinux  
# based on devel image w/ packer installed  
#  
# This is a development image, not a production one !  
#  
FROM base/devel  
  
# Set base env vars  
ENV TERM vt100  
  
# Install packer  
RUN pacman -Sy --noconfirm pacman package-query && pacman-db-upgrade  
RUN pacman -Sy --noconfirm archlinux-keyring; pacman -Su --noconfirm base-
devel git rsync strace curl ca-certificates ca-certificates-utils  
RUN pacman -Sy --noconfirm ncurses bash-completion  
  
# TODO: add zsh support  
#RUN pacman -Sy --noconfirm zsh  
# Add an user to build and run tests  
RUN useradd -G users,wheel -m -s /bin/bash devuser && \  
su devuser -c "mkdir /home/devuser/{build,export}"  
  
WORKDIR /home/devuser/build  
  
# Install python3 + libnl + zeromq + gstreamer  
RUN pacman -Sy --noconfirm python python-pip python-gobject python-gobject2
libnl zeromq gstreamer gst-python libpgm  
  
# Install pyzmq and libnl python bindings  
RUN pip install --no-use-wheel pyzmq && pip install libnl  
  
# Fetch and install custom opencv with gstreamer support  
RUN pacman -Sy --noconfirm gst-libav gst-plugins-bad gst-plugins-base gst-
plugins-base-libs gst-plugins-good gst-plugins-ugly gstreamer-vaapi
qt5-gstreamer  
RUN curl -LO https://github.com/bullekeup/arch-
packages/releases/download/opencv-gstreamer-v0.1-beta.2/opencv-
gstreamer-3.1.0-3-x86_64.pkg.tar.xz && \  
curl -LO https://github.com/bullekeup/arch-packages/releases/download/opencv-
gstreamer-v0.1-beta.2/opencv-gstreamer-samples-3.1.0-3-x86_64.pkg.tar.xz && \  
pacman -U --noconfirm opencv-gstreamer-3.1.0-3-x86_64.pkg.tar.xz && \  
pacman -U --noconfirm opencv-gstreamer-samples-3.1.0-3-x86_64.pkg.tar.xz  
  
RUN rm /var/cache/pacman/pkg/* && rm ./*.pkg.tar.xz  
RUN mkdir -p /home/workspace/{tools,src,export}  
  
RUN pacman -Sy --noconfirm libgphoto2  
RUN pacman -Sy --noconfirm gtk3 qt5-x11extras  
RUN pacman -Sy --noconfirm libglvnd mesa-vdpau libva-mesa-driver  
RUN pacman -Sy --noconfirm ttf-droid noto-fonts noto-fonts-cjk noto-fonts-
emoji font-bh-ttf sdl2_ttf sdl_ttf \  
ttf-bitstream-vera ttf-dejavu ttf-freefont ttf-linux-libertine ttf-liberation
ttf-ubuntu-font-family  
  
# Copy pym2sl updater  
WORKDIR /home/workspace  
USER devuser  
CMD ["/bin/bash"]  
EXPOSE 4000-5000  

