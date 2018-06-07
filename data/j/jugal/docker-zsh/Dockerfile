FROM ubuntu  
RUN apt-get update  
RUN apt-get install git -y  
  
# Fonts  
RUN apt-get install locales  
RUN locale-gen "en_US.UTF-8"  
RUN LC_ALL=en_US.UTF-8  
RUN LANG=en_US.UTF-8  
RUN git clone https://github.com/powerline/fonts.git --depth=1  
RUN sh fonts/install.sh  
RUN rm -rf fonts  
  
RUN apt-get install zsh -y  
RUN git clone git://github.com/robbyrussell/oh-my-zsh.git ~/.oh-my-zsh  
RUN cp ~/.oh-my-zsh/templates/zshrc.zsh-template ~/.zshrc  
RUN chsh -s $(which zsh)  
  
# CUSTOMIZE ZSH  
RUN git clone https://github.com/bhilburn/powerlevel9k.git ~/.oh-my-
zsh/themes/powerlevel9k  
RUN sed -i
's/ZSH_THEME="robbyrussell"/ZSH_THEME="powerlevel9k\/powerlevel9k"/g' ~/.zshrc  
#RUN sed -i 's/ZSH_THEME="robbyrussell"/ZSH_THEME="agnoster"/g' ~/.zshrc  
WORKDIR /root  
CMD ["/usr/bin/zsh","-l"]  

