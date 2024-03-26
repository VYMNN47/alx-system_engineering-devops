# Setup Ubuntu Server with nginx

package { 'nginx':
  ensure  => installed,
}

file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => "
server {
	listen 80;
	location / {
		return 200 'Hello World!';
        	add_header Content-Type text/plain;
    	}

    	location /redirect_me {
        	return 301 https://www.youtube.com/watch?v=dQw4w9WgXcQ;
    	}
}",
  notify  => Service['nginx'],
}

service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}
