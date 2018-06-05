FROM alpine:latest  
  
MAINTAINER MURAMATSU Atsushi <amura@tomato.sakura.ne.jp>  
  
WORKDIR /nethack  
COPY jnethack-3.6.0-0.7-utf8.patch linux-tty-x11 jnethack.conf ./  
RUN apk \--update add \--no-cache \  
ncurses-libs \  
libx11 \  
libxaw  
RUN apk \--update add \--no-cache \--virtual .build-dep \  
curl \  
flex \  
bison \  
build-base \  
musl-dev \  
linux-headers \  
ncurses-dev \  
libx11-dev \  
libxaw-dev \  
bdftopcf \  
mkfontdir \  
&& curl -sL http://ftp.gnu.org/pub/gnu/libiconv/libiconv-1.15.tar.gz | tar
-xzf - \  
&& cd libiconv-1.15 \  
&& ./configure \--prefix=/usr/local && make && make install \  
&& cd .. && rm -rf libiconv-1.15 \  
&& curl -sL https://ja.osdn.net/projects/nkf/downloads/64158/nkf-2.1.4.tar.gz
| tar zxf - \  
&& curl -sL
https://sourceforge.net/projects/nethack/files/nethack/3.6.0/nethack-360-src.tgz
| tar zxf - \  
&& cd nkf-2.1.4 && make && cd .. \  
&& nkf-2.1.4/nkf -W -e -Lu \--overwrite jnethack.conf \  
&& cd nethack-3.6.0 \  
&& curl -sL
https://ja.osdn.net/projects/jnethack/downloads/67126/jnethack-3.6.0-0.8.diff.gz
| zcat | patch -p2 \  
&& find . -type f -exec ../nkf-2.1.4/nkf -e -Lu \--overwrite {} \; \  
&& rm -rf ../nkf-2.1.4 \  
&& patch -p1 < ../jnethack-3.6.0-0.7-utf8.patch \  
&& sh sys/unix/setup.sh ../linux-tty-x11 \  
&& make \  
&& make install \  
&& cd .. && rm -rf nethack-3.6.0 \  
&& apk del \--prune .build-dep  
# make save dir && sysconf  
COPY entrypoint.sh /  
RUN chmod +x /entrypoint.sh \  
&& mkdir data \  
&& cd /usr/local/games/lib/jnethackdir \  
&& mv save logfile record xlogfile /nethack/data \  
&& chmod -R og+w /nethack/data \  
&& ln -s /nethack/data/* . \  
&& cp -rp /nethack/data /nethack/data.orig \  
&& mv sysconf /nethack \  
&& ln -s /nethack/sysconf \  
&& cat /nethack/jnethack.conf >> /nethack/sysconf  
  
ENTRYPOINT [ "/entrypoint.sh" ]  
CMD [ "/usr/local/bin/jnethack" ]  
  
# docker build -t amura/jnethack .  

