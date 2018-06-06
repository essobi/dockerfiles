FROM python  
RUN git clone https://github.com/hjptriplebee/Chinese_poem_generator.git & pip
install tensorflow  
WORKDIR Chinese_poem_generator  
COPY main.py ./  
ENTRYPOINT ["python","main.py"]  

