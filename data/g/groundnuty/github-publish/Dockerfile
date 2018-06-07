FROM python:2-alpine  
  
# Commands from python -onbuild dockerfile  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
COPY requirements.txt /usr/src/app/  
RUN pip install --no-cache-dir -r requirements.txt  
  
COPY . /usr/src/app  
  
# The default working of python:* is /usr/src/app, lets change it  
# ncurses is to have tput command  
RUN apk update && apk add git openssh bash ncurses  
  
ADD config.yml /  
ADD bin /bin  
ENV HOME /root  
RUN mkdir -p ~/.ssh/  
RUN ssh-keyscan -p7999 git.plgrid.pl >> /root/.ssh/known_hosts  
RUN ssh-keyscan -H github.com >> /root/.ssh/known_hosts  
  
ENTRYPOINT ["/bin/loop.sh"]  

