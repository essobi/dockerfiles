FROM debian:jessie  
ARG DEBIAN_VERSION="jessie"  
  
MAINTAINER newtork / Alexander Dümont <alexander_duemont@web.de>  
  
  
##########################################  
# #  
# Docker Build #  
# #  
##########################################  
#  
# USAGE  
# -----  
# docker pull newtork/openttd  
# docker build -t newtork/openttd .  
#  
##########################################  
# #  
# Docker Run #  
# #  
##########################################  
#  
# USAGE  
# -----  
# docker run -dit -p 3979:3979/tcp -p 3979:3979/udp newtork/openttd [savegame]
[settings] [servername]  
#  
# \\_____________/ \\_______________________________/ \\_____________/
\\______/ \\________/ \\_________/  
# | | | | | |  
# interactive required port forwarding maintainer save game config string
public game  
# detached destination port can be build name \n-seperated server name  
# terminal changed as required  
#  
##########################################  
# #  
# Build Settings / Environment #  
# #  
##########################################  
# start in root  
# everything is in root  
WORKDIR /root/  
# two scripts needed for running  
ENV UPLOAD_SCRIPT_CONFIG="cfg.update.sh" \  
UPLOAD_SCRIPT_WRAPPER="openttd.wrapper.sh"  
# one script and a default config file needed for building  
ARG UPLOAD_SCRIPT_DOWNLOAD="dl.checked.sh"  
ARG UPLOAD_INPUT_CONFIG="cfg.patches.cfg"  
# (Binary) Download instructions as link + xpath  
ARG OTTD_BINARY_DOWNLOADS="https://www.openttd.org/en/download-stable"  
ARG OTTD_BINARY_DOWNLOADS_ITEM_XPATH="id(\"stable-data\")/*[contains(@id,
\"-linux-debian-$DEBIAN_VERSION-amd64.deb\")][1]"  
# (Assets) Download instructions a link + xpath  
ARG OTTD_ASSETS_DOWNLOADS="https://www.openttd.org/en/download-opengfx"  
ARG OTTD_ASSETS_DOWNLOADS_ITEM_XPATH="id(\"opengfx-data\")/*[contains(@id,
\"-all.zip\")][1]"  
ARG OTTD_ASSETS_TARGET="/root/.openttd/baseset/"  
# Just copy everything, we'll work in /root/  
COPY *.sh *.cfg /root/  
# Default game server port is 3979  
# Keep in mind that TCP AND UDP are needed  
EXPOSE 3979  
##########################################  
# #  
# OpenTTD Download/Setup/Configure #  
# #  
##########################################  
#  
# Build-Process:  
# --------------  
#  
# 1) Download dependencies: curl and libxml2  
# 2) Download and verify the latest OpenTTD Debian package  
# 3) Install the debian package file with dpkg  
# 4) Make apt-get install the missing dependencies to the new package  
# 5) Download and verify the latest OpenTTD Asset files, needed to run the
server  
# 6) Extract the asset files to the game baseset directory  
# 7) Start the server to generate vanilla config, quit it immediately and
patch the config file  
#  
#  
  
RUN chmod -f +x /root/*.sh && \  
\  
echo "[1/7] Preparing installation dependencies..." && \  
apt-get -qq update && \  
apt-get -qqy install libxml2-utils --no-install-recommends > /dev/null 2>&1 &&
\  
apt-get -qqy install curl > /dev/null 2>&1 && \  
\  
echo "[2/7] Downloading installation files..." && \  
binary_tmp=$(mktemp) && \  
/root/$UPLOAD_SCRIPT_DOWNLOAD "$OTTD_BINARY_DOWNLOADS"
"$OTTD_BINARY_DOWNLOADS_ITEM_XPATH" $binary_tmp && \  
\  
echo "[3/7] Installing OpenTTD server..." && \  
dpkg --force-all -i $binary_tmp > /dev/null 2>&1 && \  
\  
echo "[4/7] Installing missing dependencies and cleaning up..." &&\  
apt-get -fqqy install > /dev/null 2>&1 && \  
rm -f $binary_tmp && \  
echo " OTTD has been successfully installed." && \  
\  
echo "[5/7] Downloading Asset files..." && \  
mkdir -p $OTTD_ASSETS_TARGET && \  
assets_tmp=$(mktemp) && \  
/root/$UPLOAD_SCRIPT_DOWNLOAD "$OTTD_ASSETS_DOWNLOADS"
"$OTTD_ASSETS_DOWNLOADS_ITEM_XPATH" $assets_tmp && \  
\  
echo "[6/7] Extracting files and clean up..." && \  
tar -xzf $assets_tmp -C "$OTTD_ASSETS_TARGET" && \  
rm -f $assets_tmp && \  
\  
echo "[7/7] Testrun the vanilla server..." && \  
echo "quit" | /usr/games/openttd -D > /dev/null 2>&1 && \  
/root/$UPLOAD_SCRIPT_CONFIG /root/$UPLOAD_INPUT_CONFIG && \  
\  
echo " Done."  
###############################################  
# #  
# START #  
# #  
###############################################  
# Use the server wrapper file, no default CMD / arguments  
ENTRYPOINT ["/root/openttd.wrapper.sh"]  

