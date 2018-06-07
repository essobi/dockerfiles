FROM jrottenberg/ffmpeg  
MAINTAINER Edward Mario (edward.mario@gmail.com)  
RUN apt-get install -y python  
RUN mkdir /convert /done  
COPY convert.py /tmp/workdir/  
ENTRYPOINT ["python","convert.py"]  
CMD ["/convert", "/done"]  

