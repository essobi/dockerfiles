FROM appropriate/curl:latest  
  
#ENV REPOSITORY stretch  
ENV DISTRIBUTION ffda  
ENV CURL_OPTS ''  
ENV APTLY_API_BASE 'https://apt.ffda.io/api'  
ADD publish.sh /publish.sh  
  
CMD /publish.sh  

