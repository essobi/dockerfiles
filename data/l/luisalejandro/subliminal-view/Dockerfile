FROM dockershelf/debian:sid  
MAINTAINER Luis Alejandro Martínez Faneyth <luis@huntingbears.com.ve>  
  
ENV COMMON_BUILD_DEPENDS="imagemagick librsvg2-bin build-essential git \  
virtualenv golang nodejs" \  
URXVT_BUILD_DEPENDS="libxt-dev libxrender-dev libx11-dev libxpm-dev groff-base
\  
autotools-dev xutils-dev libxft-dev chrpath libperl-dev \  
libev-dev libstartup-notification0-dev libgtk2.0-dev" \  
VIM_BUILD_DEPENDS="libacl1-dev libgpmg1-dev autoconf debhelper libncurses5-dev
\  
libselinux1-dev libgtk2.0-dev libgtk-3-dev libxaw7-dev libxt-dev \  
libxpm-dev libperl-dev tcl-dev python3-dev ruby ruby-dev lua5.2 \  
liblua5.2-dev"  
RUN useradd -ms /bin/bash build  
RUN apt-get update && apt-get install wget gnupg apt-transport-https  
RUN echo "deb https://deb.nodesource.com/node_7.x sid main" >
/etc/apt/sources.list.d/nodesource.list  
RUN wget -qO- https://deb.nodesource.com/gpgkey/nodesource.gpg.key | apt-key
add -  
RUN apt-get update && apt-get install ${COMMON_BUILD_DEPENDS}
${URXVT_BUILD_DEPENDS} \  
${VIM_BUILD_DEPENDS}  
RUN gem install rake  
  
USER build  
CMD ["bash"]

