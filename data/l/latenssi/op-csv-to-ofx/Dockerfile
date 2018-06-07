FROM python:3-onbuild  
RUN useradd -ms /bin/bash ofxstatement  
  
COPY op-config /home/ofxstatement/.local/share/ofxstatement/config.ini  
  
USER ofxstatement  
  
EXPOSE 8000  
CMD ["/usr/local/bin/gunicorn", "-w", "2", "-b", ":8000", "app:app"]

