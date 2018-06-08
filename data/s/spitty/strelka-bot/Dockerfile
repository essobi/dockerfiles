FROM debian:jessie  
MAINTAINER spitty.pnz@gmail.com  
  
ARG TAG  
ENV TAG ${TAG:-latest}  
LABEL version=$TAG  
  
RUN apt-get update  
RUN apt-get install -y \  
git \  
python-dev \  
python-pip  
  
RUN git clone https://github.com/spitty/strelka_telegram_bot.git  
  
WORKDIR /strelka_telegram_bot  
RUN git checkout -b $TAG $TAG  
RUN pip install -r requirements.txt  
  
VOLUME ["/strelka_data"]  
ENV STRELKA_STORED_FILE /strelka_data/strelka_bot_shelve.db  
ENV STRELKA_TOKEN_FILE /strelka_data/token.lst  
  
ENTRYPOINT ["python", "strelka_bot.py"]  

