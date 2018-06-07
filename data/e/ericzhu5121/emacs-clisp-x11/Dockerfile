FROM ubuntu:14.10  
MAINTAINER Eric Zhu <eric.zhu5121@gmail.com>  
  
ENV TERM xterm  
RUN apt-get update && apt-get install -y curl emacs24-lucid fonts-inconsolata
sbcl emacs-goodies-el emacs24-el git subversion && apt-get clean && apt-get
purge  
  
# Replace 1000 with your user / group id  
RUN export uid=1000 gid=1000 && \  
mkdir -p /home/developer && \  
echo "developer:x:${uid}:${gid}:Developer,,,:/home/developer:/bin/bash" >>
/etc/passwd && \  
echo "developer:x:${uid}:" >> /etc/group && \  
echo "developer ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/developer && \  
chmod 0440 /etc/sudoers.d/developer && \  
chown ${uid}:${gid} -R /home/developer  
  
USER developer  
ENV HOME /home/developer  
ADD ql.lsp /home/developer/ql.lsp  
RUN curl -fksSL https://raw.github.com/overtone/emacs-
live/master/installer/install-emacs-live.sh > ~/install-emacs-live.sh && \  
echo "Y"|bash ~/install-emacs-live.sh && rm -f ~/install-emacs-live.sh &&\  
cd $HOME/.live-packs && git clone \--recursive
https://github.com/thephoeron/slime-pack.git &&\  
echo "(live-add-packs '(~/.live-packs/developer-pack ~/.live-packs/slime-
pack))" > ~/.emacs-live.el && \  
mkdir -p ~/tmp && cd ~/tmp && curl -O http://beta.quicklisp.org/quicklisp.lisp
&& \  
echo ""|sbcl --script ~/ql.lsp && rm -fr ~/ql.lsp  
  
CMD /usr/bin/emacs  

