FROM python:alpine  
RUN apk --update add git gcc musl-dev  
RUN pip3 install pew  
RUN pew new FFA_JOBS_EMAILS  
  
# pymssql on separate line because it's such a pain  
# also, can't just use pymssql until
https://github.com/pymssql/pymssql/issues/432#issuecomment-238257092  
RUN pew in FFA_JOBS_EMAILS pip3 install Django  
  
# for queryset filter in openCasesSameDate  
RUN pew in FFA_JOBS_EMAILS pip install pytz  
RUN pew in FFA_JOBS_EMAILS pip install django_filter  
  
EXPOSE 8000  
WORKDIR /usr/share/ffa-jobs-emails  
COPY . .  
  
COPY docker-entry.sh /usr/bin/  
RUN chmod +x /usr/bin/docker-entry.sh  
  
ENTRYPOINT docker-entry.sh  

