# Copyright (c) 2017 Matthias Neugebauer <mtneug@mailbox.org>  
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
FROM golang:1.9-alpine AS build  
  
COPY . /go/src/github.com/mtneug/hypochronos  
WORKDIR /go/src/github.com/mtneug/hypochronos  
  
RUN apk add --no-cache make git ca-certificates \  
&& make bin/static/hypochronos-node-helper  
  
FROM scratch  
LABEL maintainer="Matthias Neugebauer <mtneug@mailbox.org>" \  
org.label-schema.schema-version="1.0" \  
org.label-schema.name="hypochronos-node-helper" \  
org.label-schema.version="0.1.0" \  
org.label-schema.description="Timetable Constrained Scheduling for Docker
Swarm" \  
org.label-
schema.usage="https://github.com/mtneug/hypochronos/blob/0.1.0/README.md" \  
org.label-schema.url="https://github.com/mtneug/hypochronos" \  
org.label-schema.vcs-url="https://github.com/mtneug/hypochronos" \  
org.label-schema.docker.debug="docker exec -it $CONTAINER sh" \  
org.label-schema.docker.cmd="docker service create --network 'example'
--constraint 'node.role == manager' --mount
'type=bind,src=/var/run/docker.sock,dst=/var/run/docker.sock'
mtneug/hypochronos-node-helper:0.1.0" \  
org.label-schema.docker.cmd.help="docker run --rm mtneug/hypochronos-node-
helper:0.1.0 --help"  
  
COPY \--from=build
/go/src/github.com/mtneug/hypochronos/bin/static/hypochronos-node-helper /  
COPY \--from=build /usr/share/ca-certificates/mozilla /etc/ssl/certs/  
  
ENTRYPOINT ["/hypochronos-node-helper"]  

