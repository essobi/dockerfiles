FROM continuumio/miniconda3:4.2.12  
ENV APP_HOME /app  
ENV FLASK_APP app.py  
EXPOSE 5000  
RUN mkdir $APP_HOME  
WORKDIR $APP_HOME  
  
ADD ./environment.yml $APP_HOME  
RUN conda env update -f environment.yml -n root  
  
ADD . $APP_HOME  
  
CMD /bin/bash -c "flask run --host=0.0.0.0"  

