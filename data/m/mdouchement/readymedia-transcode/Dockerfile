FROM base/archlinux  
MAINTAINER mdouchement  
  
ENV MINIDLNA_OPTS ''  
ENV MINIDLNA_PORT 8200  
ENV MINIDLNA_FRIENDLY_NAME 'DLNA Server'  
ENV MINIDLNA_TRANSCODE_VIDEO_TRANSCODER
/usr/share/minidlna/transcodescripts/transcode_video-hq  
  
RUN pacman --noconfirm -Sy archlinux-keyring  
RUN pacman --noconfirm -Su base-devel yajl git  
  
RUN groupadd -r yaourt  
RUN useradd -r -g yaourt yaourt  
RUN echo "yaourt ALL=NOPASSWD: ALL" >> /etc/sudoers  
RUN mkdir /tmp/yaourt  
RUN chown -R yaourt:yaourt /tmp/yaourt  
  
RUN pacman-db-upgrade  
  
WORKDIR /tmp/yaourt  
  
USER yaourt  
RUN git clone https://aur.archlinux.org/package-query.git && \  
cd package-query && \  
makepkg --noconfirm  
  
USER root  
RUN cd package-query && pacman --noconfirm -U *.pkg.tar.xz  
  
USER yaourt  
RUN git clone https://aur.archlinux.org/yaourt.git && \  
cd yaourt && \  
makepkg --noconfirm  
  
USER root  
RUN cd yaourt && pacman --noconfirm -U *.pkg.tar.xz  
  
USER yaourt  
RUN yaourt --noconfirm -S readymedia-transcode-git  
  
USER root  
RUN mkdir -p /data/{images,music,videos}  
  
WORKDIR /  
  
COPY etc/minidlna.conf /etc/minidlna.conf  
COPY entrypoint.sh /entrypoint.sh  
  
VOLUME /data  
EXPOSE 8200  
CMD /entrypoint.sh  

