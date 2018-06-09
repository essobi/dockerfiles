FROM base/archlinux  
MAINTAINER mdouchement  
  
RUN pacman --noconfirm -Sy archlinux-keyring  
RUN pacman --noconfirm -Su base-devel yajl git  
  
RUN groupadd -r yaourt  
RUN useradd -r -g yaourt yaourt  
RUN echo "yaourt ALL=NOPASSWD: ALL" >> /etc/sudoers  
RUN mkdir /tmp/yaourt  
RUN chown -R yaourt:yaourt /tmp/yaourt  
  
RUN pacman-db-upgrade  
  
WORKDIR /tmp/yaourt  
  
# fix `error setting certificate verify locations`  
RUN trust extract-compat  
  
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
RUN yaourt --noconfirm -S lximediaserver-svn  
  
USER root  
RUN mkdir -p /data/{images,music,videos}  
  
WORKDIR /  
  
COPY entrypoint.sh /entrypoint.sh  
  
USER yaourt  
VOLUME /data  
EXPOSE 4280  
CMD /entrypoint.sh  

