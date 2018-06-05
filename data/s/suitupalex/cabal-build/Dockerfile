FROM base/archlinux:latest  
  
MAINTAINER Alexander Martin <alex@suitupalex.com>  
  
# Update system and install the Haskell platform.  
RUN pacman --sync --refresh --sysupgrade --noconfirm --noprogressbar --quiet
&& \  
pacman --sync --noconfirm --noprogressbar --quiet ghc cabal-install haddock
happy alex  
  
# Create a separate user to run cabal as. Root access shouldn't typically be  
# necessary. Specify the UID so that it is unique including from the host.  
RUN useradd --uid 11235 --create-home --comment "Build User" build  
  
USER build  
ENV HOME /home/build  
  
# Set the umask to 002 so that the group has write access inside and outside  
# the container.  
ADD umask.sh $HOME/umask.sh  
  
# Setup PATH to prioritize local cabal in ahead of system PATH.  
ENV PATH $HOME/.cabal/bin:$PATH  
  
WORKDIR /code  
  
ENTRYPOINT ["/home/build/umask.sh"]  
  
RUN cabal update  
  
CMD ["cabal", "install", "-j"]  

