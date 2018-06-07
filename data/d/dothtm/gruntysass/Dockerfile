FROM dothtm/rubynode  
  
LABEL description="Grunt and Sass built inside a base with Ruby and Node.js in
one container."  
  
LABEL image_tag=dothtm/gruntysass  
  
LABEL filter_distro=hub-mod  
LABEL filter_app=grunty-sass  
  
  
RUN apt-get update && apt-get upgrade -y  
  
RUN npm install -g grunt grunt-cli  
RUN gem install sass susy compass jekyll  
  
COPY startup.sh /  
  
CMD ["/startup.sh"]

