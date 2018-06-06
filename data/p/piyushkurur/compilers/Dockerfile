# Docker file for the compilers course available at  
# https://bitbucket.org/piyush-kurur/compilers. You can use this to  
# build a ubuntu docker image suitable for the course. This docker  
# image is also used for CI at shippable.com of all the code samples  
# in the above repository.  
#  
# You can get the latest version of this docker file at  
#  
# https://bitbucket.org/piyush-kurur/compilers/src/master/Dockerfile  
#  
#########################################################################  
#  
# Copyright (c) 2017, Piyush P Kurur  
#  
# All rights reserved.  
#  
# Redistribution and use in source and binary forms, with or without  
# modification, are permitted provided that the following conditions are met:  
#  
# * Redistributions of source code must retain the above copyright  
# notice, this list of conditions and the following disclaimer.  
#  
# * Redistributions in binary form must reproduce the above  
# copyright notice, this list of conditions and the following  
# disclaimer in the documentation and/or other materials provided  
# with the distribution.  
#  
# * Neither the name of Piyush P Kurur nor the names of other  
# contributors may be used to endorse or promote products derived  
# from this software without specific prior written permission.  
#  
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS  
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT  
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR  
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT  
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,  
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT  
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,  
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY  
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT  
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE  
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.  
#  
  
FROM ubuntu:latest  
MAINTAINER Piyush P Kurur <ppk@cse.iitk.ac.in>  
  
RUN apt-get update -y  
RUN apt-get install sudo locales -y  
  
# Generate the locales.  
RUN sudo locale-gen en_US en_US.UTF-8  
RUN sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8  
  
# Install some basic packages required by the course. Mostly standard  
# ML compilers and compiler writing tools.  
  
RUN sudo apt-get install smlnj ml-yacc ml-lex ml-burg mlton make -y  

