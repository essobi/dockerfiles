FROM buildpack-deps:stretch  
  
RUN apt-get -qq update && \  
apt-get -qqy install vim tree ifstat sysstat net-tools locales sudo  
  
RUN echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen && \  
locale-gen en_US.utf8  
  
RUN sed -i 's/"syntax on/syntax on/g' /etc/vim/vimrc; \  
sed -i 's/"set background=dark/set background=dark/g' /etc/vim/vimrc; \  
echo "set expandtab" >> /etc/vim/vimrc; \  
echo "set tabstop=4" >> /etc/vim/vimrc; \  
echo "set hls" >> /etc/vim/vimrc; \  
echo "map <C-n> :tabnext<CR>" >> /etc/vim/vimrc; \  
echo "map <C-p> :tabprevious<CR>" >> /etc/vim/vimrc; \  
echo "set tabpagemax=300" >> /etc/vim/vimrc  
  
RUN sed -i "s/# export LS_OPTIONS='--color=auto'/export LS_OPTIONS='--
color=auto'/g" /root/.bashrc; \  
sed -i 's/# eval "`dircolors`"/eval "`dircolors -b`"/g' /root/.bashrc; \  
sed -i "s/# alias ls='ls \$LS_OPTIONS'/alias ls='ls \$LS_OPTIONS'/g"
/root/.bashrc; \  
sed -i "s/# alias ll='ls \$LS_OPTIONS -l'/alias ll='ls \$LS_OPTIONS -l'/g"
/root/.bashrc; \  
echo "alias grep='grep --color=auto'" >> /root/.bashrc; \  
echo "alias egrep='egrep --color=auto'" >> /root/.bashrc  

