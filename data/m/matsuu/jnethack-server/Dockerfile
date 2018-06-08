FROM ubuntu  
  
RUN \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y autoconf bison \  
bsdmainutils bzip2 flex gcc git groff language-pack-ja libncursesw5-dev \  
libsqlite3-dev make ncurses-dev patch sqlite3 tar telnetd-ssl wget xinetd && \  
apt-get clean  
  
RUN locale-gen ja_JP.UTF-8  
  
RUN git clone git://github.com/paxed/dgamelaunch.git && \  
cd dgamelaunch && \  
sed -i \  
-e "s/-lrt/-lrt -pthread/" \  
configure.ac && \  
sed -i \  
-e "/^maxnicklen/s/=.*/= 16/" \  
-e "/SERVERID/s/nethack\.alt\.org/nethack.matsuu.net/" \  
-e "/SERVERID/s/nethack\.alt\.org/matsuu.net\/nethack/" \  
-e "/game_\(path\|args\)/s/nethack/jnethack/" \  
-e "/game_name/s/NetHack 3\.4\.3/JNetHack 3.4.3-0.11/" \  
examples/dgamelaunch.conf && \  
sed -i \  
-e "s/NetHack 3\.4\.3/JNetHack 3.4.3-0.11/" \  
examples/dgl_menu_main_user.txt && \  
./autogen.sh \  
\--enable-sqlite \  
\--enable-shmem \  
\--with-config-file=/opt/nethack/nethack.alt.org/etc/dgamelaunch.conf && \  
make && \  
./dgl-create-chroot && \  
echo "#!/bin/sh\nLANG=ja_JP.UTF-8 /opt/nethack/nethack.alt.org/dgamelaunch" \  
> /opt/nethack/nethack.alt.org/dgamelaunch-wrapper && \  
chmod +x /opt/nethack/nethack.alt.org/dgamelaunch-wrapper && \  
cd .. && \  
rm -rf dgamelaunch  
  
RUN \  
wget \  
http://sourceforge.net/projects/nethack/files/nethack/3.4.3/nethack-343-src.tgz
\  
http://jaist.dl.sourceforge.jp/jnethack/58545/jnethack-3.4.3-0.11.diff.gz \  
http://elbereth.up.seesaa.net/nethack/jnethack-3.4.3-0.10-utf8-2.patch.bz2 &&
\  
tar zxf nethack-343-src.tgz && \  
cd nethack-3.4.3 && \  
gzip -dc ../jnethack-3.4.3-0.11.diff.gz | patch -p1 && \  
bzip2 -dc ../jnethack-3.4.3-0.10-utf8-2.patch.bz2 | patch -p1 && \  
sh sys/unix/setup.sh x && \  
sed -i \  
-e "/^CFLAGS/s/-O/-O2 -fomit-frame-pointer/" \  
sys/unix/Makefile.src sys/unix/Makefile.utl && \  
sed -i \  
-e "/rmdir \.\/-p/d" \  
-e "/^PREFIX/s:=.*:= /opt/nethack/nethack.alt.org:" \  
-e "/^GAMEDIR/s:=.*:= \$(PREFIX)/nh343:" \  
-e "/^VARDIR/s:=.*:= \$(GAMEDIR)/var:" \  
-e "/^GAMEGRP/s:=.*:= games:" \  
sys/unix/Makefile.top && \  
sed -i \  
-e "/# define XI18N/d" \  
-e "/define HACKDIR/s:\".*\":\"/nh343\":" \  
-e "/define COMPRESS /s:\".*\":\"/bin/gzip\":" \  
include/config.h && \  
sed -i \  
-e "/XI18N/i #include <locale.h>" \  
sys/unix/unixmain.c && \  
sed -i \  
-e "s:/\* \(#define\s*\(SYSV\|LINUX\|TERMINFO\|TIMED_DELAY\)\)\s*\*/:\1:" \  
-e "s:/\* \(#define VAR_PLAYGROUND\).*:\1 \"/nh343/var\":" \  
include/unixconf.h && \  
sed -i \  
-e "/^enter_explore_mode()/a {return 0;}\nSTATIC_PTR int _enter_explore_mode()" \  
src/cmd.c && \  
sed -i \  
-e "/^#define ENTRYMAX/s/100/10000/" \  
-e "/^#define NAMSZ/s/10/16/" \  
-e "/^#define PERS_IS_UID/d" \  
src/topten.c && \  
make all && \  
make install && \  
cd .. && \  
rm -rf \  
nethack-3.4.3 \  
nethack-343-src.tgz \  
jnethack-3.4.3-0.11.diff.gz \  
jnethack-3.4.3-0.10-utf8-2.patch.bz2  
  
RUN tar cf - \  
/bin/sh \  
/bin/dash \  
/lib/x86_64-linux-gnu/libncurses* \  
/usr/share/i18n \  
/usr/share/locale \  
/usr/share/locale-langpack \  
/usr/lib/x86_64-linux-gnu/gconv \  
/usr/lib/locale \  
| tar xf - -C /opt/nethack/nethack.alt.org/  
  
RUN ( \  
echo "service telnet" && \  
echo "{" && \  
echo " socket_type = stream" && \  
echo " protocol = tcp" && \  
echo " user = root" && \  
echo " wait = no" && \  
echo " server = /usr/sbin/in.telnetd" && \  
echo " server_args = -L /opt/nethack/nethack.alt.org/dgamelaunch-wrapper" && \  
echo " rlimit_cpu = 120" && \  
echo "}" \  
) > /etc/xinetd.d/dgl  
  
VOLUME ["/opt/nethack/nethack.alt.org/nh343/var",
"/opt/nethack/nethack.alt.org/dgldir"]  
  
EXPOSE 23  
  
CMD ["xinetd", "-dontfork"]  

