FROM ubuntu:17.04  
RUN apt-get update  
  
RUN apt-get install -y bash beef bc bison curl clang clisp coreutils erlang
flex g++ \  
gawk gfortran ghc git \  
gnuplot golang graphviz guile imagemagick inkscape kbtin \  
lua5.3 m4 make mono-mcs \  
nasm ocaml-nox \  
openjdk-9-jdk perl php7.0 python python3 python-imageio python3-imageio \  
ruby rustc scala sqlite \  
jq vim-nox zip zsh  
  
# ubuntu's nodejs is too old  
RUN curl -sL https://deb.nodesource.com/setup_7.x | bash - &&\  
apt-get install -y nodejs && \  
npm install -g typescript  
  
# ubuntu's phantomjs require X  
RUN apt-get install -y fonts-takao-gothic fontconfig phantomjs xvfb  
  
COPY ./local /usr/local  
COPY bashrc /home/bot/.bashrc  
  
RUN apt-get -y purge curl && apt-get -y autoremove && apt-get clean && rm -rf
/tmp/*  
  
RUN useradd bot && chown -R bot:bot /home/bot  
  
RUN echo 'set terminal png font "/usr/share/fonts/truetype/takao-
gothic/TakaoPGothic.ttf"' > /home/bot/.gnuplot  
  
USER bot  
  
WORKDIR /home/bot  
  

