FROM alpine  
RUN adduser -s /bin/sh -D user -G wheel  
## full color mode! (Should I leave it here, or tell people to include it at
runtime?  
#ENV TERM xterm-256color  
VOLUME /home/user/filesToPersist  
# tar and wget are already installed; get updates. we need ca-certificates  
# because the game archive is hosted on a https site.  
RUN apk update && apk add --no-cache wget tar ca-certificates ncurses-dev  
# Download brogue-1.7.4 archive, unzip it to its proper place, then delete the  
# original archive.  
RUN wget -O /tmp/brogue.tbz2
https://sites.google.com/site/broguegame/brogue-1.7.4-linux-amd64.tbz2 && \  
mkdir /home/user/brogue && \  
tar -C /home/user/brogue -xvf /tmp/brogue.tbz2 --strip-components 1 && \  
rm /tmp/brogue.tbz2  
# First, the packages needed for compiling the ncurses executable. "make
clean"  
# outputs: "env: can't execute 'bash': No such file or directory", so I'm  
# adding bash to this list to be safe  
# Second and third, "make clean" and make brogue's ncurses binaries  
# Lastly, uninstall the packages we don't need any more  
RUN apk add --no-cache build-base gcc abuild binutils bash && make
--directory=/home/user/brogue clean && make --directory=/home/user/brogue
curses && apk del build-base gcc abuild binutils ca-certificates bash  
# brogue saves high scores in the directory it was executed from  
USER user  
WORKDIR /home/user/filesToPersist  
# right now, "sleep [some amount of time]" needs to be added because otherwise  
# docker will start brogue without proper terminal dimensions set yet, and the  
# screen gets garbled.  
# https://github.com/docker/docker/issues/10341  
ENTRYPOINT sleep 0.2 ; /home/user/brogue/bin/brogue  

