FROM deviantony/python:python2  
  
COPY valigator.yml /etc/valigator/valigator.yml  
  
# TODO: Fix the warning related to Celery worker running with super
privileges.  
# RUN adduser -S -D -H valigator -G root  
# USER valigator  
CMD ["/env/bin/python", "-m", "valigator.valigator"]  

