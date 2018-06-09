# Visual Studio Code  
FROM ubuntu:16.04  
ENV CODEDEB=https://go.microsoft.com/fwlink/?LinkID=760868  
ADD $CODEDEB code.deb  
  
RUN apt-get update && apt-get -y install \  
\--no-install-recommends \  
./code.deb \  
libgtk2.0-0 \  
libx11-xcb1 \  
libxtst6 \  
libxss1 \  
libasound2 \  
git \  
openssh-server \  
xauth \  
ttf-ubuntu-font-family \  
&& rm -rf code.deb \  
&& rm -rf /var/lib/apt/lists/*  
  
WORKDIR /usr/share/fonts/truetype/droid-sans-mono  
ADD utils/droid-sans-mono.ttf .  
RUN chmod 644 droid-sans-mono.ttf  
  
WORKDIR /usr/share/themes/Flatabulous/gtk-2.0  
ADD utils/gtkrc .  
RUN chmod 644 gtkrc  
  
ADD utils/gtkrc-2.0 /etc/skel/.gtkrc-2.0  
  
ENV USERNAME=code GID=1000 UID=1000 \  
CODECONF=/code/config CODEEXT=/code/extensions  
  
ENV VSCODE code --user-data-dir ${CODECONF} --extensions-dir ${CODEEXT}  
RUN echo "alias vscode='${VSCODE}'" >> /etc/skel/.bashrc  
  
RUN useradd -ms /bin/bash ${USERNAME} \  
&& mkdir -p ${CODECONF} ${CODEEXT} \  
&& chown -R ${USERNAME}:${USERNAME} /code  
  
WORKDIR /  
  
ADD start.sh /usr/local/bin/start.sh  
RUN chmod +x /usr/local/bin/start.sh  
  
ENTRYPOINT ["start.sh"]  
  

