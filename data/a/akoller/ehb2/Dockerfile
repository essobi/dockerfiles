FROM phusion/baseimage  
  
RUN apt-get update  
RUN apt-get install -y python3-dev python3-pip git  
  
# install Latex; takes about 250 MB  
# This sets default paper size to Letter; keep an eye on that.  
RUN apt-get -y --no-install-recommends install texlive-base texlive-generic-
recommended texlive-latex-base texlive-pictures texlive-fonts-recommended
texlive-font-utils pgf  
  
RUN pip3 install --upgrade pip  
RUN pip3 install pymysql Flask sqlalchemy Flask-SQLAlchemy-Session wtforms
paypalrestsdk XlsxWriter openpyxl tornado flask_login numpy  
  
COPY *.py /ehb2/  
COPY ehb-public.conf /ehb2/  
COPY templates/ /ehb2/templates/  
COPY static/ /ehb2/static/  
  
EXPOSE 5000  
WORKDIR /ehb2  
ENTRYPOINT ["python3", "-u", "main.py"]  
  

