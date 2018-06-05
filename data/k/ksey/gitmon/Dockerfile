#  
# A program for automating the polling of commits and releases  
# sections of any repository on github.com and performing  
# the actions specified by the user.  
#  
# See gitmon.conf - https://github.com/MrKsey/GitMon/tree/master/examples  
#  
FROM python:alpine  
MAINTAINER Bob <kcey@mail.ru>  
  
COPY gitmon.py cfg.py setup.py actions.py requirements.txt
examples/gitmon.conf /tmp/  
  
RUN mkdir -p /usr/src/gitmon/data \  
&& cp /tmp/*.py /usr/src/gitmon/ \  
&& cp /tmp/requirements.txt /usr/src/gitmon/ \  
&& cp /tmp/gitmon.conf /usr/src/gitmon/data/ \  
&& pip install --no-cache-dir -r /usr/src/gitmon/requirements.txt \  
&& rm -rf /tmp/*  
  
WORKDIR /usr/src/gitmon  
  
VOLUME [ "/usr/src/gitmon/data" ]  
  
CMD [ "python", "./gitmon.py", "--config", "data/gitmon.conf", "--data",
"data/data.json" ]  

