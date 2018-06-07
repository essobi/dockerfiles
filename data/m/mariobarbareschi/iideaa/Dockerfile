FROM mariobarbareschi/clang_llvm391  
  
MAINTAINER Mario Barbareschi <mario.barbareschi@unina.it>  
MAINTAINER Giovanni Panice <n@mosfet.io>  
MAINTAINER Antonio Tammaro <ntonjeta@autistici.org>  
  
# Update Software  
# Default command at startup  
RUN pacman --noconfirm -Sy git zsh libedit libffi wget libtar doxygen boost-
libs  
#pacman --noconfirm -Syu &&  
# Copy install script  
ADD . /opt/install-iideaa  
  
SHELL ["/bin/bash", "-c"]  
  
# Run script Install for clang-Chimera, ParadisEO and Bellerophon  
RUN /opt/install-iideaa/install-chimera  
RUN /opt/install-iideaa/install-paradiseo  
RUN /opt/install-iideaa/install-bellerophon  
  
#Letting root be the only user to allow user to run root commands  
# Create a new user  
#RUN useradd -ms /bin/bash iideaa  
# Expose user  
#USER iideaa  

