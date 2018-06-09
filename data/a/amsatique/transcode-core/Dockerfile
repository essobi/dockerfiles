FROM golang:latest  
MAINTAINER Francois Dazan  
  
#Go  
ADD keys/core_key /root/.ssh/id_rsa  
RUN chmod 700 /root/.ssh/id_rsa  
RUN echo "Host bitbucket.org\n\tStrictHostKeyChecking no\n" >>
/root/.ssh/config  
RUN git config --global url.ssh://git@bitbucket.org/.insteadOf
https://bitbucket.org/  
RUN go get -d bitbucket.org/4pjt/transcode-core  
RUN go get -u github.com/jteeuwen/go-bindata/...  
RUN go generate bitbucket.org/4pjt/transcode-core  
RUN go install bitbucket.org/4pjt/transcode-core  
  
# Expose port  
EXPOSE 3000  
# Executing node  
CMD ["transcode-core"]  

