FROM canelrom1/debian-canel:latest  
  
LABEL maintainer="Rom1 <rom1@canel.ch> \- CANEL - https://www.canel.ch"  
LABEL date="07/01/18"  
LABEL description="z80pack: Simulator for Z80, 8080 CP/M(1,2,3) MP/M -
http://www.autometer.de/unix4fun/z80pack/"  
  
RUN apt-get update \  
&& apt-get upgrade -y -q \  
&& apt-get -y -q --no-install-recommends \  
install build-essential \  
git \  
locales \  
ssh-client \  
tmux \  
vim \  
wget  
RUN sed -i 's/# fr_CH.UTF-8 UTF-8/fr_CH.UTF-8 UTF-8/' /etc/locale.gen \  
&& locale-gen fr_CH.UTF-8  
ENV LANG fr_CH.UTF-8  
ENV LANGUAGE fr_CH.UTF-8  
ENV LC_ALL fr_CH.UTF-8  
ENV LC_CTYPE fr_CH.UTF-8  
ENV Z80PACK_VERSION 1.36  
RUN wget -P /tmp
http://www.autometer.de/unix4fun/z80pack/ftp/z80pack-${Z80PACK_VERSION}.tgz \  
&& tar -zxvf /tmp/z80pack-${Z80PACK_VERSION}.tgz -C /tmp  
  
WORKDIR /tmp/z80pack-${Z80PACK_VERSION}/z80sim/srcsim  
RUN make -f Makefile.linux \  
&& cp z80sim /usr/local/bin  
  
WORKDIR /tmp/z80pack-${Z80PACK_VERSION}/z80asm  
RUN make \  
&& cp z80asm /usr/local/bin  
  
WORKDIR /tmp/z80pack-${Z80PACK_VERSION}/cpmsim/srctools  
RUN make bin2hex \  
&& cp bin2hex /usr/local/bin  
  
RUN mkdir /home/z80  
WORKDIR /home  
  
COPY ./entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  

