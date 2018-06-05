FROM ubuntu:16.04  
RUN apt-get update && apt-get install -y sudo apt-utils net-tools iputils-ping
tmux  
RUN useradd -ms /bin/bash sundbp && \  
adduser sundbp sudo && \  
echo "sundbp ALL = (ALL) NOPASSWD: ALL" >> /etc/sudoers && \  
mkdir -p /home/sundbp/dev/dotfiles  
  
COPY bootstrap-linux.sh /home/sundbp/dev/dotfiles/  
COPY setup-vim.sh /home/sundbp/dev/dotfiles/  
  
RUN chown -R sundbp:sundbp /home/sundbp/dev  
  
USER sundbp  
WORKDIR /home/sundbp  
  
RUN cd dev/dotfiles && \  
./bootstrap-linux.sh && \  
./setup-vim.sh  
  
USER root  
COPY . /home/sundbp/dev/dotfiles/  
COPY toolbox-entrypoint.sh /home/sundbp/.entrypoint.sh  
RUN chown -R sundbp:sundbp /home/sundbp/dev && \  
chmod 755 /home/sundbp/.entrypoint.sh  
  
USER sundbp  
ENV TB_BUILD true  
RUN cd dev/dotfiles && \  
./install-dotfiles.sh -f  
ENV LANG en_US.UTF-8  
ENV HOME /home/sundbp  
  
RUN sudo chsh -s /usr/bin/fish sundbp && \  
bash -l -c 'source ~/.nvm/nvm.sh && nvm install v9.4.0' && \  
fish -l -c 'fisher -q (cat ~/dev/dotfiles/fish/fishfile)' && \  
chown -R sundbp:sundbp ~/dev  
  
RUN emacs --batch .bashrc -l /home/sundbp/.emacs.d/init.el -f save-buffer  
  
ENV SHELL /usr/bin/fish  
  
CMD /home/sundbp/.entrypoint.sh  

