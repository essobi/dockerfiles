FROM ubuntu:xenial  
MAINTAINER Yu-Cheng (Henry) Huang  
  
# Installed Packages:  
# Essentials:  
# - gcc  
# - g++  
# - git  
# - Vim with lots of plugins  
# - ranger  
# PenTest Tools:  
# - Metasploit  
# - sqlmap  
# - nmap  
# - Recon-ng  
# Reversing/Pwn Tools:  
# - qira  
# - GDB with Peda/symgdb/Pwngdb  
# - PwnTools  
# - one_gadget  
# Symbolic Execution:  
# - Z3Prover  
# - Triton  
# Misc:  
# - Tmux  
# - John the Ripper  
# - binwalk  
SHELL ["/bin/bash", "-c"]  
  
RUN dpkg --add-architecture i386 && \  
apt-get update && \  
apt-get install -y man git git-core tmux bash-completion curl wget \  
python-pip python-dev build-essential cmake unzip \  
xz-utils nmap john strace ltrace gcc g++ libc6-dev-i386 \  
gdbserver lib32stdc++6 libxml2-dev libxslt1-dev libssl-dev nasm \  
libboost1.58-dev libpython2.7-dev libc6-dbg libc6-dbg:i386 sudo  
  
RUN pushd ~ && \  
git clone https://github.com/Happyholic1203/dotfiles && \  
pushd ~/dotfiles && \  
chmod +x ./install.sh && \  
./install.sh --with-ycm --with-ranger && \  
echo "#!/bin/bash" > ~/init && \  
echo "TERM=xterm-256color tmux" >> ~/init && \  
echo "bash" >> ~/init && \  
chmod +x ~/init && \  
popd && \  
popd  
  
RUN pip install --upgrade setuptools && \  
pip install ipython==5.7.0 && \  
pip install pwntools && \  
rm -rf ~/.cache/pip  
  
RUN export tmp=$(mktemp -d) && \  
pushd $tmp && \  
wget https://github.com/vim/vim/archive/v8.0.1098.zip && \  
unzip v8.0.1098.zip && \  
pushd vim-8.0.1098 && \  
./configure --with-features=huge \  
\--enable-multibyte \  
\--enable-rubyinterp=yes \  
\--enable-pythoninterp=yes \  
\--with-python-config-dir=/usr/lib/python2.7/config \  
\--enable-python3interp=yes \  
\--with-python3-config-dir=/usr/lib/python3.5/config \  
\--enable-perlinterp=yes \  
\--enable-luainterp=yes \  
\--enable-gui=gtk2 \  
\--enable-cscope \  
\--prefix=/usr/local && \  
make VIMRUNTIMEDIR=/usr/local/share/vim/vim80 && \  
make install && \  
rm -f /usr/bin/vi && \  
ln -sf `which vim` /usr/bin/vi && \  
popd && \  
popd && \  
rm -rf $tmp  
  
RUN export tmp=`mktemp -d` && \  
pushd $tmp && \  
wget https://bitbucket.org/LaNMaSteR53/recon-ng/get/v4.9.3.tar.gz && \  
tar -zxvf v4.9.3.tar.gz && \  
mv LaNMaSteR53-recon-ng* ~/recon-ng && \  
popd && \  
rm -rf $tmp && \  
pushd ~/recon-ng && \  
bash -c 'pip install -r REQUIREMENTS || pip install -r REQUIREMENTS || pip
install -r REQUIREMENTS' && \  
ln -sf ~/recon-ng/recon-ng /usr/local/bin/recon-ng && \  
popd && \  
rm -rf ~/.cache/pip  
  
RUN export tmp=`mktemp -d` && \  
pushd $tmp && \  
wget http://www.capstone-
engine.org/download/3.0.4/ubuntu-14.04/libcapstone3_3.0.4-0.1ubuntu1_amd64.deb
&& \  
wget http://www.capstone-engine.org/download/3.0.4/ubuntu-14.04/libcapstone-
dev_3.0.4-0.1ubuntu1_amd64.deb && \  
dpkg -i libcapstone3_3.0.4-0.1ubuntu1_amd64.deb && \  
dpkg -i libcapstone-dev_3.0.4-0.1ubuntu1_amd64.deb && \  
popd && \  
rm -rf $tmp  
  
RUN pushd ~ && \  
git clone https://github.com/radare/radare2 && \  
pushd radare2 && \  
./sys/install.sh && \  
find . -type f -name '*.o' -exec rm -f {} \; && \  
find . -type f -name '*.a' -exec rm -f {} \; && \  
popd && \  
popd  
  
RUN export tmp=$(mktemp -d) && \  
pushd $tmp && \  
wget https://github.com/Z3Prover/z3/tarball/z3-4.5.0 && \  
tar zxvf z3-4.5.0 && \  
mv Z3Prover-z3-* z3 && \  
pushd z3 && \  
python scripts/mk_make.py --python && \  
pushd build && \  
make && \  
make install && \  
popd && \  
popd && \  
popd && \  
rm -rf $tmp  
  
