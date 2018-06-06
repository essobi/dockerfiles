FROM google/golang  
  
MAINTAINER Shun Yanuara <metroplexity@gmail.com>  
  
RUN go get github.com/bketelsen/captainhook  
  
EXPOSE 80  
VOLUME ["/hooks"]  
  
CMD ["captainhook", "-configdir", "/hooks"]  

