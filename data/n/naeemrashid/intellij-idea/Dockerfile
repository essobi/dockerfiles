FROM debian:jessie-slim  
ENV DEBIAN_FRONTEND noninteractive  
RUN mkdir -p /usr/share/man/man1/ \  
&& apt-get update && apt-get install -y software-properties-common \  
hicolor-icon-theme \  
libgl1-mesa-dri \  
libgl1-mesa-glx \  
libpango1.0-0 \  
libxtst6 \  
gconf2 \  
gconf-service \  
gvfs-bin \  
libasound2 \  
libcap2 \  
libgconf-2-4 \  
libgnome-keyring-dev \  
libgtk2.0-0 \  
libnotify4 \  
libnss3 \  
libxkbfile1 \  
libxss1 \  
libxtst6 \  
libx11-xcb-dev \  
xdg-utils \  
openjdk-7-jre-headless \  
openjdk-7-jdk \  
&& rm -rf /var/lib/apt/lists/*  
ENV VERSION=2017.3.4  
ENV IDEA_URL=https://download.jetbrains.com/idea/ideaIU-${VERSION}.tar.gz  
RUN buildDeps=' \  
ca-certificates \  
curl \  
tar \  
' \  
&& apt-get update && apt-get install -y $buildDeps --no-install-recommends \  
&& curl -L ${IDEA_URL} > /tmp/intellij-idea.tar.gz \  
&& tar -xzvf /tmp/intellij-idea.tar.gz -C /opt/ \  
&& rm -rf /tmp/*.zip \  
&& apt-get purge --auto-remove $buildDeps  
#RUN useradd --create-home --home-dir $HOME eclipse \  
# && chown -R eclipse:eclipse $HOME \  
# && mkdir $HOME/workspace  
WORKDIR /home/root/  
CMD [ "/opt/intellij-idea/bin/studio.sh" ]  

