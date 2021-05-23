# using the lightweight image as required (stable-alpine)
FROM nginx:stable-alpine

# copy the hello-world html file and supervisord config for multiple services
COPY hello-world-static-html /usr/share/nginx/html/index.html
COPY supervisord.conf /etc/supervisord.conf

# must for the rc-update
VOLUME /sys/fs/cgroup

# install ssh service (apk instead of apt since it's alpine image) & install rc tool to be able enable services & supervisor
RUN apk update \
	&& apk add --update --no-cache openssh openrc supervisor

# enable ssh service
RUN rc-update add sshd

# rc status
RUN rc-status

# need to open this file to be able start the service immediately
RUN mkdir -p /run/openrc \
	&& touch /run/openrc/softlevel

# start the service
RUN /etc/init.d/sshd start

# just publish the ports at the image documentations
EXPOSE 80 22

# run the supervisord
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]