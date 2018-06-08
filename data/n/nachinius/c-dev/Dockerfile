FROM ubuntu:trusty  
MAINTAINER nachinius  
  
RUN apt-get update; apt-get upgrade -y  
#RUN apt-get upgrade -y  
RUN apt-get install -y build-essential  
RUN apt-get install -y linux-headers-generic  
#RUN apt-get install -y glibc-dev  
RUN apt-get install -y vim exuberant-ctags  
RUN apt-get install -y bash-completion  
RUN apt-get install -y gdb  
RUN apt-get install -y libc-dbg  
RUN apt-get install -y nodejs  
  
# colorize output of make  
RUN apt-get install -y colormake  
RUN echo "alias make='colormake '\n" >> /etc/bash.bashrc  
  
# manpages  
RUN apt-get install -y man-db manpages-dev  
RUN apt-get install -y less  
  
# colorize manpages for all users that use bash  
RUN echo "export LESS_TERMCAP_mb=$'\E[01;31m' # begin blinking \n \  
export LESS_TERMCAP_md=$'\E[01;38;5;74m' # begin bold \n \  
export LESS_TERMCAP_me=$'\E[0m' # end mode \n \  
export LESS_TERMCAP_se=$'\E[0m' # end standout-mode \n \  
export LESS_TERMCAP_so=$'\E[38;5;246m' # begin standout-mode - info box \n \  
export LESS_TERMCAP_ue=$'\E[0m' # end underline \n \  
export LESS_TERMCAP_us=$'\E[04;38;5;146m' # begin underline \n" >>
/etc/bash.bashrc  
  
  
RUN apt-get install -y locate  
RUN apt-get install -y tree  
RUN updatedb  
  
CMD ["/bin/bash"]  
  
  
  

