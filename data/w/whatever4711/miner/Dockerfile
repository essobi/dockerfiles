FROM alpine AS build  
  
RUN apk add -U --no-cache gcc g++ make autoconf automake libcurl curl-dev
jansson git && \  
git clone https://github.com/pooler/cpuminer.git  
  
WORKDIR /cpuminer  
RUN ./autogen.sh  
RUN CFLAGS="-O3 -Wall -msse2" ./configure  
RUN make  
  
FROM alpine  
RUN apk add -U --no-cache libcurl  
COPY \--from=build /cpuminer/minerd /usr/bin  
ENTRYPOINT ["minerd"]  
CMD ["--help"]  
  

