FROM python:stretch  
  
ENV TZ=Europe/Berlin  
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone  
  
RUN apt-get update \  
&& export DEBIAN_FRONTEND="noninteractive" \  
&& apt-get install -y cron \  
&& rm -rf /var/lib/apt/lists/* \  
&& git clone https://github.com/webcomics/dosage.git \  
&& cd dosage \  
&& pip install --no-cache-dir -r requirements.txt \  
&& /usr/local/bin/python setup.py install \  
&& cd / \  
&& rm -r dosage  
  
RUN mkdir /Comics && mkdir /templates  
COPY download.sh .  
COPY redirect.php /templates  
COPY index.php /templates  
COPY run.sh .  
RUN chmod +x download.sh && chmod +x run.sh  
COPY dosage-cron /etc/cron.d/  
RUN chmod +x /etc/cron.d/dosage-cron  
  
# Create the log file to be able to run tail  
RUN touch /var/log/cron.log  
  
ENTRYPOINT ["/run.sh"]

