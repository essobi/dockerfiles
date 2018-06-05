FROM tjakobsson/ruby-base:1.0  
MAINTAINER jakobsson.tobias@gmail.com  
  
RUN echo "nameserver 8.8.8.8" > /etc/resolv.conf && \  
gem install bourbon -v 5.0.0.beta.7  
  
ENTRYPOINT ["bourbon"]  
CMD ["install"]  

