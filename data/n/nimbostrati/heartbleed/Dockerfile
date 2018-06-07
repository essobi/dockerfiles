FROM nimbostrati/opensuse_go_1_2  
MAINTAINER Stephen Moore, stephen.moore@linux.com  
  
RUN zypper --non-interactive install git  
  
RUN go get github.com/FiloSottile/Heartbleed  
RUN go install github.com/FiloSottile/Heartbleed  
  
ENTRYPOINT ["Heartbleed"]  
  
CMD ["google.com:443"]  

