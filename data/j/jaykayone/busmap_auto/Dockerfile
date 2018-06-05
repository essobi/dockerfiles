FROM grahamdumpleton/mod-wsgi-docker:python-2.7  
RUN apt-get update && apt-get install -y python-pip virtualenv git libpq-dev
libproj-dev libgeos-dev libgdal-dev cron  
ENV appdir /app  
WORKDIR /app  
##CREATE VIRTUAL ENV  
RUN mkdir -p ${appdir}  
RUN cd ${appdir} && virtualenv env  
RUN echo alias ll=\'ls -lisa\' >> ~/.bashrc  
RUN /bin/bash -c "source ${appdir}/env/bin/activate && pip install --upgrade
pip && pip install --upgrade setuptools"  
COPY app.wsgi /app/app.wsgi  
COPY getDelayData_full.sh /app/getDelayData_full.sh  
COPY getDelayData_incremental.sh /app/getDelayData_incremental.sh  
COPY cron.sh /app/cron.sh  
COPY startup.sh /app/startup.sh  
RUN /bin/bash -c "chmod o+x *.sh"  
RUN git clone https://github.com/jaykayone/liveBusDelayHeatMap.git  
RUN /bin/bash -c "source ${appdir}/env/bin/activate && pip install -r
${appdir}/liveBusDelayHeatMap/liveBusDelayHeatMap/requirements.txt"  
RUN /bin/bash -c "source ${appdir}/env/bin/activate && cd
${appdir}/liveBusDelayHeatMap/liveBusDelayHeatMap && python setup.py install"  
COPY production.ini
${appdir}/liveBusDelayHeatMap/liveBusDelayHeatMap/production.ini  
RUN chown -R whiskey: ${appdir} && chmod a+x ${appdir}/app.wsgi && chmod 400
${appdir}/liveBusDelayHeatMap/liveBusDelayHeatMap/production.ini  
COPY crontab /app/crontab  
RUN cat crontab >> /etc/crontab  
#RUN ln -sf /proc/1/fd/1 /app/cron_full_latest.log  
#RUN ln -sf /proc/1/fd/1 /app/cron_inc_latest.log  
#DEFINE ENTRYPOINT  
ENTRYPOINT /app/startup.sh  
EXPOSE 80  

