FROM python  
  
#Install Rasa CORE  
#RUN pip install rasa_core  
#RUN pip install rasa_nlu  
COPY ./dev-requirements.txt /  
COPY ./requirements.txt /  
COPY ./setup.py /  
COPY ./rasa_core/version.py /rasa_core/  
COPY ./README.md /  
RUN pip install -r dev-requirements.txt  
RUN pip install -U spacy  
RUN python -m spacy download en  
RUN pip install -U scikit-learn scipy sklearn-crfsuite  
  
COPY . /  
#ADD ./restaurantbot /  
#CMD ["cd", "examples/restaurantbot"]  
EXPOSE 5005  
WORKDIR "examples/restaurantbot"  
CMD [ "python", "-m", "rasa_core.server", "-d","models/dialogue", "-u",
"models/nlu/current", "-o", "out.log" ]  
#CMD ["ls"]

