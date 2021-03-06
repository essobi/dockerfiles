FROM qmxme/workstation-box:latest  
COPY \--from=qmxme/golang-tools:latest /usr/local/go /usr/local/go  
RUN apt-get update && apt-get install -qq -y \  
build-essential \  
clang \  
cmake \  
default-libmysqlclient-dev \  
direnv \  
gdb \  
git \  
git-crypt \  
htop \  
jq \  
less \  
libclang-dev \  
liblzma-dev \  
libofx-dev \  
libpq-dev \  
libsqlite3-dev \  
libssl-dev \  
lldb \  
mtr-tiny \  
neovim \  
pkg-config \  
pwgen \  
python \  
python3 \  
python3-pip \  
shellcheck \  
sqlite3 \  
stow \  
sudo \  
tmate \  
unzip \  
zgen \  
zip \  
zlib1g-dev \  
zsh \  
\--no-install-recommends \  
&& rm -rf /var/lib/apt/lists/*  
  
ARG user=qmx  
ARG uid=1000  
ARG github_user=qmx  
RUN useradd -m $user -u $uid -G users,sudo,docker -s /bin/zsh  
# user setup  
USER $user  
RUN mkdir ~/.ssh && curl -fsL https://github.com/$github_user.keys >
~/.ssh/authorized_keys && chmod 700 ~/.ssh && chmod 600 ~/.ssh/authorized_keys  
RUN mkdir -p /home/$user/bin /home/$user/.cargo/bin  
  
# rust essential crates  
COPY \--from=qmxme/rust-tools:latest /opt/rust-tools/bin/*
/home/$user/.cargo/bin/  
  
# golang + vim-go tools  
COPY \--from=qmxme/golang-tools:latest /go/bin/* /home/$user/bin/  
  
# universal-ctags  
COPY \--from=qmxme/universal-ctags:latest /opt/local/bin/ctags /home/$user/bin  
  
# neovim and python dependencies  
RUN python3 -m pip install setuptools && python3 -m pip install wheel &&
python3 -m pip install neovim && python3 -m pip install flake8 && python3 -m
pip install autopep8  
  
RUN git clone https://github.com/qmx/dotfiles.git ~/.dotfiles  
RUN mkdir -p ~/.config  
RUN cd ~/.dotfiles && stow .  
RUN zsh ~/.zshrc || true  
RUN nvim +PlugInstall +qall 2> /dev/null > /dev/null  
RUN curl -sSf https://sh.rustup.rs | zsh -s -- -y  
RUN /home/$user/.cargo/bin/rustup component add rust-src  
RUN /home/$user/.cargo/bin/rustup toolchain install nightly  
RUN /home/$user/.cargo/bin/rustup component add rustfmt-preview  
RUN /home/$user/.cargo/bin/rustup component add rls-preview  
RUN /home/$user/.cargo/bin/rustup component add rust-analysis  
  
VOLUME ["/mnt/codez"]  
VOLUME ["/mnt/secrets"]  
VOLUME ["/home/$user/.cargo/registry"]  
  
USER root  
ENV TARGET_USER=$user  
COPY entrypoint /bin/entrypoint  
ENTRYPOINT ["/bin/entrypoint"]  
CMD ["/usr/sbin/sshd", "-D"]  

