FROM grahamdumpleton/mod-wsgi-docker:python-3.5-onbuild  
RUN apt-get update && apt-get -y install libyajl2 python3-yaml  
RUN pip3 install bottle pyyaml elasticsearch elasticsearch-dsl ijson yajl
mimerender rdflib rdflib-jsonld urllib3  
  
#RUN mkdir /ops-search  
#ADD src /ops-search  
ADD ./conf/openphacts.yaml /app/config.yaml  
#WORKDIR /app  
#EXPOSE 8839  
CMD ["src/search.wsgi"]  
#CMD ["src/run.wsgi"]  

