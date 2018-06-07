# Run heroku-toolblet in a container  
#  
# heroku(){  
# del_stopped heroku  
# docker run -it --rm -u $(id -u):$(id -g) -w $HOME \  
# -v /etc/passwd:/etc/passwd:ro \  
# -v /etc/group:/etc/group:ro \  
# -v /etc/localtime:/etc/localtime:ro \  
# -v /home:/home \  
# -v /tmp:/tmp \  
# -v /run/user/$(id -u):/run/user/$(id -u) \  
# --name heroku \  
# johnnagro/heroku-toolbelt "$@"  
# }  
FROM ubuntu:16.04  
MAINTAINER John Nagro <john.nagro@gmail.com>  
  
RUN apt-get clean && apt-get update  
RUN apt-get install -y \  
sudo \  
wget \  
openssh-client \  
ruby \  
git \  
postgresql-client \  
curl  
  
ADD https://cli-assets.heroku.com/install-ubuntu.sh /opt/install-ubuntu.sh  
RUN sh /opt/install-ubuntu.sh  
  
ENTRYPOINT [ "heroku" ]  

