FROM ubuntu:14.04  
# Script to choose Python version  
COPY choose_python.sh /usr/bin/  
# Installer script for Pythons 2.7 3.4 3.5 3.6  
COPY build_install_pythons.sh /  
  
# Install Pythons 2.7 3.4 3.5 3.6 and matching pips  
RUN bash build_install_pythons.sh && rm build_install_pythons.sh  
  
# Install manylinux1 libraries. See:  
# https://www.python.org/dev/peps/pep-0513/#the-manylinux1-policy  
# Thanks to @native-api for the report:  
# https://github.com/matthew-brett/multibuild/issues/106  
RUN apt-get update && \  
apt-get install -y libncurses5 libgcc1 libstdc++6 libc6 libx11-6 libxext6 \  
libxrender1 libice6 libsm6 libgl1-mesa-glx libglib2.0-0  
  
# Run Python selection on way into image  
ENTRYPOINT ["/usr/bin/choose_python.sh"]  

