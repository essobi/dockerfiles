FROM elixir:1.6-alpine  
  
RUN apk --no-cache add nodejs nodejs-npm curl git zsh \  
bind-tools inotify-tools gettext shadow alpine-sdk python  
  
# Add dev group  
RUN groupadd dev && useradd -ms /usr/bin/zsh -g dev dev  
  
USER dev  
ENV SHELL /bin/zsh  
  
RUN mix local.hex --force  
RUN mix local.rebar --force  
  
CMD ["/bin/zsh"]  

