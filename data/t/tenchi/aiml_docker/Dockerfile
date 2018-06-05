FROM ubuntu:16.04  
MAINTAINER Alexey Vinogradov <aleksey.vinogradov@rt.ru>  
  
RUN apt-get update  
  
RUN apt-get -q -y install python3-dev git python3-pip locales  
RUN pip3 install --upgrade pip  
RUN pip3 install --no-cache-dir virtualenv  
RUN localedef -i en_US -f UTF-8 en_US.UTF-8  
  
CMD virtualenv venv && /bin/bash -c "source venv/bin/activate" && git clone
https://github.com/Tenchi88/smart_telegram_bot.git && pip3 install -r
smart_telegram_bot/requirements.txt && python3
smart_telegram_bot/helpers/openshift.py && chmod 400 ~/.ssh/git_lab && ssh-
keyscan -H git.digital.rt.ru >> ~/.ssh/known_hosts && ssh-agent bash -c 'ssh-
add ~/.ssh/git_lab; git clone
git@git.digital.rt.ru:aleksey.vinogradov/AIML.git' && cd AIML && python3
smart_bot.py  

