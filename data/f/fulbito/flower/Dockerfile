FROM fulbito/webapi-app-code  
  
MAINTAINER Zeta <zetahernandez@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update -y && rm -rf /var/lib/apt/lists/*  
  
RUN pip install flower  
  
EXPOSE 5555  
WORKDIR /usr/src/app  
  
# Running flower  
CMD ["celery", "flower", "-A", "fulbitocore.celeryconf"]

