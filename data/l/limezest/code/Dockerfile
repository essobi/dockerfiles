# Visual Studio in a container  
# NOTE: Needs the redering device (yeah... idk)  
#docker run -d \  
# -v /tmp/.X11-unix:/tmp/.X11-unix \  
# -v /home/cyril/workspace:/home/user \  
# -e DISPLAY=unix$DISPLAY \  
# --device /dev/dri \  
# --name vscode \  
# limezest/vscode  
#start.sh  
#su user -c /usr/local/bin/code  
FROM jess/chromium  
MAINTAINER forked by csabourault, higly inspired by jfrazz  
  
RUN apt-get update && apt-get install -y \  
build-essential \  
ca-certificates \  
curl \  
git \  
libasound2 \  
libgconf-2-4 \  
libgnome-keyring-dev \  
libgtk2.0-0 \  
libnss3 \  
libpci3 \  
libxtst6 \  
unzip \  
\--no-install-recommends  
  
ENV HOME /home/user  
RUN useradd --create-home --home-dir $HOME user \  
&& chown -R user:user $HOME  
  
# install node  
RUN curl -sL https://deb.nodesource.com/setup | bash -  
RUN apt-get update && apt-get install -y \  
nodejs \  
npm \  
&& rm -rf /var/lib/apt/lists/* \  
&& npm update -g  
  
# download the release 1.2  
RUN curl -sSL https://go.microsoft.com/fwlink/?LinkID=620884 -o /tmp/vs.zip \  
&& unzip /tmp/vs.zip -d /usr/src/ \  
&& rm -rf /tmp/vs.zip \  
&& ln -snf /usr/src/VSCode-linux-x64/code /usr/local/bin/code  
  
COPY start.sh /usr/local/bin/start.sh  
WORKDIR $HOME  
  
ENTRYPOINT [ "/usr/local/bin/start.sh" ]  

