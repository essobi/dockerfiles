# Copyright 2017 Nirmal Kumar  
# This file is part of LibreRead.  
# LibreRead is free software: you can redistribute it and/or modify  
# it under the terms of the GNU Affero General Public License as published by  
# the Free Software Foundation, either version 3 of the License, or  
# (at your option) any later version.  
# LibreRead is distributed in the hope that it will be useful,  
# but WITHOUT ANY WARRANTY; without even the implied warranty of  
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the  
# GNU Affero General Public License for more details.  
# You should have received a copy of the GNU Affero General Public License  
# along with LibreRead. If not, see <http://www.gnu.org/licenses/>.  
FROM golang:alpine as builder  
RUN apk add --no-cache musl-dev gcc git  
WORKDIR /go/src/github.com/LibreRead/server  
COPY . .  
RUN go get -d -v ./...  
RUN go install -v ./...  
  
FROM alpine  
RUN apk add --no-cache unzip poppler-utils ca-certificates  
WORKDIR /libreread  
ENV LIBREREAD_ASSET_PATH "/usr/local/share/libreread"  
COPY templates $LIBREREAD_ASSET_PATH/templates  
COPY static $LIBREREAD_ASSET_PATH/static  
COPY \--from=builder /go/bin/libreread /usr/bin/libreread  
VOLUME /libreread  
EXPOSE 8080  
ENTRYPOINT ["libreread"]  

