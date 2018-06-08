FROM ubuntu:16.04  
MAINTAINER Sugeng Tigefa <sugeng@tigefa.space>  
ENV DEBIAN_FRONTEND=noninteractive DEBCONF_NONINTERACTIVE_SEEN=true  
COPY sources.list /etc/apt/sources.list  
RUN apt update  
RUN apt upgrade -y  
RUN apt install -y sudo curl wget apt-utils language-pack-gnome-en language-
pack-gnome-id command-not-found command-not-found-data gnupg gnupg-agent
gnupg2 apt-transport-https ca-certificates software-properties-common tzdata  
RUN locale-gen en_US  
RUN update-locale LANG=en_US.UTF-8 LC_CTYPE=en_US.UTF-8  
RUN export LC_ALL="en_US.UTF-8" LANG="en_US.UTF-8" LANGUAGE="en_US:en"  
RUN locale  
RUN sudo add-apt-repository ppa:jonathonf/backports -y  
RUN sudo add-apt-repository ppa:jonathonf/aria2 -y  
# RUN sudo add-apt-repository ppa:jonathonf/python-2.7 -y  
RUN sudo add-apt-repository ppa:deadsnakes/ppa -y  
RUN sudo add-apt-repository ppa:mc3man/xerus-media -y  
RUN sudo add-apt-repository ppa:mc3man/mpv-tests -y  
RUN sudo add-apt-repository ppa:git-core/ppa -y  
RUN sudo add-apt-repository ppa:mercurial-ppa/releases -y  
RUN sudo add-apt-repository ppa:dominik-stadler/subversion-1.9 -y  
RUN sudo add-apt-repository ppa:ubuntu-toolchain-r/test -y  
RUN sudo add-apt-repository ppa:longsleep/golang-backports -y  
RUN sudo add-apt-repository ppa:brightbox/ruby-ng -y  
RUN sudo add-apt-repository ppa:apt-fast/stable -y  
RUN sudo add-apt-repository ppa:numix/ppa -y  
RUN sudo add-apt-repository ppa:numix/numix-daily -y  
RUN sudo add-apt-repository ppa:qbittorrent-team/qbittorrent-unstable -y  
RUN sudo add-apt-repository ppa:gnome-terminator/nightly-gtk3 -y  
RUN sudo add-apt-repository ppa:noobslab/macbuntu -y  
RUN sudo add-apt-repository ppa:noobslab/icons -y  
RUN sudo add-apt-repository ppa:noobslab/themes -y  
RUN sudo add-apt-repository ppa:transmissionbt/ppa -y  
RUN sudo add-apt-repository ppa:wfg/0ad -y  
RUN sudo add-apt-repository ppa:obsproject/obs-studio -y  
RUN sudo add-apt-repository ppa:peek-developers/stable -y  
RUN sudo add-apt-repository ppa:otto-kesselgulasch/gimp -y  
RUN sudo add-apt-repository ppa:uget-team/ppa -y  
RUN sudo add-apt-repository ppa:clipgrab-team/ppa -y  
RUN sudo add-apt-repository ppa:neovim-ppa/stable -y  
RUN sudo add-apt-repository ppa:certbot/certbot -y  
RUN sudo add-apt-repository ppa:chris-lea/redis-server -y  
RUN sudo apt-get install -y dirmngr gnupg  
RUN sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys
561F9B9CAC40B2F7  
RUN sudo apt-get install -y apt-transport-https ca-certificates  
RUN sudo sh -c 'echo deb https://oss-
binaries.phusionpassenger.com/apt/passenger xenial main >
/etc/apt/sources.list.d/passenger.list'  
RUN sudo sh -c 'echo deb http://apt.llvm.org/xenial/ llvm-toolchain-xenial-5.0
main > /etc/apt/sources.list.d/llvm.list'  
RUN sudo sh -c 'echo deb-src http://apt.llvm.org/xenial/ llvm-toolchain-
xenial-5.0 main >> /etc/apt/sources.list.d/llvm.list'  
RUN wget -O - https://apt.llvm.org/llvm-snapshot.gpg.key|sudo apt-key add -  
RUN curl -sL https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -  
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee
/etc/apt/sources.list.d/yarn.list  
RUN curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash -  
RUN sudo apt-get -y install aria2 youtube-dl  
RUN sudo apt-get update  
RUN apt-get upgrade -y  
RUN apt-get dist-upgrade -y  
RUN apt-get install -y icnsutils graphicsmagick xz-utils rpm bsdtar gcc-
multilib g++-multilib gdc-multilib gobjc-multilib gobjc++-multilib gccgo-
multilib  
RUN apt-get install -y imagemagick libmagickcore-dev libmagickwand-dev  
RUN apt-get install -y curl python-pip python3-pip landscape-common wget whois
tree aria2 netcat figlet  
RUN apt-get install -y libsecret-1-dev xvfb fakeroot dpkg xz-utils xorriso
build-essential nodejs yarn  
RUN sudo apt-get install -y clang-5.0 lldb-5.0 git git-core ruby2.5
ruby2.5-dev  
RUN sudo apt-get install -y build-essential zlib1g-dev libyaml-dev libssl-dev
libgdbm-dev libre2-dev libreadline-dev libncurses5-dev libffi-dev curl
openssh-server checkinstall libxml2-dev libxslt-dev libcurl4-openssl-dev
libicu-dev logrotate rsync python-docutils pkg-config cmake  
RUN sudo apt-get install -y golang golang-go  
RUN sudo apt-get install -y dirmngr gnupg p7zip p7zip-full ruby ruby-dev  
RUN sudo apt-get install -y build-essential git libsecret-1-dev fakeroot rpm
libx11-dev libxkbfile-dev git-all subversion mercurial  
RUN sudo apt-get install -y libxml2-dev libcppunit-dev autoconf automake
autotools-dev autopoint libtool nettle-dev libgmp-dev libssh2-1-dev libc-ares-
dev zlib1g-dev libsqlite3-dev pkg-config libgpg-error-dev libssl-dev
libexpat1-dev  
RUN sudo apt-get build-dep -y aria2 php hhvm  
RUN sudo apt-get install -y landscape*  
RUN sudo apt-get install -y coreutils util-linux bsdutils file openssl ca-
certificates ssh wget patch sudo htop dstat vim nano tmux curl git jq realpath
zsh ksh xz-utils build-essential bash-completion  
RUN sudo apt-get install -y make build-essential libssl-dev zlib1g-dev
libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev
libncursesw5-dev xz-utils tk-dev  
RUN sudo apt-get install -y cmake gcc g++ pkg-config ragel libasound2-dev
libssl-dev libglib2.0-dev libpango1.0-dev libgl1-mesa-dev libevent-dev
libgtk-3-dev libgtk2.0-dev libxrandr-dev libxrender-dev libxcursor-dev
libv4l-dev libgles2-mesa-dev libavcodec-dev libva-dev libvdpau-dev libdrm-dev
libicu-dev libpulse-dev libjack-jackd2-dev libsoxr-dev libglew-dev libglewmx-
dev  
RUN sudo apt-get install -y libboost-dev libgtkmm-3.0-dev libglibmm-2.4-dev
libsqlite3-dev libjemalloc-dev libdmalloc-dev libgoogle-perftools-dev
libexpat1-dev libgcrypt11-dev libgcrypt20-dev libcrypto++-dev libuv1-dev  
RUN echo "postfix postfix/mailname string example.com" | debconf-set-
selections  
RUN echo "postfix postfix/main_mailer_type string 'Internet Site'" | debconf-
set-selections  
RUN sudo apt-get install -y inotify-hookable inotify-tools
libinotifytools0-dev iwatch  
RUN sudo apt-get install -y g++ cmake libboost-all-dev libevent-dev libdouble-
conversion-dev libgoogle-glog-dev libgflags-dev libiberty-dev liblz4-dev
liblzma-dev libsnappy-dev make zlib1g-dev binutils-dev libjemalloc-dev libssl-
dev pkg-config  
RUN sudo apt-get install -y libunwind8-dev libelf-dev libdwarf-dev  
RUN sudo apt-get install -y inotify-hookable inotify-tools
libinotifytools0-dev iwatch hhvm-dev valgrind libev-dev libevhtp-dev libevent-
dev  
  
# Build  
# RUN cd /tmp && git clone -b v2018.05.07.00
https://github.com/facebook/folly.git && cd folly && mkdir _build && cd _build
&& cmake configure .. && make -j $(nproc) && sudo make install  
# Print tool versions  
RUN bash --version | head -n 1  
RUN zsh --version  
RUN ksh --version || true  
RUN dpkg -s dash | grep ^Version | awk '{print $2}'  
RUN git --version  
RUN curl --version  
RUN wget --version  
RUN ruby --version  
RUN gem --version  
RUN python --version  
  
RUN sudo ln -fs /usr/share/zoneinfo/Asia/Jakarta /etc/localtime  
RUN sudo dpkg-reconfigure -f noninteractive tzdata  
RUN sudo apt-get update  
RUN apt-get upgrade -y  
RUN apt-get dist-upgrade -y  
RUN sudo apt-get autoremove -y  
RUN sudo apt-get clean -y  
RUN sudo apt-get autoclean -y  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

