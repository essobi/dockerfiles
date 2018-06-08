FROM frolvlad/alpine-bash  
  
COPY ./etc/inputrc /etc/inputrc  
  
# perl is required by git-submodule  
# less makes git log/diff colorful  
RUN apk add --no-cache \  
openssh-client git perl make less \  
bash bash-completion docker-bash-completion \  
vim \  
htop iftop \  
tmux fish mdocml-apropos && \  
echo '\  
. /etc/profile ; \  
PS1='\''\[\e[01;33m\\][\h \u:\\[\e[01;34m\\]\w\[\e[01;33m\\]]\[\e[00m\\]\$
'\'' ; \  
eval `dircolors -b` ; \  
alias ls="ls --color=auto" ; \  
alias l="ls -lah" ; \  
alias ll="ls -lh" ; \  
' >> /etc/bash.bashrc && \  
echo '. ~/.bashrc' > /root/.bash_profile && \  
echo '. /etc/bash.bashrc' > /root/.bashrc && \  
echo 'set-option -g default-shell /usr/bin/fish' > /root/.tmux.conf && \  
mkdir -p /root/.config/fish/functions && \  
echo '\  
function fish_prompt ;\  
if not set -q __fish_prompt_hostname ;\  
set -g __fish_prompt_hostname (hostname) ;\  
end ;\  
set_color -o yellow ;\  
echo -n -s "$USER" @ "$__fish_prompt_hostname" " " ;\  
set_color -o blue ;\  
echo -n (prompt_pwd) ;\  
echo -n " # " ;\  
set_color normal ;\  
end ;\  
\  
alias l="ls -la" ;\  
' > /root/.config/fish/functions/fish_prompt.fish #&& \  
ln -s vim /usr/local/bin/vi  
  
CMD ["bash"]  

