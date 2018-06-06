FROM java:7  
  
ENV CLASSYSHARK_VERSION 6.4  
  
ADD https://github.com/google/android-
classyshark/releases/download/${CLASSYSHARK_VERSION}/ClassyShark.jar
/usr/local/lib/classyshark/  
  
ADD docker-entrypoint.sh /  
ENTRYPOINT ["/docker-entrypoint.sh"]  

