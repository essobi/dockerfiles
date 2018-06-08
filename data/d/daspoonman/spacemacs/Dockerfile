FROM daspoonman/base-dev  
  
RUN sudo apt-get update \  
&& sudo add-apt-repository ppa:kelleyk/emacs \  
&& sudo apt-get update \  
&& sudo apt-get install -y emacs25 silversearcher-ag netcat libgl1-mesa-glx \  
&& git clone \--depth 1 --branch master https://github.com/syl20bnr/spacemacs
${USER_HOME}/.emacs.d \  
&& emacs -batch -u ${USER} -q -kill  
  
COPY files/start_spacemacs_session /usr/local/bin/  
COPY files/pbcopy /usr/bin/  
  
CMD ["/usr/local/bin/start_spacemacs_session"]  

