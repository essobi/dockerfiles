# The FROM instruction sets the Base Image for subsequent instructions.  
# As such, a valid Dockerfile must have FROM as its first instruction.  
FROM node:6  
# The MAINTAINER instruction allows you to set the Author field of the
generated images.  
MAINTAINER Pham Cong Toan <toan.pham@monokera.com>  
  
RUN apt-get update && apt-get install -y \  
git \  
ruby-full \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN gem install sass  
  
RUN yarn global add \  
bower \  
generator-angular \  
generator-karma \  
grunt-cli \  
gulp \  
http-server \  
yo \  
&& echo '{ "allow_root": true }' > /root/.bowerrc  
  
# The RUN instruction will execute any commands in a new layer on top of the
current image and commit the results.  
# The resulting committed image will be used for the next step in the
Dockerfile.  
# This is not a docker best practice but there are no choice when this become
a our template Dockerfile  
RUN mkdir -p /root/.ssh \  
&& ssh-keyscan bitbucket.org >> /root/.ssh/known_hosts \  
&& ssh-keyscan github.com >> /root/.ssh/known_hosts  
  
# The WORKDIR instruction sets the working directory for any RUN, CMD,  
# ENTRYPOINT, COPY and ADD instructions that follow it in the Dockerfile.  
WORKDIR /data/www/current  
  
# The COPY instruction copies new files or directories from <src>  
# and adds them to the filesystem of the container at the path <dest>.  
# TL;DR https://www.ctl.io/developers/blog/post/dockerfile-add-vs-copy/  
# Use COPY  
# The VOLUME instruction creates a mount point with the specified name and
marks it  
# as holding externally mounted volumes from native host or other containers.  
VOLUME /data/www  
  
# An ONBUILD command executes after the current Dockerfile build completes.  
# ONBUILD composer update  
# The main purpose of a CMD is to provide defaults for an executing container.  
CMD http-server -p 3000  
  
# The EXPOSE instructions informs Docker that the container will listen on the
specified network ports at runtime.  
EXPOSE 443  
EXPOSE 80  
EXPOSE 35729  
EXPOSE 3000  

