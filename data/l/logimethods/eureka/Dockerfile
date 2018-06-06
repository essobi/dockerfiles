## MIT License  
##  
## Copyright (c) 2017 Logimethods  
##  
## Permission is hereby granted, free of charge, to any person obtaining a
copy  
## of this software and associated documentation files (the "Software"), to
deal  
## in the Software without restriction, including without limitation the
rights  
## to use, copy, modify, merge, publish, distribute, sublicense, and/or sell  
## copies of the Software, and to permit persons to whom the Software is  
## furnished to do so, subject to the following conditions:  
##  
## The above copyright notice and this permission notice shall be included in
all  
## copies or substantial portions of the Software.  
##  
## THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR  
## IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,  
## FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE  
## AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER  
## LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM,  
## OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE  
## SOFTWARE.  
  
# https://docs.docker.com/engine/userguide/eng-image/multistage-build/#use-
multi-stage-builds  
# https://github.com/Logimethods/docker-eureka  
FROM logimethods/eureka:entrypoint as entrypoint  
  
### MAIN FROM ###  
  
FROM alpine:3.6  
# https://stedolan.github.io/jq/  
RUN apk --no-cache add \  
jq bash netcat-openbsd  
  
COPY --from=entrypoint eureka_utils.sh /eureka_utils.sh  
COPY --from=entrypoint entrypoint.sh /entrypoint.sh  
  
# OPTIONAL  
COPY entrypoint_insert.sh /entrypoint_insert.sh  
COPY entrypoint_finalize.sh /entrypoint_finalize.sh  
COPY entrypoint_prepare.sh /entrypoint_prepare.sh  
  
# EXPOSE 6868  
# ENV EUREKA_AVAILABILITY_PORT=6868  
  
HEALTHCHECK --interval=5s --timeout=1s --retries=1 CMD test -f
/availability.lock  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ping eureka  

