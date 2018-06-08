FROM python:2  
WORKDIR /usr/src/app  
COPY requirements.txt .  
RUN pip install --no-cache-dir -r requirements.txt  
RUN git clone \--depth=1 https://github.com/aquynh/capstone \  
&& cd * \  
&& ./make.sh \  
&& ./make.sh install \  
&& rm -rf ../*  
RUN git clone \--depth=1 https://github.com/xoreaxeaxeax/sandsifter \  
&& mv */* . \  
&& rmdir --ignore-fail-on-non-empty sandsifter \  
&& make  
COPY docker-entrypoint.sh /usr/local/bin/  
ENTRYPOINT ["docker-entrypoint.sh"]  
ENV TERM=xterm-256color  
CMD exec python sifter.py --unk --dis --len --sync --tick -- -P1 -t  

