# Pull base image.  
FROM stackbrew/ubuntu:13.10  
MAINTAINER Robert Gruendler <r.gruendler@dubture.com>  
  
# install dependencies  
RUN DEBIAN_FRONTEND=noninteractive apt-get update  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y --force-yes software-
properties-common  
RUN DEBIAN_FRONTEND=noninteractive add-apt-repository -y ppa:chris-lea/node.js  
RUN DEBIAN_FRONTEND=noninteractive apt-get update  
# brunch installs skeletons via git  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y --force-yes nodejs git  
  
# see https://github.com/npm/npm/issues/4377#issuecomment-31252532  
RUN npm -g install http://registry.npmjs.org/ansi-color/-/ansi-color-0.2.1.tgz  
RUN npm -g install coffee-script brunch bower  
  
# Append to $PATH variable.  
RUN echo '\n# Node.js\nexport PATH="node_modules/.bin:$PATH"' >>
/root/.bash_profile  
  
# Attach a web volume  
VOLUME /var/www  
  
# Expose development server  
EXPOSE 3333  
# Define default command.  
CMD ["node"]  

