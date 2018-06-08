FROM grahamdumpleton/mod-wsgi-docker:python-2.7-onbuild  
RUN mkdir -p /app/instance/ && ln -s /run/secrets/gz_nodes.cfg
/app/instance/gz_nodes.cfg  
CMD ["gz_nodes_wsgi.py"]  

