FROM shsingh/kali-linux-docker  
MAINTAINER shain.singh@gmail.com  
  
RUN echo "deb http://http.kali.org/kali kali-rolling main contrib non-free" >
/etc/apt/sources.list && \  
echo "deb-src http://http.kali.org/kali kali-rolling main contrib non-free" >>
/etc/apt/sources.list  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get -y update && apt-get -y dist-upgrade && apt-get clean  
  
RUN apt-get -y install kali-linux-full  
RUN apt-get -y install zsh vim git tmux  
  
CMD ["/bin/bash"]  

