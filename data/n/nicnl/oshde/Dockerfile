FROM python:3.6  
MAINTAINER nicnl25@gmail.com  
  
# 1] Création de l'arborescence initiale  
RUN mkdir /oshde-orchestrator  
WORKDIR /oshde-orchestrator  
  
# 2] Installation des requirements python  
COPY requirements.txt requirements.txt  
RUN pip install -r requirements.txt  
  
# 3] Intégration des sources  
COPY src src  
WORKDIR /oshde-orchestrator/src  
  
# 4] On est prêts, on lance tout  
ENTRYPOINT ["python", "-u", "main.py"]  

