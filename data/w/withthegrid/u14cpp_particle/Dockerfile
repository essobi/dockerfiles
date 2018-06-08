FROM drydock/u14:prod  
  
ADD . /u14cpp_particle  
  
# Fix Ubuntu bug "stdin: is not a tty" due to mesg n in .profile  
RUN sed -i 's/^mesg n$/tty -s \&\& mesg n/g' $HOME/.profile  
  
# Set shell script executable permissions  
RUN find . -name '*.sh' -type f | xargs chmod +x  
  
RUN /u14cpp_particle/install.sh  

