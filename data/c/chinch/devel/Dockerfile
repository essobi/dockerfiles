FROM fedora  
  
RUN dnf -y install unzip wget python ncurses-compat-libs cmake;dnf
autoremove;dnf clean all;cd ~/;mkdir tools;cd ~/tools;wget
https://dl.google.com/android/repository/android-
ndk-r15-linux-x86_64.zip;unzip android-ndk-r15-linux-x86_64.zip;cd android-
ndk-r15/build/tools;python make_standalone_toolchain.py \--arch arm64 \--api
24 \--stl libc++ \--install-dir /root/tc;cd ~/; rm -rf ~/tools;touch
/etc/profile.d/toolchain.sh;echo "export PATH=/root/tc/bin:$PATH" >
/etc/profile.d/toolchain.sh;chmod 0700 /etc/profile.d/toolchain.sh  
  
CMD /bin/bash  

