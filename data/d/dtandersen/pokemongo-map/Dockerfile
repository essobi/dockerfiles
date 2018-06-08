FROM python:2.7.12-alpine  
#FROM alpine:3.3  
RUN apk --update add git build-base nodejs  
#RUN apk --update add python py-pip nodejs git gcc libgcc libstdc++ g++
python-dev build-base  
RUN git clone -b develop --single-branch
https://github.com/PokemonGoMap/PokemonGo-Map.git /opt/PokemonGo-Map \  
&& cd /opt/PokemonGo-Map \  
&& rm -r .git \  
&& pip install --upgrade pip -r requirements.txt \  
&& npm install \  
&& npm install -g grunt-cli \  
&& grunt build  
  
EXPOSE 5000  
#ENV SCAN_DELAY=15 STEP_LIMIT=4 HOST=0.0.0.0 PORT=5000  
#COPY entrypoint.sh .  
#RUN chmod 550 entrypoint.sh  
WORKDIR /opt/PokemonGo-Map  
#CMD /entrypoint.sh  
ENTRYPOINT ["python", "runserver.py"]  
CMD ["-h"]  

