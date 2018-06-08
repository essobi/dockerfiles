FROM ubuntu:vivid  
  
# ADD apt-http-proxy /etc/apt/apt.conf.d/  
ENV HOME /root  
RUN apt-get update && apt-get install -y aptitude && aptitude clean  
  
### Basic sysadmin tools ###  
RUN aptitude install -y dstat htop man && aptitude clean  
  
### User tools ###  
RUN aptitude install -y vim fish sloccount byobu vim-gocomplete && aptitude
clean  
  
### Software engineering tools ###  
RUN aptitude install -y build-essential && aptitude clean  
RUN aptitude install -y zip unzip strace autoconf libtool clang llvm &&
aptitude clean  
RUN aptitude install -y mercurial git git-man wget curl && aptitude clean  
  
# Remove unnecessary packages  
RUN apt-get autoremove -y  
  
### Environment ###  
ADD docker-run-cmd.sh /bin/  
RUN echo fish >> /bin/docker-run-cmd.sh  
CMD /bin/docker-run-cmd.sh  
RUN chsh -s /usr/bin/fish root && byobu-ctrl-a screen  
  
ADD apti /usr/sbin/apti  
ADD user /usr/sbin/user  
  
ADD fish/config.fish /root/.config/fish/config.fish  
  
RUN date > ~/build_date.txt  
  
RUN cp -vr --reflink=auto -t /etc/skel ~/* ~/.profile ~/.byobu ~/.config  
  
RUN useradd -m -s /usr/bin/fish -U user && chown -R user:user ~user  
  
### OCaml-multicore ###  
ADD build-ocaml-multicore.sh /opt/  
RUN su user -c /opt/build-ocaml-multicore.sh  

