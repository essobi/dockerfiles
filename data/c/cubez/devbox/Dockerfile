FROM alpine:3.2  
ENV BASE_PACKAGES curl fish nano git  
ENV EXTRA_PACKAGES py-pip  
ENV DOCKER_VERSION 1.8.3  
ENV COMPOSE_VERSION 1.5.0  
ENV SOURCE_DIR /root/src  
  
# Update and install all of the required packages  
# At the end, remove the apk cache  
RUN apk update && \  
apk upgrade && \  
apk add $BASE_PACKAGES && \  
apk add $EXTRA_PACKAGES && \  
rm -rf /var/cache/apk/*  
  
# Installing docker from source to get the version we want  
RUN curl -L https://get.docker.com/builds/Linux/x86_64/docker-$DOCKER_VERSION
\  
> /usr/local/bin/docker && \  
chmod +x /usr/local/bin/docker  
  
# Installing docker-compose from pip  
RUN pip install -U docker-compose==$COMPOSE_VERSION  
  
# Clone dotfiles  
RUN mkdir -p $SOURCE_DIR && \  
cd $SOURCE_DIR && \  
git clone https://github.com/cubez/dotfiles.git && \  
mkdir -p /root/.config/fish/  
  
# Setup symlinks  
ENV DOTFILES $SOURCE_DIR/dotfiles  
RUN ln -s $DOTFILES/fish/config.fish /root/.config/fish/config.fish && \  
ln -s $DOTFILES/nanorc/nanorc /root/.nanorc  
  
WORKDIR /host  
  
CMD ["fish"]

