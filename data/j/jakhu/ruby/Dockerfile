FROM jakhu/base:latest  
# Builds ruby image  
MAINTAINER Gum-Joe "kishansambhi@hotmail.co.uk"  
# Override ENV  
ENV JAKHU_WORKER_VERSION 1.0.0  
ENV JAKHU_WORKER_NAME jakhu-docker-ubuntu-ruby  
ENV JAKHU_OS_IMAGE ubuntu  
ENV JAKHU_OS_IMAGE_TAG latest  
ENV JAKHU_DOCKER_IMAGE ruby  
RUN /bin/bash -l -c "source ~/.rvm/scripts/rvm && rvm use $RUBY_VERSION && gem
install rake foreman compass"  
# Re-generate versioning  
# Pull images list  
RUN sudo chown -R jakhu /jakhuImages; cd /jakhuImages && git pull  
VOLUME /jakhuImages  
# Create version  
RUN sudo chown -R jakhu /metadata  
COPY . /jakhutools  
RUN /bin/bash -l -c "source ~/.rvm/scripts/rvm && rvm use $RUBY_VERSION &&
ruby /jakhutools/versions.rb"  
RUN chmod 700 /metadata/version.sh  
RUN chmod 777 /metadata/version.sh  
RUN sudo chmod 700 /jakhutools/info.sh  
RUN sudo chmod 777 /jakhutools/info.sh  
RUN sudo chmod 700 /runner  
RUN sudo chmod 777 /runner  
RUN sudo chmod +s /runner  
VOLUME /runner  
VOLUME /jakhutools  
CMD /jakhutools/info.sh  

