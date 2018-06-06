# Run changeagent in a container  
#  
# Example:  
#  
# Optionally, create a directory on your docker host so that the data can be
persistently stored:  
#  
# mkdir ~/agent/data1  
#  
# Now run:  
#  
# docker run -it -p 8080:8080 \  
# -v /home/docker/agent/data1:/data changeagent  
#  
# Image details:  
#  
# Changeagent will listen on port 8080. Map it however you want.  
#  
# When it first starts, changeagent will be running in standalone mode.  
# To assemble a group of changeagent servers into a cluster, see the README.  
#  
# Each agent will store its database in /data. Since data is important,  
# this should be a persistent volume.  
# (If you choose not to create this directory, then the data will be stored  
# on the ephemeral volume created by Docker, and will go away when the  
# container is stopped.)  
# To get a pre-built copy of changeagent:  
# Build this image  
# "docker run -d" this image  
# "docker cp /changeagent ./changeagent"  
# "docker stop" the image  
# You now have the executable  
# This image has Git, Glide, and rocksdb pre-built for us.  
FROM gbrail/go-rocksdb:1.6.2-4.2  
COPY . /go/src/github.com/30x/changeagent  
  
RUN \  
(cd /go/src/github.com/30x/changeagent; glide install) \  
&& (cd /go/src/github.com/30x/changeagent; make clean all) \  
&& cp /go/src/github.com/30x/changeagent/changeagent / \  
&& mkdir /data \  
&& mkdir /keys \  
&& rm -r /go  
  
EXPOSE 8080 8443 9080  
VOLUME [ "/data" "/keys" ]  
  
ENV LD_LIBRARY_PATH=/usr/local/lib  
  
ENTRYPOINT ["/changeagent", "-logtostderr", "-p", "8080", "-d", "/data"]  

