FROM jcai/nirvana-java  
MAINTAINER Jun Tsai <jcai@ganshane.com>  
  
RUN {\  
apt-get update \  
&& apt-get install -qqy numactl libaio-dev ; \  
}  
  
ADD apps/lib /dist/apps/lib  
ADD apps/doc /dist/apps/doc  
ADD apps/dic /dist/apps/dic  
ADD config /dist/config  
ADD apps/cloud /dist/apps/cloud  
ADD apps/ext-5 /dist/apps/ext-5  
ADD apps/group /dist/apps/group  
ADD apps/sync /dist/apps/sync  
ADD apps/node /dist/apps/node  
ADD apps/api /dist/apps/api  
  
WORKDIR /apps  
  
ENV release_path /dist  
ENV app_path /apps  
ENV _stage docker  
ENV comp cloud  
  
  
#cloud  
RUN {\  
ln -s ${release_path}/apps/${comp} ${app_path}/${comp} \  
&& ln -s ${release_path}/apps/doc ${app_path}/${comp}/doc \  
&& ln -s ${release_path}/config/${_stage}/${comp}/config ${app_path}/${comp}/
\  
&& cp ${release_path}/config/${_stage}/${comp}/${comp}rc ~/.${comp}rc \  
&& mkdir -p ${release_path}/apps/${comp}/lib \  
&& ln -s ${release_path}/apps/${comp}/private-lib/*
${release_path}/apps/${comp}/lib/ \  
&& ln -s ${release_path}/apps/lib/* ${release_path}/apps/${comp}/lib/ ; \  
}  
ENV comp group  
#group  
RUN {\  
ln -s ${release_path}/apps/${comp} ${app_path}/${comp} \  
&& ln -s ${release_path}/apps/doc ${app_path}/${comp}/doc \  
&& ln -s ${release_path}/config/${_stage}/${comp}/config ${app_path}/${comp}/
\  
&& cp ${release_path}/config/${_stage}/${comp}/${comp}rc ~/.${comp}rc \  
&& mkdir -p ${release_path}/apps/${comp}/lib \  
&& ln -s ${release_path}/apps/${comp}/private-lib/*
${release_path}/apps/${comp}/lib/ \  
&& ln -s ${release_path}/apps/lib/* ${release_path}/apps/${comp}/lib/ ; \  
}  
ENV comp sync  
#sync  
RUN {\  
ln -s ${release_path}/apps/${comp} ${app_path}/${comp} \  
&& ln -s ${release_path}/apps/doc ${app_path}/${comp}/doc \  
&& ln -s ${release_path}/config/${_stage}/${comp}/config ${app_path}/${comp}/
\  
&& cp ${release_path}/config/${_stage}/${comp}/${comp}rc ~/.${comp}rc \  
&& mkdir -p ${release_path}/apps/${comp}/lib \  
&& ln -s ${release_path}/apps/${comp}/private-lib/*
${release_path}/apps/${comp}/lib/ \  
&& ln -s ${release_path}/apps/lib/* ${release_path}/apps/${comp}/lib/ ; \  
}  
ENV comp node  
#node  
RUN {\  
ln -s ${release_path}/apps/${comp} ${app_path}/${comp} \  
&& ln -s ${release_path}/apps/doc ${app_path}/${comp}/doc \  
&& ln -s ${release_path}/apps/dic ${app_path}/${comp}/dic \  
&& ln -s ${release_path}/config/${_stage}/${comp}/config ${app_path}/${comp}/
\  
&& cp ${release_path}/config/${_stage}/${comp}/${comp}rc ~/.${comp}rc \  
&& mkdir -p ${release_path}/apps/${comp}/lib \  
&& ln -s ${release_path}/apps/${comp}/private-lib/*
${release_path}/apps/${comp}/lib/ \  
&& ln -s ${release_path}/apps/lib/* ${release_path}/apps/${comp}/lib/ ; \  
}  
ENV comp api  
#api  
RUN {\  
ln -s ${release_path}/apps/${comp} ${app_path}/${comp} \  
&& ln -s ${release_path}/apps/doc ${app_path}/${comp}/doc \  
&& ln -s ${release_path}/apps/dic ${app_path}/${comp}/dic \  
&& ln -s ${release_path}/config/${_stage}/${comp}/config ${app_path}/${comp}/
\  
&& cp ${release_path}/config/${_stage}/${comp}/${comp}rc ~/.${comp}rc \  
&& mkdir -p ${release_path}/apps/${comp}/lib \  
&& ln -s ${release_path}/apps/${comp}/private-lib/*
${release_path}/apps/${comp}/lib/ \  
&& ln -s ${release_path}/apps/lib/* ${release_path}/apps/${comp}/lib/ ; \  
}  
  
EXPOSE 9080 9081  
VOLUME ["/monad-data"]  
VOLUME ["/monad-log"]  
  
RUN apt-get install -yy net-tools wget  
  
ADD dockers/dev/run.sh /run.sh  
RUN chmod +x /run.sh  
  
ENTRYPOINT ["/run.sh"]  
  

