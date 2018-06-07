FROM ubuntu:16.04  
  
LABEL maintainer="DockerWare" \  
description="KiCad is an open source software suite for Electronic Design
Automation (EDA). \  
The programs handle Schematic Capture, and PCB Layout with Gerber output. The
suite runs on Windows, \  
Linux and OS X and is licensed under GNU GPL v3."  
  
ENV \  
DISPLAY=unix:0.0  
  
RUN set -xe \  
  
&& buildDeps=" \  
software-properties-common \  
" \  
&& runtimeDeps=" \  
libatk-adaptor \  
libgail-common \  
libcanberra-gtk-module \  
" \  
&& apt-get update && apt-get install -y $buildDeps $runtimeDeps --no-install-
recommends \  
  
# Install via ppa  
&& localeDeps=" \  
kicad-locale-ca \  
kicad-locale-cs \  
kicad-locale-de \  
kicad-locale-el \  
kicad-locale-es \  
kicad-locale-fi \  
kicad-locale-fr \  
kicad-locale-hu \  
kicad-locale-id \  
kicad-locale-it \  
kicad-locale-ja \  
kicad-locale-ko \  
kicad-locale-lt \  
kicad-locale-nl \  
kicad-locale-pl \  
kicad-locale-pt \  
kicad-locale-ru \  
kicad-locale-sk \  
kicad-locale-sl \  
kicad-locale-sv \  
kicad-locale-zh \  
kicad-locale-bg \  
language-pack-ca \  
language-pack-cs \  
language-pack-de \  
language-pack-el \  
language-pack-es \  
language-pack-fi \  
language-pack-fr \  
language-pack-hu \  
language-pack-id \  
language-pack-it \  
language-pack-ja \  
language-pack-ko \  
language-pack-lt \  
language-pack-nl \  
language-pack-pl \  
language-pack-pt \  
language-pack-ru \  
language-pack-sk \  
language-pack-sl \  
language-pack-sv \  
language-pack-bg \  
" \  
&& apt-add-repository --yes ppa:js-reynaud/ppa-kicad \  
&& apt-get update \  
&& apt-get install -y \  
kicad \  
kicad-library \  
$localeDeps \  
  
# Setup enveroument  
&& echo "NO_AT_BRIDGE=1" | tee -a /etc/environment \  
&& useradd --no-log-init --user-group --home-dir /home creator \  
  
# Clean  
&& apt-get purge -y \--auto-remove -o
APT::AutoRemove::RecommendsImportant=false $buildDeps \  
&& apt-get clean \  
&& rm -rf /tmp/* /var/tmp/* /var/lib/apt/lists/*  
  
COPY entrypoint.sh /usr/local/bin/entrypoint  
  
WORKDIR /home  
  
ENTRYPOINT ["entrypoint"]  

