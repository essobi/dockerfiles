FROM mikewright/python3  
  
MAINTAINER "Michael Wright <mkwright@gmail.com>"  
# Install the shunit2 system (for running the tests)  
RUN cd /tmp && \  
curl https://shunit2.googlecode.com/files/shunit2-2.1.6.tgz | tar xvz && \  
mv shunit2-2.1.6 /usr/local/shunit2  
  
# Install the python application  
ADD grader/ /grader  
WORKDIR /grader  
RUN pip3 install -r /grader/requirements.txt  
  
EXPOSE 5000  
# Setup the starting mechanism for docker  
CMD ["/grader/run.sh"]  
ENTRYPOINT ["/bin/bash"]  

