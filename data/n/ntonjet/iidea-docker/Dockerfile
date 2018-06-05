FROM mariobarbareschi/clang_llvm391  
  
MAINTAINER Giovanni Panice <n@mosfet.io>  
MAINTAINER Antonio Tammaro <ntonjeta@autistici.org>  
MAINTAINER Mario Barbareschi <mario.barbareschi@unina.it>  
  
#RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
# Update Software  
# Default command at startup  
RUN pacman --noconfirm -Sy git zsh libedit libffi wget libtar doxygen  
#pacman --noconfirm -Syu &&  
# Copy install script  
ADD . /opt/install-iidea  
  
SHELL ["/bin/bash", "-c"]  
  
# Run script Install  
RUN /opt/install-iidea/install-chimera  
RUN /opt/install-iidea/install-paradiseo  
RUN /opt/install-iidea/install-bellerophon  
  
# Create a new user  
#RUN useradd -ms /bin/bash homer  
# Expose user  
#USER homer  

