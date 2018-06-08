# docker-version 0.6  
FROM stackbrew/ubuntu:13.10  
# install dependencies  
RUN DEBIAN_FRONTEND=noninteractive apt-get update  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y --force-yes python
build-essential  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y --force-yes software-
properties-common  
RUN DEBIAN_FRONTEND=noninteractive add-apt-repository -y ppa:chris-lea/node.js  
RUN DEBIAN_FRONTEND=noninteractive apt-get update  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y --force-yes nodejs  
  
# see https://github.com/npm/npm/issues/4377#issuecomment-31252532  
RUN DEBIAN_FRONTEND=noninteractive npm -g install yo coffee-script  
  
# Append to $PATH variable.  
RUN echo '\n# Node.js\nexport PATH="node_modules/.bin:$PATH"' >>
/root/.bash_profile  
  
# ruby (sass/compass)  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y ruby2.0  
RUN gem install sass  
RUN gem install compass  
  
# Define default command.  
CMD ["yo"]

