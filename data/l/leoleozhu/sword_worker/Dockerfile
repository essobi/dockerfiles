FROM python:3  
RUN apt-get update && apt-get install -y alien  
  
ADD 3rd_party/viesus-*.rpm /tmp  
RUN alien --script -i /tmp/viesus-*.rpm  
RUN rm -rf /tmp/viesus-*.rpm  
  
ENV workdir /workdir-sword  
RUN mkdir -p ${workdir}  
WORKDIR ${workdir}  
  
ADD requirements.txt ${workdir}  
RUN pip install -r requirements.txt  
  
ADD sword ${workdir}/sword  
  
ENTRYPOINT ["celery", "-E", "-A", "sword.tasks", "worker"]  

