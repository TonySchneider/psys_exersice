# using the lightweight image as required (3.7-alpine)
FROM python:3.7-alpine

# copy the python accessible test
COPY accessible_test /accessible_test

# install ssh service (apk instead of apt since it's alpine image), rc tool & nmap
RUN apk update \
	&& apk add --update --no-cache openssh openrc nmap

# enable ssh service
RUN rc-update add sshd

# rc status
RUN rc-status

# need to open this file to be able start the service immediately
RUN mkdir -p /run/openrc \
	&& touch /run/openrc/softlevel

# start the service
RUN /etc/init.d/sshd start

# install python requirements
RUN python -m pip install -r accessible_test/requirements.txt

# just publish the ports at the image documentations
EXPOSE 22

# run the supervisord
CMD ["/usr/sbin/sshd", "-D"]