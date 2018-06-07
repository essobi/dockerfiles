FROM debian:latest  
MAINTAINER Khairul Anwar <https://iruwl.github.io>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
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
  
# Define working directory  
WORKDIR /home/docker  
  
# Activate docker  
USER docker  
  
# Add notes by me  
ADD notes.txt /home/docker  
  
# Default command  
CMD ["/bin/bash"]

