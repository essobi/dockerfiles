FROM ubuntu:rolling  
LABEL maintainer='amritanshu16@outlook.com'  
RUN apt update -y && apt upgrade -y  
RUN apt install -y \  
build-essential curl git locales nano neofetch openvpn openssh-server python3
sudo tree shellcheck vim wget zsh \  
make build-essential libssl-dev zlib1g-dev libbz2-dev \  
libreadline-dev libsqlite3-dev llvm libncurses5-dev libncursesw5-dev \  
xz-utils tk-dev  
RUN useradd -ms /bin/bash xps  
RUN echo "xps ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/xps && \  
chmod 0440 /etc/sudoers.d/xps  
ADD copy-to-home-in-container /copy-to-home-in-container  
RUN cp -rT /copy-to-home-in-container /home/xps  
RUN chown -R xps /home/xps  
RUN locale-gen en_US.UTF-8  
ENV LANG='en_US.UTF-8' LANGUAGE='en_US:en' LC_ALL='en_US.UTF-8'  
USER xps  
WORKDIR /home/xps  
RUN sudo sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-
zsh/master/tools/install.sh)"  
RUN sudo chown -R xps .oh-my-zsh .zshrc  
RUN sudo chsh -s $(which zsh)  
RUN git clone git://github.com/yyuu/pyenv.git ~/.pyenv  
RUN git clone https://github.com/yyuu/pyenv-virtualenv.git
~/.pyenv/plugins/pyenv-virtualenv  
ENV HOME /home/xps  
ENV PYENV_ROOT $HOME/.pyenv  
ENV PATH $PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH  
RUN git clone https://github.com/nodenv/nodenv.git ~/.nodenv  
RUN cd ~/.nodenv && src/configure && make -C src && cd ~  
RUN echo 'export PATH="$HOME/.nodenv/bin:$PATH"' >> ~/.zshrc  
RUN git clone https://github.com/nodenv/node-build.git
$($HOME/.nodenv/bin/nodenv root)/plugins/node-build  
RUN echo "\nneofetch\n" >> /home/xps/.zshrc  
ADD bootstrap.sh /home/xps/bootstrap.sh  
RUN sudo chmod +x bootstrap.sh  
RUN bash /home/xps/bootstrap.sh  
CMD echo 'Execute /bin/zsh while instantiating the container \ndocker run -it
<image> /bin/zsh'

