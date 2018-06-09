FROM teemow/npm  
MAINTAINER Timo Derstappen, teemow@gmail.com  
  
RUN sudo npm install -g grunt-cli  
RUN sudo pacman -S --needed --noconfirm ruby  
RUN sudo gem install compass bourbon  
  
ENTRYPOINT ["grunt"]  

