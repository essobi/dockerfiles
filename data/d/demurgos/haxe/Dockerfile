FROM base/archlinux:latest  
MAINTAINER Charles Samborski <demurgos@demurgos.net>  
  
# Build:  
# docker build -t haxe-3.1 .  
# Run:  
# docker run -it haxe-3.1  
# Run with GUI support:  
# xhost local:docker && docker run -it -e DISPLAY -v
$HOME/.Xauthority:/home/root/.Xauthority --net=host haxe-3.1  
# Packages (for Flash development with Haxe)  
# Utils: git, coreutils (provides `timeout` and `true`), expect  
# Haxe compilation: camlp4, gcc (provides `as`), make, neko, ocaml, pcre, zlib  
# Flash dev: firefox, flashpluginm, xorg-server-xvfb  
RUN pacman -Syu --quiet --noconfirm --noprogressbar \  
&& pacman -S --quiet --noconfirm --noprogressbar \  
camlp4 \  
coreutils \  
expect \  
firefox \  
flashplugin \  
gcc \  
git \  
make \  
neko \  
ocaml \  
pcre \  
xorg-server-xvfb \  
zlib  
  
# Initialize firefox by running it once  
RUN timeout 20s xvfb-run firefox; true  
# Haxe 3.1_bugfix installation from source  
# HAXE_STD_PATH is required for Haxelib and normal execution  
ENV HAXE_STD_PATH /usr/lib/haxe/std/:.  
# HAXELIB_REPOSITORY_PATH points to the root of Haxelib's local repository  
ENV HAXELIB_REPOSITORY_PATH /usr/lib/haxe/lib/  
RUN HAXE_SRC_PATH="/src/haxe/" \  
&& HAXE_REPOSITORY="https://github.com/demurgos/haxe.git" \  
&& HAXE_BRANCH="3.1_bugfix" \  
&& git clone --recursive --branch "$HAXE_BRANCH" "$HAXE_REPOSITORY"
"$HAXE_SRC_PATH" \  
&& cd "$HAXE_SRC_PATH" \  
&& make \  
&& make install \  
# Haxelib configuration, must be executed outside of the Haxe sources  
&& cd / \  
&& echo "$HAXELIB_REPOSITORY_PATH" | haxelib setup  
  
RUN pacman -Syu --quiet --noconfirm --noprogressbar \  
&& pacman -S --quiet --noconfirm --noprogressbar \  
nodejs \  
npm \  
&& npm install -g npm gulp-cli  
  
# Haxelib packages for Flash development  
RUN haxelib install lime 2.3.3 \  
&& haxelib install munit 2.1.2 \  
&& haxelib install openfl 3.0.1 \  
&& haxelib install svg 1.1.1  
  
CMD ["/bin/bash"]  

