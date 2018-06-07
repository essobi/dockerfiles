FROM ubuntu:16.04  
ENV DEBUG_COLORS true  
ENV FORCE_COLOR true  
ENV DEBIAN_FRONTEND noninteractive  
ENV NVM_DIR /usr/local/nvm  
ENV PATH
$NVM_DIR/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH  
  
RUN dpkg --add-architecture i386  
RUN apt update -qq  
RUN apt install --no-install-recommends -y wget python rpm g++-multilib
libxss-dev build-essential pkg-config libx11-dev:i386 libxext-dev:i386 libxss-
dev:i386 libssl-dev ca-certificates snapcraft locales  
RUN wget -qO-
https://raw.githubusercontent.com/creationix/nvm/v0.33.0/install.sh | bash  
RUN echo 'source $NVM_DIR/nvm.sh' >> /etc/profile  
RUN /bin/bash -l -c "nvm install 9"  
RUN mkdir yarn && wget -qO- https://yarnpkg.com/latest.tar.gz | tar xvz -C
yarn && mv ./yarn/* /opt/yarn  
  
WORKDIR /project  
  
# fix error /usr/local/bundle/gems/fpm-1.5.0/lib/fpm/package/freebsd.rb:72:in
`encode': "\xE2" from ASCII-8BIT to UTF-8 (Encoding::UndefinedConversionError)  
# http://jaredmarkell.com/docker-and-locales/  
# http://askubuntu.com/a/601498  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
ENV PATH "/opt/yarn/bin:$PATH"  

