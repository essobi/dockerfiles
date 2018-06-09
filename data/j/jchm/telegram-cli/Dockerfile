FROM ubuntu  
RUN apt-get update && apt-get install -y \  
git \  
libconfig-dev \  
libevent-dev \  
libjansson-dev \  
liblua5.2-dev \  
libpython-dev \  
libreadline-dev \  
libssl-dev \  
lua5.2 \  
make \  
python  
RUN git clone \--recursive https://github.com/vysheng/tg.git /root/tg  
WORKDIR /root/tg  
RUN ./configure && make  
ENV PATH /root/tg/bin/:$PATH  
ENTRYPOINT ["telegram-cli"]

