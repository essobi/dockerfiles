FROM debian:8  
ENV _TAG=debian-8  
ARG USE_APT_CACHER="false"  
ARG USE_APT_MIRROR="false"  
ARG APT_CACHER_HOST="172.17.0.1"  
ARG APT_MIRROR="th.archive.ubuntu.com"  
RUN if [ "$USE_APT_MIRROR" = "true" ]; then sed -i
"s|archive.ubuntu.com|$APT_MIRROR|g" /etc/apt/sources.list; fi \  
&& if [ "$USE_APT_CACHER" = "true" ]; then echo "Acquire::http::Proxy
\"http://$APT_CACHER_HOST:3142\";" > /etc/apt/apt.conf.d/11proxy; fi  
  
RUN export DEBIAN_FRONTEND="noninteractive" \  
&& apt-get -y update \  
&& apt-get -y install apt-utils \  
&& apt-get -y install autoconf build-essential curl libncurses-dev vim-nox zsh
\  
# for silversearcher  
&& apt-get -y install liblzma-dev libpcre3-dev pkg-config zlib1g-dev \  
# for build zsh documents  
&& apt-get -y install yodl \  
&& rm -rf /var/lib/apt/lists/*  
  
ADD *.sha /build/  
WORKDIR /build  
ENV LIBEVENT_BUILD_DIR=libevent-2.1.8-stable \  
TMUX_BUILD_DIR=tmux-2.7 \  
AG_BUILD_DIR=the_silver_searcher-2.1.0 \  
ZSH_BUILD_DIR=zsh-zsh-5.5.1  
RUN curl -o libevent-2.1.8-stable.tar.gz -sSL
"https://github.com/libevent/libevent/releases/download/release-2.1.8-stable/libevent-2.1.8-stable.tar.gz"
\  
&& sha256sum -c libevent-2.1.8-stable.tar.gz.sha \  
&& tar -xf libevent-2.1.8-stable.tar.gz \  
&& rm libevent-2.1.8-stable.tar.gz libevent-2.1.8-stable.tar.gz.sha  
RUN curl -o tmux-2.7.tar.gz -sSL "https://github.com/nuimk/nmk-
tmux/releases/download/2.7/tmux-2.7.tar.gz" \  
&& sha256sum -c tmux-2.7.tar.gz.sha \  
&& tar -xf tmux-2.7.tar.gz \  
&& rm tmux-2.7.tar.gz tmux-2.7.tar.gz.sha  
RUN curl -o zsh-5.5.1.tar.gz -sSL "https://github.com/zsh-
users/zsh/archive/zsh-5.5.1.tar.gz" \  
&& sha256sum -c zsh-5.5.1.tar.gz.sha \  
&& tar -xf zsh-5.5.1.tar.gz \  
&& rm zsh-5.5.1.tar.gz zsh-5.5.1.tar.gz.sha  
RUN curl -o the_silver_searcher-2.1.0.tar.gz -sSL
"http://geoff.greer.fm/ag/releases/the_silver_searcher-2.1.0.tar.gz" \  
&& sha256sum -c the_silver_searcher-2.1.0.tar.gz.sha \  
&& tar -xf the_silver_searcher-2.1.0.tar.gz \  
&& rm the_silver_searcher-2.1.0.tar.gz the_silver_searcher-2.1.0.tar.gz.sha  
  
COPY entrypoint /  
ENTRYPOINT ["/entrypoint"]  

