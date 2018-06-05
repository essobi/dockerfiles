## -*- docker-image-name: "dotfiles" -*-  
FROM debian:testing  
  
MAINTAINER Alexandre Héaumé <aheaume@gmail.com>  
  
# Install packages  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update -qy  
RUN apt-get install -qy --no-install-recommends curl emacs24-nox git haskell-
platform make zsh  
  
# Change the user  
RUN useradd -ms /bin/zsh aheaume  
USER aheaume  
ENV HOME /home/aheaume  
  
# Install dotfiles  
RUN git clone https://github.com/aheaume/dotfiles $HOME/src/dotfiles  
WORKDIR $HOME/src/dotfiles  
RUN git submodule update --init --recursive  
RUN make  
  
# Default to zsh when running the image  
CMD ["zsh"]  

