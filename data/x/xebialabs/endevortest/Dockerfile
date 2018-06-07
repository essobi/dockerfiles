FROM fedora:25  
MAINTAINER Rick Broker <rick.broker@gmail.com>  
  
RUN dnf -y install procps net-tools pcre pcre-static python && \  
dnf clean all  
RUN pip install --upgrade pip  
RUN pip install flask  
RUN mkdir /endevor  
  
ENV FLASK_APP=/endevor/app.py  
ENV FLASK_ENV=development  
  
COPY endevor /endevor  
  
VOLUME /endevor  
  
EXPOSE 5000  
CMD flask run --host=0.0.0.0  

