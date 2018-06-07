FROM debian:sid  
RUN apt-get update  
RUN apt-get install -yq apt-transport-https gpgv-static gnupg2 bash apt-utils  
RUN echo deb https://pkg.tox.chat/debian stable sid | tee
/etc/apt/sources.list.d/tox.list  
RUN wget -qO - https://pkg.tox.chat/debian/pkg.gpg.key | apt-key add - && apt-
get update  
RUN echo "deb https://eyedeekay.github.io/lair-web/lair-deb/debian rolling
main" | tee /etc/apt/sources.list.d/lair.list  
RUN wget -qO - https://eyedeekay.github.io/lair-web/lair-
deb/cmotc.github.io.lair-web.lair-deb.gpg.key | apt-key add -  
RUN apt-get update && \  
apt-get install -yq libtox-dev libtoxav0 libtoxav0-dbgsym libtoxav-dev \  
libtoxcore0 libtoxcore0-dbgsym libtoxcore-dev libtoxdns0 libtoxdns0-dbgsym \  
libtoxdns-dev libtoxencryptsave0 libtoxencryptsave0-dbgsym \  
libtoxencryptsave-dev build-essential checkinstall valac valac-vapi \  
libvala-dev sdl2-vapi tox-vapi pkgconf tartrazine libsdl2-dev \  
libsdl2-gfx-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-net-dev \  
libsdl2-ttf-dev libsdl2-2.0-0 libsdl2-image-2.0-0 libsdl2-mixer-2.0-0 \  
libsdl2-net-2.0-0 libsdl2-ttf-2.0-0 libsdl-ttf2.0-0 libsdl-ttf2.0-dev \  
libluajit-5.1-2 libluajit-5.1-common libluajit-5.1-dev liblua5.2-dev \  
luajit lua5.2 lua-check libc-dev make git musl musl-dev musl-tools \  
debhelper devscripts xdg-user-dirs fakeroot-ng xdg-utils git-core git  
RUN adduser --disabled-password --disabled-login --home /home/lair --shell
/bin/bash --gecos 'lair,,,,' lair  
RUN for item in $(ls /usr/include/luajit-2.1/); do \  
ln -v -f -s /usr/include/luajit-2.0/$item /usr/include/$item; \  
ln -v -f -s /usr/lib/x86_64-linux-gnu/pkgconfig/luajit.pc
/usr/lib/pkgconfig/lua.pc; \  
ln -v -f -s /usr/lib/x86_64-linux-gnu/pkgconfig/luajit.pc
/usr/lib/x86_64-linux-gnu/pkgconfig/lua.pc; \  
done  
USER lair  
WORKDIR /home/lair  
RUN git clone https://github.com/eyedeekay/valair /home/lair/valair  
RUN cd valair && \  
make  
USER root  
RUN chown -R lair:lair /home/lair/valair  
RUN apt-get install -y lairart  
RUN cd valair && make && make install  
USER lair  
CMD /usr/bin/LAIR  

