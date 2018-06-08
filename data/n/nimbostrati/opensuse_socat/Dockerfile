FROM nimbostrati/updated_13_1  
MAINTAINER Stephen Moore, stephen.moore@linux.com  
  
RUN zypper update  
RUN zypper --non-interactive install socat  
  
ENTRYPOINT ["socat"]  
  
CMD ["-V"]  

