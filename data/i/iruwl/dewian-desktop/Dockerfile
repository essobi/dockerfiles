# vnc-password -> debian  
# run -> (v1) docker run -it --rm -p 5901:5901 -e USER=docker dewian-desktop
bash -c "vncserver :1 -geometry 1204x768 -depth 24 && tail -F ~/.vnc/*.log"  
# (v2) docker run -it --rm dewian-desktop  
FROM debian:latest  
MAINTAINER Khairul Anwar <https://iruwl.github.io>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV VNCDISPLAY 1  
ENV VNCDEPTH 24  
ENV VNCGEOMETRY 1280x700  
  
# Exclude some directories to reduce size  
RUN echo "path-exclude /usr/share/doc/*\n#\  
we need to keep copyright files for legal reasons\n\  
path-include /usr/share/doc/*/copyright\n\  
path-exclude /usr/share/man/*\n\  
path-exclude /usr/share/groff/*\n\  
path-exclude /usr/share/info/*\n#\  
lintian stuff is small, but really unnecessary\n\  
path-exclude /usr/share/lintian/*\n\  
path-exclude /usr/share/linda/*" \  
>> /etc/dpkg/dpkg.cfg.d/01_nodoc  
  
# Update/Upgrade/Cleansing  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get install -yq --no-install-recommends apt-utils && \  
apt-get install -yq --no-install-recommends sudo nano wget && \  
apt-get install -y lightdm xfce4 xfce4-goodies iceweasel tightvncserver
autocutsel && \  
apt-get clean -y && \  
apt-get autoclean -y && \  
apt-get autoremove -y && \  
rm -rf /usr/share/locale/* && \  
rm -rf /var/cache/debconf/*-old && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /usr/share/doc/*  
  
# Update/change apt source list to repository from Indonesia  
RUN mv /etc/apt/sources.list /etc/apt/sources.list.orig  
RUN echo "#KAMBING-UI\n\  
deb http://kambing.ui.ac.id/debian/ jessie main contrib non-free\n\  
deb http://kambing.ui.ac.id/debian/ jessie-updates main contrib non-free\n\  
deb http://kambing.ui.ac.id/debian-security/ jessie/updates main contrib non-
free" \  
>> /etc/apt/sources.list  
  
# Aliases & Add normal user  
RUN \  
echo "alias ls='ls --color=auto'" >> /root/.bashrc && \  
echo "alias ll='ls -lha --color=auto --group-directories-first'" >>
/root/.bashrc && \  
echo "alias l='ls -lh --color=auto --group-directories-first'" >>
/root/.bashrc && \  
addgroup --system docker && \  
adduser \  
\--home /home/docker \  
\--disabled-password \  
\--shell /bin/bash \  
\--gecos "Mr. Docker" \  
\--ingroup docker \  
\--quiet \  
docker && \  
cp /root/.bashrc /home/docker && \  
echo 'docker ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers && \  
echo '# Acquire::http { Proxy "http://172.17.0.1:3142"; };' >>
/etc/apt/apt.conf.d/00proxy  
  
# Add/replace config to enable bash tab-complete  
ADD config /home/docker/.config  
  
# Add notes by me  
ADD notes.txt /home/docker  
  
# Add vnc start command  
ADD start-vnc.sh /home/docker  
RUN chmod +x /home/docker/start-vnc.sh  
  
# Set owner to docker  
RUN chown -R docker.docker /home/docker  
  
# Define working directory  
WORKDIR /home/docker  
  
# Activate docker  
USER docker  
  
RUN touch ~/.Xresources && \  
touch ~/.Xauthority && \  
mkdir ~/.vnc && \  
echo "debian" | vncpasswd -f > ~/.vnc/passwd && \  
chmod 600 ~/.vnc/passwd  
  
# Expose ports  
EXPOSE 5901  
EXPOSE 80  
EXPOSE 22  
# Default command  
CMD ["/home/docker/start-vnc.sh"]  

