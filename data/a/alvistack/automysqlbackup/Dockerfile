# (c) Wong Hoi Sing Edison <hswong3i@pantarei-design.com>  
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
FROM ubuntu:16.04  
ENV USERNAME ""  
ENV PASSWORD ""  
ENV DBHOST "localhost"  
ENV DBNAMES "all"  
ENV BACKUPDIR "/var/lib/automysqlbackup"  
ENV MAILCONTENT "stdout"  
ENV MAXATTSIZE "4000"  
ENV MAILADDR ""  
ENV MDBNAMES ""  
ENV DBEXCLUDE "mysql performance_schema information_schema"  
ENV CREATE_DATABASE "yes"  
ENV SEPDIR "yes"  
ENV DOWEEKLY "6"  
ENV COMP "gzip"  
ENV COMMCOMP "no"  
ENV LATEST "yes"  
ENV MAX_ALLOWED_PACKET ""  
ENV SOCKET ""  
ENV PREBACKUP ""  
ENV POSTBACKUP ""  
ENV ROUTINES "yes"  
VOLUME $BACKUPDIR  
WORKDIR $BACKUPDIR  
  
ENTRYPOINT [ "dumb-init", "--" ]  
CMD [ "automysqlbackup" ]  
  
# Prepare APT depedencies  
RUN set -ex \  
&& apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y automysqlbackup curl
patch \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install dumb-init  
RUN set -ex \  
&& curl -skL https://github.com/Yelp/dumb-init/releases/download/v1.2.1/dumb-
init_1.2.1_amd64 > /usr/local/bin/dumb-init \  
&& chmod 0755 /usr/local/bin/dumb-init  
  
# Copy files  
COPY files /  
  
# Apply patches  
RUN set -ex \  
&& patch -d/ -p1 < /.patch  

