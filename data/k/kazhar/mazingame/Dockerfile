FROM python:3.6.4  
LABEL maintainer="Sami Salkosuo"  
LABEL source_url="https://github.com/samisalkosuo/mazingame"  
  
WORKDIR /mazingame  
  
#install mazepy requirement and make data-directory that holds scores and game
history  
RUN pip install mazepy \  
&& mkdir /data  
  
VOLUME [ "/data" ]  
  
#copy mazingame files  
COPY mazingame/ ./mazingame/  
COPY mazingame-runner.py ./  
  
#set TERM so that console works correctly  
ENV TERM xterm  
  
COPY scripts/run_mazingame.sh ./  
  
#set correct permissions  
RUN chmod 755 *.sh  
  
ENTRYPOINT ["/bin/bash", "-c", "./run_mazingame.sh \"$@\"", "--"]  
  
#CMD ["/bin/bash"]  

