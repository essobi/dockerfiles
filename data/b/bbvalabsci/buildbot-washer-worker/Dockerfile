FROM python:3.6 as builder  
  
# Install dependencies.  
COPY requirements.txt ./  
RUN pip install -r requirements.txt  
  
# Compile worker startup script with Nuitka.  
COPY worker.py ./  
RUN python -m nuitka --standalone -j5 --python-flag=-S worker.py  
  
# Prepare the distribution directory.  
RUN mv worker.dist /washer  
RUN cp /washer/worker.exe /washer/buildbot-worker  
RUN ldd /washer/buildbot-worker | awk '/=>/ && !/\/washer/ {print $3}' | xargs
-I{} cp -nv {} /washer/  
  
# Copy entrypoint and set permissions.  
COPY entrypoint.sh /washer  
RUN chmod a+x /washer/entrypoint.sh  
  
FROM alpine:latest  
COPY \--from=builder /washer /washer  
CMD ["/washer/entrypoint.sh"]  

