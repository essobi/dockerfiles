FROM golang:1.6.0  
MAINTAINER Anton Martsen <amartsen@le-talo.ru>  
  
# More info on site https://getgb.io && https://getgb.io/faq/#missing-race-
support  
RUN go get github.com/constabulary/gb/... && go install -a -race std  

