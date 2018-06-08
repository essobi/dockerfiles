#  
# To build:  
# > sudo docker build -t scrapyrt .  
#  
# to start as daemon with port 9080 of api exposed as 9080 on host  
# and host's directory ${PROJECT_DIR} mounted as /scrapyrt/project  
#  
# > sudo docker run -p 9080:9080 -tid -v ${PROJECT_DIR}:/scrapyrt/project
scrapyrt  
#  
FROM ubuntu:14.04  
RUN mkdir -p /scrapyrt/project  
RUN mkdir -p /var/log/scrapyrt  
  
FROM python:2-onbuild  
CMD ["python", "setup.py"]  
  
WORKDIR /scrapyrt/project  
ENV PYTHONPATH=/usr/src/app  
CMD ["python", "-m", "scrapyrt.cmdline", "-i 0.0.0.0"]  
  
EXPOSE 9080  

