### DOCKERFILE for building containers  
  
FROM ubuntu:14.04  
  
  
##----------------------verify different logging drivers runtime '--log-
driver'  
ENTRYPOINT ping 0.0.0.0 -c 50  
  
##----------------------Check runtime variable setting using '-e'  
#COPY userdata/information.sh /userdata/  
#ENTRYPOINT information.sh $GUEST $TOWN  
##----------------------ARG working, STOPSIGNAL needs to be understood  
  
#ARG file  
#ARG var  
#COPY volume/userdata/ /userdata/  
#RUN if grep kill /userdata/$file; then STOPSIGNAL 9; fi  
#RUN echo "Looks like I am not killed " /userdata/killstatus  
  
  
##-----------------------Created image with ONBUILD  
##-----------------------Later used that as a base image and when new image
created and ran then it had executed ADD & COPY command mentioned.  
#FROM testbuild  
#Maintainer Manoj Chaudhari <manojchaudhari@hotmail.com>  
#  
#RUN echo "Test Onbuild behaviour" > /Onbuild.test  
#  
#ONBUILD ADD https://support.apple.com/en-us/HT201236 /userdata/  
#  
#ONBUILD COPY TE/test* /userdata/  
  
##------------------------User creation using ARG method...password didn't
work though.  
##------------------------Additionally volume is created under the ownership
of user created  
##------------------------Build command : "docker build --build-arg
user=tester -t testvol ."  
##------------------------NOTE: if you use -v HOST_dir:container_Dir then this
will override volume created while buildtime  
  
#ARG user  
##RUN mkdir /home/$user  
#RUN useradd -d /home/$user -s /bin/sh -m $user  
##RUN chown $user:$user /home/$user  
#USER $user  
#RUN mkdir ~/myvol  
#RUN echo "testing volumes " >~/myvol/newvolumetest  
#VOLUME ~/myvol  
  
#\---------------------------  
##-------------------------- My first docker file to build from Ubuntu:14.04
image  
#RUN apt-get update  
#FROM nginx  
#FROM ubuntu:14.04  
#Maintainer Manoj Chaudhari <manojchaudhari@hotmail.com>  
#COPY TE/test* /userdir/TEfiles/  
#WORKDIR /userdir/TEfiles  
#WORKDIR /userdata  
#CMD ["./test.sh","/userdir/TEfiles/test.param"]  
#ADD https://support.apple.com/en-us/HT201236 /userdata/  
#ADD bmw.results benz.results toyota.results /userdata/  
#RUN ./install.sh  
#ADD testdrive.tar /userdata/  
#ADD bmw.results /userdata/testresults  
#LABEL USER_FIRSTNAME="Manoj"  
#LABEL USER_LASTNAME="CHAUDHARI"  
#LABEL Description="this is all going to help\  
#docker study and practise. Continue doing what you are doing and build
amazing applications to help"  
#ADD userdata /userdata  
#COPY TE/test* /userdata/  
#ENV PATH /userdata/:$PATH  
#CMD ["test.param", "ENTRYPOINT"]  
#ENTRYPOINT ["test.sh","test.param","ENTRYPOINT"]  
#ENTRYPOINT ["top","-b"]  
#ARG scrpt  
##ADD userdata /userdata  
#COPY TE/test* /userdata/  
#ENV PATH /userdata/:$PATH  
#ENV SCT $scrpt  
#ENTRYPOINT ["$SCT","test.param","ENTRYPOINT"]  
#RUN echo $SCT >/userdata/SCT1  
#\---------------------------try to create an user and create directory then
volume  
#RUN useradd -d /home/e4ainst e4ainst  
#USER e4ainst  
##doesn't work -> RUN su - e4ainst -c mkdir ~/myvol  
#RUN echo "testing volumes " >~/myvol/newvolumetest  
#VOLUME ~/myvol  
#\-----------------------------see how CMD and ENTRYPOINT works hand in hand
(pretty bad so far)...  
#ADD userdata /userdata  
#COPY TE/test* /userdata/  
#ENV PATH /userdata/:$PATH  
#CMD ["test.sh","test1.param","TRY"]  
#CMD "test.sh" "test1.param" "TRY"  
#ENTRYPOINT ["test.sh","test.param","ENTRYPOINT"]  
#ENTRYPOINT "test.sh" "test.param" "ENTRYPOINT"  
  
#\-----------------------------  

