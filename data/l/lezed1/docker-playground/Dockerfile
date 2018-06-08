FROM ubuntu:xenial  
  
RUN mkdir /root/dependencies  
  
ADD install/foundation-install.sh /root/dependencies/  
RUN bash /root/dependencies/foundation-install.sh  
  
ADD install/apt-install.sh /root/dependencies/  
RUN bash /root/dependencies/apt-install.sh  
  
ADD install/pip-install.sh /root/dependencies/  
RUN bash /root/dependencies/pip-install.sh  
  
ADD install/misc-install.sh /root/dependencies/  
RUN bash /root/dependencies/misc-install.sh  
  
RUN apt-get install -y wget  
ADD install/spacemacs-install.sh /root/dependencies/  
RUN bash /root/dependencies/spacemacs-install.sh  
ADD install/dot-spacemacs /home/software/.spacemacs  
RUN su software -c "emacs --batch -u software --kill"  
  
ADD install/extra-install.sh /root/dependencies/  
RUN bash /root/dependencies/extra-install.sh  
  
ADD install/ocaml-install.sh /root/dependencies/  
RUN bash /root/dependencies/ocaml-install.sh  
ADD install/ocaml-user-install.sh /home/software/  
  
RUN rm -rf /tmp/* /var/lib/apt/lists/* /root/.cache/*  
  
USER software  
  
# ADD install/dot-ocamlinit /home/software/.ocamlinit  
RUN bash /home/software/ocaml-user-install.sh  
RUN opam user-setup install  
RUN rm /home/software/ocaml-user-install.sh  
  
WORKDIR /home/software/cuauv/software  
CMD sudo service ssh start && echo "CUAUV Docker container running! C-c to
stop the container" && cat  

