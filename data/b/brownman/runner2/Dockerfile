FROM ubuntu:14.04  
#FROM ubuntu:12.04  
################################################ ENV_VARS  
ENV DEBIAN_FRONTEND noninteractive  
ENV MODE_DEBUG false  
ENV dir_ssh '/root'  
################################################ APT-GET  
RUN echo IMAGINE APT-GET UPDATE..  
RUN apt-get -y update 1>/dev/null  
RUN apt-get -y install sudo #who needs it? DOCKER=YES TRAVIS=NO  
################################################ TRAVIS STEPS  
ADD . /docker  
RUN chmod +x /docker/travis.sh  
RUN /docker/travis.sh  
################################################ SSH: CONFIG  
# Prepare a known host file for non-interactive ssh connections  
RUN mkdir -p $dir_ssh/.ssh  
RUN touch $dir_ssh/.ssh/known_hosts  
################################################ INSTALL REPO: GITLAB-CI-
RUNNER  
WORKDIR /gitlab-ci-runner.git  
################################################ HOOK: ON_IMAGE_RESTART:
execute the user's custom script  
# When the image is started add the remote server key, set up the runner and
run it  
CMD ssh-keyscan -H $GITLAB_SERVER_FQDN >> /root/.ssh/known_hosts && bundle
exec ./bin/setup_and_run  

