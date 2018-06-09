FROM buildbot/buildbot-worker:master  
COPY buildbot.tac /buildbot/buildbot.tac  
USER root  
RUN pip install kazoo  
USER buildbot  

