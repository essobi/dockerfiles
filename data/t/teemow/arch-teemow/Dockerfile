FROM teemow/arch  
MAINTAINER Timo Derstappen, teemow@gmail.com  
  
RUN pacman -Sy --noconfirm zsh git vim sudo  
RUN useradd -s /bin/zsh teemow  
RUN echo "teemow ALL = NOPASSWD: ALL" >> /etc/sudoers  
  
RUN pacman -Sy --noconfirm sed  
RUN git clone \--recursive https://github.com/sorin-ionescu/prezto.git
/home/teemow/.zprezto  
RUN find /home/teemow/.zprezto/runcoms/ -name "z*" -exec basename {} \; |
while read filename; do cp /home/teemow/.zprezto/runcoms/$filename
/home/teemow/.$filename; done  
RUN chown -R teemow.teemow /home/teemow  
  
# minimal theme  
RUN echo "autoload -Uz promptinit" >> /home/teemow/.zshrc  
RUN echo "promptinit" >> /home/teemow/.zshrc  
RUN echo "prompt minimal" >> /home/teemow/.zshrc  
  
# fix vi->vim  
RUN ln -s /usr/bin/vim /usr/bin/vi  
  
# Set locale  
RUN locale-gen --no-purge de_DE.UTF-8  
ENV LANG de_DE.UTF-8  
RUN rm /etc/localtime  
RUN ln -s /usr/share/zoneinfo/Europe/Berlin /etc/localtime  
  
ENV SHELL /bin/zsh  
ENV HOME /home/teemow  
WORKDIR /home/teemow  
USER teemow  

