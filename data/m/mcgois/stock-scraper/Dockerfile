FROM python  
MAINTAINER Matheus Cabral <matheus.cabral@gmail.com>  
  
# install cron  
RUN apt-get update -y  
RUN apt-get install cron -y  
  
# workdir  
WORKDIR /usr/src/app  
  
# instala dependencias do python do projeto  
COPY requirements.txt ./  
RUN pip install --no-cache-dir -r requirements.txt  
  
# copia arquivos  
COPY stockscraper.py main.py /usr/src/app/  
  
# configura cron  
COPY crontab /etc/cron.d/stock-cron  
RUN chmod 0644 /etc/cron.d/stock-cron  
RUN touch /var/log/cron.log  
  
# 1) exporta as variaveis de ambiente ser usado do cron  
# 2) roda o cron  
# 3) monitora o log  
CMD printenv | sed 's/^\\(.*\\)$/export \1/g' > /root/project_env.sh && cron
&& tail -f /var/log/cron.log  

