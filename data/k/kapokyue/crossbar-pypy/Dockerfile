FROM pypy:2  
MAINTAINER kapokyue  
  
EXPOSE 8080  
RUN pip install crossbar[all]  
  
COPY COPY/ /  
  
RUN crossbar version && crossbar check  
  
ENTRYPOINT ["crossbar"]  
CMD ["start"]

