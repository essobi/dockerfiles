FROM rockkid/codecompass-base  
  
ENV CC_WITHOUT_BUILD 0  
ENV CC_WITHOUT_PARSE 1  
RUN apt-get install --yes gdb  
COPY runner.sh /opt/runner.sh  
RUN chmod +x /opt/runner.sh  
  
EXPOSE 6251  
VOLUME /src/cc  
VOLUME /src/projects  
  
CMD ["./opt/runner.sh"]  

