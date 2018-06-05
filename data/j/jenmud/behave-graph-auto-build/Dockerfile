FROM alpine  
  
MAINTAINER Jenda Mudron  
  
LABEL Description="Graph visualization for behave features, scenarios, and
steps."  
  
ENV PYTHON_VERSION 2.7.11  
ENV PIP_INDEX_URL https://pypi.python.org/simple/  
  
RUN apk --no-cache add py-pip python git  
RUN git clone https://www.github.com/jenmud/behave-graph.git  
RUN pip install --upgrade pip setuptools wheel && pip install /behave-graph/  
RUN mkdir /my-share  
  
VOLUME /my-share  
WORKDIR /my-share  
  
EXPOSE 80  
ENTRYPOINT ["behave-graph", "--runserver"]  
CMD ["--port", "80"]  

