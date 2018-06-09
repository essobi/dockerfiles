FROM ubuntu:latest  
  
RUN apt-get update && apt-get install -y \  
luajit \  
luarocks \  
libreadline-dev \  
libconfig-dev \  
libssl-dev \  
lua5.2 \  
liblua5.2-dev \  
libevent-dev \  
libjansson-dev \  
libpython-dev \  
make \  
git \  
python \  
python-pip  
  
RUN pip install --upgrade pip && \  
pip install requests  
  
RUN git clone \--recursive https://github.com/vysheng/tg.git /tg && \  
cd /tg && \  
./configure && \  
cd /tg && \  
make && \  
mv -v /tg/bin/* /usr/bin/ && \  
mkdir -vp /etc/telegram-cli/ && \  
mv -v /tg/tg-server.pub /etc/telegram-cli/server.pub && \  
rm -rf /tg/  
  
ENV TZ=America/Sao_Paulo  
  
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone  
  
RUN mkdir -vp /app  
  
CMD [ "python", "/app/telegram.py" ]  

