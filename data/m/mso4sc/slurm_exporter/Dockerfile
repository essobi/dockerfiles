# Copyright 2017 MSO4SC - javier.carnero@atos.net  
#  
# Licensed under the Apache License, Version 2.0 (the "License");  
# you may not use this file except in compliance with the License.  
# You may obtain a copy of the License at  
#  
# http://www.apache.org/licenses/LICENSE-2.0  
#  
# Unless required by applicable law or agreed to in writing, software  
# distributed under the License is distributed on an "AS IS" BASIS,  
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  
# See the License for the specific language governing permissions and  
# limitations under the License.  
FROM golang:1.9-alpine  
  
LABEL maintainer="javier.carnero@atos.net"  
  
RUN mkdir /app  
WORKDIR /app  
  
# Install git  
RUN apk add --update --no-cache git  
  
# Get slurm exporter  
RUN go get github.com/mso4sc/slurm_exporter  
  
# Install slurm exporter  
RUN /bin/sh $GOPATH/src/github.com/mso4sc/slurm_exporter/utils/install.sh  
  
EXPOSE 9100  
ENTRYPOINT ["slurm_exporter", "-listen-address", ":9100"]  
  

