#  
# Dockerfile  
#  
# Copyright (c) 2016-2017 Junpei Kawamoto  
#  
# This file is part of Roadie queue manager.  
#  
# Roadie queue manager is free software: you can redistribute it and/or modify  
# it under the terms of the GNU General Public License as published by  
# the Free Software Foundation, either version 3 of the License, or  
# (at your option) any later version.  
#  
# Roadie queue manager is distributed in the hope that it will be useful,  
# but WITHOUT ANY WARRANTY; without even the implied warranty of  
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the  
# GNU General Public License for more details.  
#  
# You should have received a copy of the GNU General Public License  
# along with Roadie queue manager. If not, see <http://www.gnu.org/licenses/>.  
#  
FROM ubuntu:latest  
MAINTAINER Junpei Kawamoto <kawamoto.junpei@gmail.com>  
  
ENV TERM vt100  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install necessary packages  
RUN apt-get update && \  
apt-get install -y apt-utils curl git gcc python-dev python-setuptools libssl-
dev libffi-dev python-pip unzip && \  
apt-get clean && \  
rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/  
RUN pip install -U pip pycrypto pyOpenSSL crcmod gsutil  
RUN echo "[GoogleCompute]\nservice_account =
default\n[GSUtil]\nparallel_composite_upload_threshold = 150M" >>
/etc/boto.cfg  

