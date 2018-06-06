#  
# Erlang build environment.  
#  
# docker build -t pt_erlang_build .  
#  
# APP_SOURCE_DIR is the folder containing the rebar.config file.  
#  
# To execute unfortunately you have to use a linux machine. For windows, you
have to log into the  
# docker-machine VM. '$USERNAME' is the name you use on your private
repositories  
#  
# docker run --rm --name build_test -v $SSH_AUTH_SOCK:$SSH_AUTH_SOCK -e
SSH_AUTH_SOCK \  
# -v $APP_SOURCE_DIR:/erlang_app timadorus/rebar3-build $USERNAME  
#  
# you must have a ssh-agent running, and it will only work if running local on
the docker host!!!  
#  
# reuse the image already created  
FROM erlang  
  
MAINTAINER Lutz Behnke <lutz.behnke@gmx.de>  
  
RUN apt-get update  
RUN apt-get -y install openssh-client git  
  
RUN mkdir /build  
WORKDIR /build/  
  
ADD build_erlang.sh /build/  
ADD https://s3.amazonaws.com/rebar3/rebar3 /build/  
RUN chmod a+x /build/rebar3  
  
VOLUME /erlang_app  
  
CMD ["nouser"]  
ENTRYPOINT ["/bin/bash","-ev","/build/build_erlang.sh","/erlang_app","/build"]  
  

