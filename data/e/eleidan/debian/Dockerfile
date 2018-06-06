FROM debian:stretch  
  
LABEL maintainer="Oleg Kulyk" \  
description="Debian GNU/Linux stretch" \  
run="docker run -it --rm -v $(pwd):/home/phantom/app eleidan/debian:stretch" \  
version="2017-07-06"  
  
ENV HOME="/root" \  
SERVICE_NAME="debian:stretch" \  
CONTAINER_PS1="[ $(get_container_ip) |
\[\e[0;36m\\]$(get_container_service)\[\e[m\\] | \[\e[0;35m\\]\w\[\e[m\\]
]\n\[\e[1;32m\\]>\[\e[m\\] "  
  
COPY .profile .bashrc .bash_history /etc/skel/  
COPY .profile .bashrc .bash_history $HOME/  
  
CMD ["/bin/bash"]  

