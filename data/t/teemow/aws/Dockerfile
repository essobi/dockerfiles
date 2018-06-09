FROM teemow/build  
  
RUN sudo pacman -S --noconfirm python-pip groff  
RUN sudo pip install -U awscli  
  
ENTRYPOINT ["aws"]  
  

