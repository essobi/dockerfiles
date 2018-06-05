FROM tjakobsson/ruby-base:1.0  
MAINTAINER jakobsson.tobias@gmail.com  
  
RUN echo "nameserver 8.8.8.8" > /etc/resolv.conf && \  
gem install neat  
  
ENTRYPOINT ["neat"]  
CMD ["install"]  

