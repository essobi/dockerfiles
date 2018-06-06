FROM ubuntu  
RUN apt-get update  
RUN apt-get install -y git curl build-essential vim  
RUN apt-get install -y python python-dev python-distribute python-pip  
RUN git clone https://github.com/joe-practice/github_watchdog.git  
RUN pip install -r /github_watchdog/requirements.txt  
WORKDIR /github_watchdog  
CMD /github_watchdog/github_watchdog.py  

