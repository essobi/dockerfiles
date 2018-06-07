# File: ./Dockerfile  
# Summary: An implementation for early-stage venture-backed startups.  
# License: MIT License  
# Company: Blockfreight, Inc.  
# Author: Julian Smith  
# Site: https://blockfreight.com  
# Support: <support@blockfreight.com>  
  
# Blockfreight, Inc. - OFBiz (ERP) Docker Image  
  
# Copyright © 2018 Blockfreight, Inc. All Rights Reserved.  
  
# Permission is hereby granted, free of charge, to any person obtaining  
# a copy of this software and associated documentation files (the "Software"),  
# to deal in the Software without restriction, including without limitation  
# the rights to use, copy, modify, merge, publish, distribute, sublicense,  
# and/or sell copies of the Software, and to permit persons to whom the  
# Software is furnished to do so, subject to the following conditions:  
  
# The above copyright notice and this permission notice shall be  
# included in all copies or substantial portions of the Software.  
  
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS  
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,  
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE  
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY,  
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR
IN  
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.  
  
#
=================================================================================================================================================  
#
=================================================================================================================================================  
  
# BBBBBBBBBBBb lll kkk ffff iii hhh ttt  
# BBBB``````BBBB lll kkk fff ``` hhh ttt  
# BBBB BBBB lll oooooo ccccccc kkk kkkk fffffff rrr rrr eeeee iii gggggg ggg
hhh hhhhh tttttttt  
# BBBBBBBBBBBB lll ooo oooo ccc ccc kkk kkk fffffff rrrrrrrr eee eeee iii gggg
ggggg hhhh hhhh tttttttt  
# BBBBBBBBBBBBBB lll ooo ooo ccc kkkkkkk fff rrrr eeeeeeeeeeeee iii gggg ggg
hhh hhh ttt  
# BBBB BBB lll ooo ooo ccc kkkk kkkk fff rrr eeeeeeeeeeeee iii ggg ggg hhh hhh
ttt  
# BBBB BBBB lll oooo oooo cccc ccc kkk kkkk fff rrr eee eee iii ggg gggg hhh
hhh tttt ....  
# BBBBBBBBBBBBB lll oooooooo ccccccc kkk kkkk fff rrr eeeeeeeee iii gggggg ggg
hhh hhh ttttt ....  
# ggg ggg  
# Blockfreight™ | The blockchain of global freight. ggggggggg  
  
#
=================================================================================================================================================  
#
=================================================================================================================================================  
  
# Use an official Ubuntu 16.04 Debian-based Linux operating system release as
a parent image.  
FROM ubuntu:16.04  
  
# Package Dockerfile is a package that defines the Blockfreight, Inc. - OFBiz
(ERP) Docker Image  
# and provides some useful functions to work with the BF_TX token ecosystem.  
MAINTAINER Julian Smith <julian.smith@blockfreight.com>  
  
# Enable Doccker Ports - Primary ['1'] Secondary ['2'] Tertiary ['3']  
# 80:http(1) 443:https(1) 5432:PostgreSQL(1) 8080:http(2) 8081:http(3)
8443:https(2)  
EXPOSE 80 443 5432 8080 8081 8443  
  
RUN echo "debconf shared/accepted-oracle-license-v1-1 select true" | debconf-
set-selections  
RUN echo "debconf shared/accepted-oracle-license-v1-1 seen true" | debconf-
set-selections  
RUN export DEBIAN_FRONTEND=noninteractive  
  
RUN apt update -y  
RUN apt upgrade -y  
  
# Update package manager and update default applications.  
RUN apt install -y software-properties-common wget unzip net-tools  
RUN add-apt-repository -y ppa:webupd8team/java  
RUN apt update -y  
RUN apt install -y oracle-java8-installer  
  
RUN echo "export JAVA_HOME=/usr/lib/jvm/java-8-oracle" >> ~/.bashrc  
RUN /bin/bash -c "source ~/.bashrc"  
  
# Install pre-requisites applications to support OFBiz in production.  
  
# Install PostgreSQL - core database server  
# RUN apt­get install postgresql-9.6  
# PostgreSQL - client libraries and client binaries  
# RUN apt­get install postgresql-client-9.6  
# PostgreSQL - additional supplied modules  
# RUN apt­get install postgresql-contrib-9.6  
# PostgreSQL - libraries and headers for C language frontend development  
# RUN apt­get install libpq-dev  
# PostgreSQL - libraries and headers for C language backend development  
# RUN apt­get install postgresql-server-dev-9.6  
# PostgreSQL - pgAdmin III graphical administration utility  
# RUN apt­get install pgadmin3  
# Install PostgreSQL - PostgreSQL ­Java Library  
# RUN apt­get install libpostgresql­java  
  
# Setup PostgreSQL  
#RUN -i -u postgres  
#RUN psql  
  
#RUN CREATE USER root WITH PASSWORD 'root';  
#RUN CREATE DATABASE "test";  
#RUN GRANT ALL ON DATABASE "test" TO root;  
#RUN \q  
#RUN $ exit  
  
# Notes: postgresql libpq5 postgresql-9.5 postgresql-client-9.5 postgresql-
client-common postgresql-contrib  
  
# Install NGinx  
#RUN apt­get install nginx­full  
  
# Install the reference implementation of OFBiz  
RUN wget http://mirror.dsrg.utoronto.ca/apache/ofbiz/apache-ofbiz-16.11.04.zip  
RUN unzip apache-ofbiz-16.11.04.zip  
  
# Install the reference implementation of OFBiz  
WORKDIR apache-ofbiz-16.11.04  
RUN ./gradlew cleanAll loadDefault  
CMD ./gradlew ofbiz  
  
# TODO  
  
# Web Proxy - Add NGinx  
# Data - Add Persistent Storage  

