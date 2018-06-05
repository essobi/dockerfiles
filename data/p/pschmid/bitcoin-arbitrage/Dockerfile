FROM python:3  
LABEL maintainer="Philip Schmid"  
  
RUN useradd -ms /bin/bash serviceuser  
RUN mkdir -p /opt/app  
RUN chown serviceuser:serviceuser -R /opt/app  
  
WORKDIR /opt/app  
  
COPY . .  
  
USER serviceuser  
  
CMD [ "python", "-m", "arbitrage" ]  

