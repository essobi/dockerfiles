FROM alpine:3.4  
MAINTAINER Arthur Axel fREW Schmidt <frioux@gmail.com>  
  
# Dockerfile defining a robust offlineimap container  
#  
# Copyright 2015 Arthur Axel fREW Schmidt  
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
CMD ["/usr/local/bin/generate_configs", "s6-svscan", "-S", "-t", "0",
"/home/user/services"]  
# declaring the volume makes it owned by root. Lame.  
# VOLUME ["/opt/var/mail", "/opt/var/index", "/opt/log/offlineimap",
"/opt/etc"]  
ADD ./offlineimaprc /home/user/.offlineimaprc  
ADD ./offlineimap.py /home/user/.offlineimap.py  
ADD ./bin/generate_configs /usr/local/bin/generate_configs  
ADD ./bin/setup /usr/local/bin/setup  
ADD ./bin/cerberus /usr/local/bin/cerberus  
ADD ./services /home/user/services  
  
RUN /usr/local/bin/setup  

