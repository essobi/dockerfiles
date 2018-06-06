FROM decorist/finds_api:dev  
RUN pip install flower  
COPY entrypoint.sh /  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["-l", "info"]  

