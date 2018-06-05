FROM fedora:26  
RUN dnf install -y git \  
bzip2 \  
scons \  
protobuf-compiler \  
python2-protobuf  
  
RUN set -o pipefail && \  
curl https://armkeil.blob.core.windows.net/developer/Files/downloads/gnu-
rm/6-2017q2/gcc-arm-none-eabi-6-2017-q2-update-linux.tar.bz2 | tar -C /opt
-xjf - && \  
echo "export PATH=/opt/gcc-arm-none-eabi-6-2017-q2-update/bin:$PATH" >
/etc/profile.d/arm-none-eabi_path.sh  

