FROM nsls2/debian-with-miniconda:latest  
  
USER root  
COPY . /home/builder/app  
RUN chown -R builder /home/builder  
USER builder  
WORKDIR /home/builder/app  
RUN pip install -r server-requirements.txt  
RUN pip install -e .  
  
ENTRYPOINT ["python"]  
CMD ["exceptional/app.py"]  

