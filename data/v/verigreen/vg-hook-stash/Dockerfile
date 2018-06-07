FROM verigreen/stash:stash_3.8_v0.1  
MAINTAINER Giovanni Matos http://github.com/gmatoshp  
  
ENV VG_HOOK_HOME="/var/vg_hook/home" \  
VG_HOOK="/var/vg_hook/config" \  
VERIGREEN_VERSION="2.0.1" \  
VG_HOOK_EXE="vg_hook.sh"  
RUN mkdir -p $VG_HOOK && \  
mkdir -p $VG_HOOK_HOME && \  
  
curl -sSL
https://github.com/Verigreen/verigreen/releases/download/verigreen-$VERIGREEN_VERSION/verigreen-
git-hook.tar.gz -o /tmp/verigreen-git-hook.tar.gz && \  
cd /tmp && \  
tar -xzvf verigreen-git-hook.tar.gz && \  
cp git-hook/verigreen-git-hook/* $VG_HOOK_HOME  
  
ADD stash_setup.py stash_setup.py  
ADD setup.sh setup.sh  
ADD setup_hook.py setup_hook.py  
ADD vg_hook.sh vg_hook.sh  
CMD ./setup.sh $STASH_INSTALL_DIR  