RUN export tmp=`mktemp -d` && \  
pushd $tmp && \  
wget
https://github.com/geohot/qira/tarball/2d4cdfb121384f83ea8deec45c73b740687538f9
&& \  
tar -zxvf 2d4cdfb121384f83ea8deec45c73b740687538f9 && \  
mv geohot-qira-* ~/qira && \  
popd && \  
rm -rf $tmp && \  
pushd ~/qira && \  
./install.sh && \  
find ~/qira/tracers/qemu/qemu-2.1.3 -type f -name '*.o' -exec rm -f {} \; ; \  
rm -f ~/qira/tracers/qemu/qemu-2.1.3.tar.bz2 ; \  
popd  
  
RUN export tmp=`mktemp -d` && \  
pushd $tmp && \  
wget http://downloads.metasploit.com/data/releases/metasploit-latest-
linux-x64-installer.run && \  
chmod +x metasploit-latest-linux-x64-installer.run && \  
./metasploit-latest-linux-x64-installer.run --mode unattended
--unattendedmodeui none && \  
popd && \  
rm -rf $tmp  
  
RUN cd ~ && \  
git clone https://github.com/longld/peda  
  
RUN cd ~ && \  
git clone https://github.com/Happyholic1203/Pwngdb && \  
cp ~/Pwngdb/.gdbinit ~/  
  
RUN export tmp=`mktemp -d` && \  
pushd $tmp && \  
wget
http://software.intel.com/sites/landingpage/pintool/downloads/pin-2.14-71313-gcc.4.4.7-linux.tar.gz
&& \  
tar xvzf pin-2.14-71313-gcc.4.4.7-linux.tar.gz && \  
mv pin-2.14-71313-gcc.4.4.7-linux ~/pin && \  
popd && \  
rm -rf $tmp  
  
RUN export tmp=`mktemp -d` && \  
pushd $tmp && \  
wget https://github.com/JonathanSalwan/Triton/tarball/master && \  
tar -zxvf master && \  
mv JonathanSalwan-Triton-* ~/pin/source/tools/Triton && \  
popd && \  
rm -rf $tmp && \  
pushd ~/pin/source/tools/Triton && \  
mkdir build && \  
pushd build && \  
cmake -DPINTOOL=on .. && \  
make -j$(grep processor < /proc/cpuinfo | wc -l) install && \  
popd && \  
find . -type f -name '*.o' -exec rm -f {} \; && \  
popd  
  
RUN cd ~ && \  
git clone https://github.com/SQLab/symgdb && \  
cd ~/symgdb && \  
./install.sh && \  
rm -rf /usr/local/share/gdb ; \  
cp -r gdb/gdb/data-directory /usr/local/share/gdb && \  
rm -rf ~/symgdb/gdb ; \  
rm -f ~/symgdb/gdb-*.tar.gz ; \  
echo "source ~/symgdb/symgdb.py" >> ~/.gdbinit  
  
RUN cd ~ && \  
wget https://github.com/sqlmapproject/sqlmap/tarball/master --output-
document=sqlmap.tar.gz && \  
tar -zxvf sqlmap.tar.gz && \  
mv sqlmapproject-sqlmap-* sqlmap && \  
ln -sf `pwd`/sqlmap/sqlmap.py /usr/local/bin/sqlmap && \  
rm -f sqlmap.tar.gz  
  
RUN apt-get update && \  
apt-get install -y ruby-dev && \  
command curl -sSL https://rvm.io/mpapis.asc | gpg --import - && \  
\curl -sSL https://get.rvm.io | bash -s stable --ruby && \  
source /usr/local/rvm/scripts/rvm && \  
echo 'source /etc/profile.d/rvm.sh' >> ~/.bashrc_custom && \  
gem install one_gadget  
  
RUN export tmp=$(mktemp -d) && \  
pushd $tmp && \  
wget https://github.com/ReFirmLabs/binwalk/archive/v2.1.1.tar.gz && \  
tar -zxvf v2.1.1.tar.gz && \  
cd binwalk-* && \  
python setup.py install && \  
popd && \  
rm -rf $tmp  
  
RUN echo "#!/bin/bash" > ~/msfconsole && \  
echo "pass=`sed -n 's/\s*password:\s*\"\\([0-9a-z]*\\)\"$/\1/p'
/opt/metasploit/apps/pro/ui/config/database.yml | sort | uniq`" >>
~/msfconsole && \  
echo 'msf=/opt/metasploit/ctlscript.sh' >> ~/msfconsole && \  
echo '$msf status | grep "already running" || $msf start' >> ~/msfconsole && \  
echo '/usr/local/bin/msfconsole --quiet -x "db_disconnect; db_connect
msf3:$pass@localhost:7337/msf3"' >> ~/msfconsole && \  
echo 'export PATH="$PATH:~/pin/source/tools/Triton/build"' >> ~/.bashrc_custom
&& \  
chmod +x ~/msfconsole && \  
echo "alias msfconsole='~/msfconsole'" >> ~/.aliases && \  
rm -rf /tmp/* && \  
rm -rf ~/.cache ; \  
rm -f ~/.bash_history ; \  
rm -f ~/.config/radare2/history ; \  
rm -rf ~/.pwntools-cache ; \  
rm -f ~/.gdb_history ; \  
rm -f ~/.viminfo ; \  
rm -f ~/.config/ranger/history ; \  
rm -f ~/.config/radare2/history; \  
ipython profile create && \  
sed -i "s/.*\\(c\\.TerminalInteractiveShell\\.editing_mode\\).*/\1 = 'vi'/g"
~/.ipython/profile_default/ipython_config.py  
  
# qira  
EXPOSE 3002 3003 4000  
CMD ["/root/init"]  

