FROM debian:unstable-20170907  
RUN apt-get -y update && \  
apt-get -y install z3 git curl build-essential time ghc && \  
apt-get -y clean autoclean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN curl -L
https://github.com/commercialhaskell/stack/releases/download/v1.5.1/stack-1.5.1-linux-x86_64-static.tar.gz
| \  
tar xz --wildcards --strip-components=1 -C /usr/local/bin '*/stack'  
  
# force https on github instead of ssh  
RUN git config --system url."https://github.com/".insteadOf "git@github.com:"  
  
RUN useradd -m popl18  
USER popl18  
  
# use system ghc  
RUN stack config set system-ghc --global true  
  
WORKDIR /home/popl18  
RUN git clone \--depth 10 -b popl18 --recursive https://github.com/ucsd-
progsys/liquidhaskell.git  
WORKDIR /home/popl18/liquidhaskell  
ENV PATH "/home/popl18/.local/bin:${PATH}"  
RUN stack install  
RUN stack test liquidhaskell --no-run-tests  
  
WORKDIR /home/popl18  
RUN git clone \--depth 10 -b popl18 --recursive https://github.com/iu-
parfunc/verified-instances.git  
WORKDIR /home/popl18/verified-instances  
RUN make build  
  
WORKDIR /home/popl18  
RUN git clone \--depth 10 -b popl18 --recursive https://github.com/iu-
parfunc/lvars.git  
WORKDIR /home/popl18/lvars  
RUN make build  
  
CMD cd /home/popl18/liquidhaskell && \  
stack test liquidhaskell || true && \  
cd /home/popl18/verified-instances && \  
make check && \  
cd /home/popl18/lvars && \  
make check  

