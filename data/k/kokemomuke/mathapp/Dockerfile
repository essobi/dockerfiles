#\-----------------------------------------------------------------------------  
## NOT TESTED, SHOULD TEST THIS IN FUTURE!!!!  
  
#FROM golang:1.6  
#  
## Create the directory where the application will reside  
#RUN mkdir /app  
#  
## Copy the application files (needed for production)  
#ADD MathApp /app/MathApp  
#ADD views /app/views  
#ADD conf /app/conf  
#  
## Set the working directory to the app directory  
#WORKDIR /app  
#  
## Expose the application on port 8080.  
## This should be the same as in the app.conf file  
#EXPOSE 8080  
#  
## Set the entry point of the container to the application executable  
#ENTRYPOINT /app/MathApp  
  
#\-----------------------------------------------------------------------------  
  
## Start from a Debian image with the latest version of Go installed  
## and a workspace (GOPATH) configured at /go.  
#FROM golang  
#  
## Copy the local package files to the container's workspace.  
#RUN go get github.com/astaxie/beego && go get github.com/beego/bee  
#RUN go get github.com/KanybekMomukeyev/MathApp  
#  
##ADD . /go/src/github.com/astaxie/beego  
##ADD . /go/src/github.com/KanybekMomukeyev/MathApp  
#  
#RUN go install github.com/KanybekMomukeyev/MathApp  
#  
## Run the outyet command by default when the container starts.  
#ENTRYPOINT /go/bin/MathApp  
#  
## Document that the service listens on port 8080.  
#EXPOSE 8080  
  
  
  
  
FROM google/golang  
  
WORKDIR /gopath/src/github.com/KanybekMomukeyev/MathApp  
  
ADD . /gopath/src/github.com/KanybekMomukeyev/MathApp/  
  
ADD views /gopath/src/github.com/KanybekMomukeyev/MathApp/views  
ADD conf /gopath/src/github.com/KanybekMomukeyev/MathApp/conf  
  
# go get all of the dependencies  
RUN go get github.com/astaxie/beego && go get github.com/beego/bee  
RUN go get github.com/KanybekMomukeyev/MathApp  
  
EXPOSE 8080  
CMD []  
#ENTRYPOINT ["/gopath/bin/MathApp"]  
ENTRYPOINT /go/bin/MathApp  

