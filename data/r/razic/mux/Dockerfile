FROM ruby  
  
ENV HOME /root  
ENV TERM xterm-256color  
  
RUN apt-get update \  
&& apt-get -y install tmux \  
&& gem install tmuxinator  
  
ADD .tmux.conf $HOME/.tmux.conf  
ADD .tmuxinator $HOME/.tmuxinator  
  
ENTRYPOINT ["mux"]  

