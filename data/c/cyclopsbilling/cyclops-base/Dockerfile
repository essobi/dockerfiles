# Copyright (c) 2015. Zuercher Hochschule fuer Angewandte Wissenschaften  
# All Rights Reserved.  
#  
# Licensed under the Apache License, Version 2.0 (the "License"); you may  
# not use this file except in compliance with the License. You may obtain  
# a copy of the License at  
#  
# http://www.apache.org/licenses/LICENSE-2.0  
#  
# Unless required by applicable law or agreed to in writing, software  
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT  
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the  
# License for the specific language governing permissions and limitations  
# under the License.  
#  
# Author: Piyush Harsh,  
# URL: piyush-harsh.info  
#  
# Thanks to: https://hub.docker.com/_/java/  
FROM ubuntu:14.04  
EXPOSE 4567 4568 4569 4570 4571 4572  
  
RUN apt-get update  
RUN apt-get install -y software-properties-common  
RUN add-apt-repository -y ppa:webupd8team/java  
RUN apt-get -y update  
RUN apt-get install -y maven git nano  
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true | sudo /usr/bin/debconf-set-selections && apt-get install -y oracle-
java8-installer && update-java-alternatives -s java-8-oracle && apt-get
install -y oracle-java8-set-default  

