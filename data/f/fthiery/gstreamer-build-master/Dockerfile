FROM archlinux/base  
  
WORKDIR /root  
  
ADD . /root  
  
RUN pacman -Sy --noconfirm --needed \  
python-gobject gobject-introspection \  
gstreamer gstreamer-vaapi gst-plugins-base gst-plugins-good gst-plugins-bad
gst-python \  
ttf-freefont \  
libva-utils \  
libva-intel-driver \  
git base-devel gtk-doc meson ninja  
  
# makepkg will only run as user, not root  
RUN echo "nobody ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/nobody  
RUN mkdir -p /home/nobody/build && chown -R nobody: /home/nobody  
USER nobody  
ENV HOME=/home/nobody  
ENV EDITOR=/bin/true  
WORKDIR /home/nobody  
  
USER root  
RUN cp /root/install-aur-deps.sh /home/nobody  
  
# install extra deps from AUR  
RUN chown nobody /home/nobody/install-aur-deps.sh  
USER nobody  
RUN /home/nobody/install-aur-deps.sh  
  
# build gstreamer  
USER root  
RUN /root/gst-build.sh  

