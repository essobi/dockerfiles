FROM python:2.7  
# WARNING: BE SURE NOT TO USE THE WORD 'FLOWER' IN THE ENV VARS  
# E.G. VIA LINKING OR MAESTRO-NG: THEY HAVE A SPECIAL MEANING IN FLOWER.  
RUN pip install redis==2.10.5  
RUN pip install https://github.com/mher/flower/zipball/master  
  
ENV FLOWER_PERSISTENT=True  
ENV FLOWER_DEBUG=False  
ENV FLOWER_MAX_WORKERS=10  
ENV FLOWER_AUTO_REFRESH=True  
ENV FLOWER_INSPECT_TIMEOUT=1000  
ENV FLOWER_INSPECT=True  
ENV FLOWER_NATURAL_TIME=True  
ENV FLOWER_PORT=5555  
ENV BROKER_URL=amqp://guest:guest@rabbitmq:5672//  
  
ENV TZ=America/Sao_Paulo  
RUN rm -vf /etc/localtime \  
&& ln -snf /usr/share/zoneinfo/$TZ /etc/localtime \  
&& echo $TZ > /etc/timezone  
  
# Default port  
EXPOSE 5555  
CMD flower --broker=$BROKER_URL  

