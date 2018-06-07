FROM prologic/python-runtime:2.7  
ENTRYPOINT ["zerobin"]  
  
RUN pip install zerobin  
  
EXPOSE 80  
CMD ["--compressed-static", "true", "--host", "0.0.0.0", "--port", "80"]  

