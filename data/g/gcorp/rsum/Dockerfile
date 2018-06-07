FROM gcorp/rsum:build  
MAINTAINER duchess@gahan-corporation.com  
WORKDIR /srv  
ENV PYTHONPATH /srv/rsum  
ENV RSUM_ENV dev  
ENV DJANGO_SETTINGS_MODULE rsum.settings  
ENV CC_TEST_REPORTER_ID
c154ee2ef2b2fbf68d59c8102b7adef7677728a44f379589dbee6f1d92aebaf8  
ENV CODACY_PROJECT_TOKEN 16dae58cf59049eda9c6d34c207c5d54  
ENV PGHOST postgres  
ENV PGUSER xander  
RUN rm -rf /usr/lib/python3.6/site-packages/rsum*  
RUN git clone https://github.com/gahan-corporation/rsum.git  
WORKDIR /srv/rsum  
RUN git fetch -p; git checkout v0.1.2; git checkout -b current  
RUN pip uninstall -y rsum || true; pip uninstall -y rsum || true; python
setup.py build; python setup.py install  
COPY create /bin/create  
RUN apk update; apk add bash  
CMD /bin/create  

