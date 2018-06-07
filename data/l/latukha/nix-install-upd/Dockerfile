FROM ubuntu:16.04  
MAINTAINER Anton-Latukha <anton.latukha@gmail.com>  
  
# Install dependencies  
RUN apt update && apt -y install git patch curl bzip2  
  
ENV NIX_VER nix-1.11.15  
ENV NIX_SYSTEM x86_64-linux  
ENV NIX_EXT tar.bz2  
ENV NIX_URL
https://nixos.org/releases/nix/"$NIX_VER"/"$NIX_VER"-"$NIX_SYSTEM"."$NIX_EXT"  
RUN mkdir ~/build  
WORKDIR /root/build  
  
# Clone current updated installation process  
RUN git clone -b installFullProgress https://github.com/Anton-Latukha/nix.git
installFullProgress  
  
# Download and extract official installation  
RUN curl -L "$NIX_URL" -O  
RUN tar xvf "$NIX_VER"-"$NIX_SYSTEM"."$NIX_EXT"  
RUN rm "$NIX_VER"-"$NIX_SYSTEM"."$NIX_EXT"  
  
# Copy updated instalation to nix install folder  
RUN cp ./installFullProgress/scripts/install-nix-from-closure.sh
./"$NIX_VER"-"$NIX_SYSTEM"/install-new.sh  
RUN chmod u+x ./"$NIX_VER"-"$NIX_SYSTEM"/install-new.sh  
  
WORKDIR /root/build/"$NIX_VER"-"$NIX_SYSTEM"  
  
# Apply patch that populates build variables with relevant ones  
## This is a patch  
RUN echo '\  
\--- install-nix-from-closure.sh 2017-10-28 14:04:24.812532357 +0200\n\  
+++ install-nix-from-closure-new.sh 2017-10-28 14:03:49.104006041 +0200\n\  
@@ -89,8 +89,8 @@\n\  
{\n\  
readonly dest="/nix"\n\  
readonly self="$(dirname "$(realpath "$0")")"\n\  
-readonly nix="@nix@"\n\  
-readonly cacert="@cacert@"\n\  
+readonly nix="/nix/store/b4s1gxiis1ryvybnjhdjvgc5sr1nq0ys-nix-1.11.15"\n\  
+readonly cacert="/nix/store/28v6ma4zb887m7ldrbqh56r8jjxc53cb-nss-
cacert-3.31"\n\  
readonly appname="$0"\n\  
}\n\  
###############################\n\  
' >> git_to_deploy.patch  
## Applying  
RUN patch install-new.sh git_to_deploy.patch  
  
# Banner  
RUN echo '[ ! -z "$TERM" -a -r /etc/motd ] && cat /etc/issue && cat /etc/motd'
\  
>> /etc/bash.bashrc \  
; echo '\033[1;32m\  
======================================================================\n\  
= Docker container for new Nix install demonstration for NixCon 2017 =\n\  
======================================================================\n\  
\n\  
Installation solves bugs of installator. It is tranparent to migrate to.\n\  
\n\  
Because it stays transparent to migrate upstream to - it also uses single\n\  
user Nix installation, as old does.\n\  
\n\  
And so it falls on nixbld group, because single user installation does\n\  
not requires nix workers by official documentation.\n\  
\n\  
Providing nixbld group and workers is a pure WND of expectations of Nix C++
code.\n\  
So it needs to be upplied manually:\n\  
\033[1;33m \n\  
######## Multiuser block: \n\  
groupadd -r nixbld\n\  
for n in $(seq 1 10); do useradd -c "Nix build user $n" -d /var/empty -g
nixbld -G nixbld -M -N -r -s "$(which nologin)" "nixbld$n"; done\n\  
\033[0;m\  
########\n\  
\n\  
(c) Anton Latukha, Serokell 2017 \n\  
\n\  
Source directory: '"$PWD"'\n'\  
> /etc/motd  

