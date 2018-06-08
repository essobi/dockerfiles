# Copyright 2014 The Go Authors. All rights reserved.  
# Use of this source code is governed by a BSD-style  
# license that can be found in the LICENSE file.  
FROM goli/go-playground-sandbox80  
  
# add dir for gccgo  
RUN mkdir -p /opt  
  
# add gccgo from /opt  
ADD gccgo.tar.gz /opt  
RUN tar -xf /opt/gccgo.tar -C /opt  
RUN rm /opt/gccgo.tar  
  
# add and compile sandbox daemon  
COPY . /go/src/gccbox  
RUN go install gccbox  
  
EXPOSE 80  
ENTRYPOINT ["/go/bin/gccbox"]  

