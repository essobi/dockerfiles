FROM debian:8.6  
RUN apt-get update && \  
apt-get install -y make build-essential libssl-dev zlib1g-dev \  
libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \  
libncurses5-dev libncursesw5-dev xz-utils git bash && \  
useradd -m -u 900 debian && \  
rm -rf /var/lib/apt/lists/*  
WORKDIR /home/debian  
COPY .bash_profile /home/debian/  
RUN chown debian:debian .bash_profile  
USER debian  
ENV TERM=xterm  
RUN git clone https://github.com/yyuu/pyenv.git .pyenv  

