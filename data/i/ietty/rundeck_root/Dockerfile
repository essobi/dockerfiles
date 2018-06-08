From jordan/rundeck  
  
MAINTAINER takemi.ohama takemi.ohama@gmail.com  
  
RUN apt-get update  
RUN apt-get install -y locales task-japanese vim  
  
RUN sed -i -e "s/# ja_JP.UTF-8 UTF-8/ja_JP.UTF-8 UTF-8/" /etc/locale.gen  
RUN locale-gen  
RUN update-locale LANG=ja_JP.UTF-8 LANGUAGE="ja_JP:ja"  
RUN cat /etc/mysql/my.cnf  
RUN sed -i -e "s/127.0.0.1/0.0.0.0\ncharacter-set-server=utf8\n/g"
/etc/mysql/my.cnf  
  
RUN echo "export LANG=ja_JP.UTF-8" >> /root/.bashrc  
RUN echo "export LANG=ja_JP.UTF-8" >> /etc/profile  
RUN echo "export LANG=ja_JP.UTF-8" >> /etc/rundeck/profile  
RUN echo "export PYTHONPATH=/var/rundeck" >> /etc/profile  
RUN echo "export PYTHONPATH=/var/rundeck" >> /etc/rundeck/profile  
  

