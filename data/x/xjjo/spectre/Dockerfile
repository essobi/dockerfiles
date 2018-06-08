# First Stage - build  
FROM gcc:7  
COPY spectre.c /usr/src/  
WORKDIR /usr/src  
RUN gcc -std=c99 -O0 -static spectre.c -o spectre  
  
# Second Stage - just the static binary  
FROM alpine  
COPY \--from=0 /usr/src/spectre /spectre  
CMD ["/spectre"]  

